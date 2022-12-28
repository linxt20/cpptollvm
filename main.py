from antlr4 import *
import sys
import ast

from src.cpp14Lexer import cpp14Lexer
from src.cpp14Parser import cpp14Parser
from src.cpp14ParserListener import cpp14ParserListener as cpp14Listener
from src.cpp14ParserVisitor import cpp14ParserVisitor as cpp14Visitor
from llvmlite.ir.types import ArrayType
from llvmlite.ir.values import GlobalVariable, ReturnValue
from table import *
from utils import *
import llvmlite.ir as ir

double = ir.DoubleType()
int1 = ir.IntType(1)
int8 = ir.IntType(8)
int16 = ir.IntType(16)
int32 = ir.IntType(32)
int64 = ir.IntType(64)
void = ir.VoidType()

int8p = ir.PointerType(int8)
int16p = ir.PointerType(int16)
int32p = ir.PointerType(int32)
int64p = ir.PointerType(int64)
doublep = ir.PointerType(double)


class NewCpp14Visitor(cpp14Visitor):
    def __init__(self):
        super(cpp14Visitor, self).__init__()

        self.irModule = ir.Module()  # llvm生成模块
        self.irBuilder = []  # 待生成的llvm语句块，新生成的语句在末尾
        self.symbolTable = NameTable()  # 符号表
        
        self.switch_expression = []  # 用于存储switch表达式的结果，来与case匹配
        self.switch_case_label = []  # 用于存储switch表达式中label的值

        # break,continue语句跳转到的block
        self.blockToBreak = []
        self.blockToContinue = []

        self.string_count = 0  # 全局字符串的数量

        self.irModule.triple = "x86_64-pc-linux"

        self.type = None

    def visitLiterals(self, ctx: cpp14Parser.LiteralsContext):
        literals = self.visit(ctx.getChild(0))
        return literals

    # Visit a parse tree produced by cpp14Parser#floatingLiteral.
    def visitFloatingLiteral(self, ctx: cpp14Parser.FloatingLiteralContext):
        floating_literal = {
                            'type': double,
                            'value': ir.Constant(double, float(ctx.getText()))
                          }
        return floating_literal

    # Visit a parse tree produced by cpp14Parser#integerLiteral.
    def visitIntegerLiteral(self, ctx: cpp14Parser.IntegerLiteralContext):
        signed = True                                                           # 考虑需不需要
        text = ctx.getText()
        if text[-2:] == 'll' or text[-2:] == 'LL':
            return_type = int64
            text_without_suffix = text[:-2]
        else:
            return_type = int32
            if text[-1] == 'l' or text[-2:-1] == 'L':
                text_without_suffix = text[:-1]
            else:
                text_without_suffix = text
        
        integer_literal = {
                            'type': return_type,
                            'signed': signed,                                    # 和上面一起
                            'value': ir.Constant(return_type, int(text_without_suffix))
                        }
        return integer_literal

    # Visit a parse tree produced by cpp14Parser#characterLiteral.
    def visitCharacterLiteral(self, ctx: cpp14Parser.CharacterLiteralContext):
        character_literal = {
                                'type': int8,
                                'value': ir.Constant(int8, ord(ctx.getText()[1]))
                            }
        return character_literal

    # Visit a parse tree produced by cpp14Parser#stringLiteral.
    def visitStringLiteral(self, ctx: cpp14Parser.StringLiteralContext):

        # 一个不大确定的操作，可以在这里用全局变量，将识别到的字符串归于其中
        s = ast.literal_eval(ctx.getText()) + '\0'
        
        string_type = ArrayType(int8, len(s))
        string_address = ir.GlobalVariable(self.irModule, string_type, '__string_' + str(self.string_count))
        string_address.linkage = 'internal'
        string_address.initializer = ir.Constant(string_type, None)
        string_address.initializer = ir.Constant(string_type, bytearray(s, encoding='ascii'))
        self.string_count += 1
        if self.symbolTable.current_scope_level != 0:
            # a local variable
            builder = self.irBuilder[-1]
            string_address = builder.gep(string_address, [ir.Constant(int32, 0), ir.Constant(int32, 0)], inbounds=True)
        string_literal = {
                            'type': string_type,
                            'value': string_address
                        }     

        return string_literal

    # Visit a parse tree produced by cpp14Parser#constExpression.
    def visitConstExpression(self, ctx: cpp14Parser.ConstExpressionContext):
        return self.visit(ctx.literals())

    # Visit a parse tree produced by cpp14Parser#leftExpression.
    def visitLeftExpression(self, ctx: cpp14Parser.LeftExpressionContext):
        if ctx.getText()[-1] == ']':
            
            '''
            对应语法: leftExpression:Identifier (LSQUARE expression RSQUARE)
            '''
            index = self.symbolTable.getProperty(ctx.getChild(0).getText())
            subscribe = self.visit(ctx.getChild(2))['value']
            if isinstance(index.get_type(), ir.types.ArrayType):
                builder = self.irBuilder[-1]
                address = builder.gep(index.get_value(), [ir.Constant(int32, 0), subscribe], inbounds=True)
                return_value = builder.load(address)
                print("call arrayItem", return_value)
                left_expression = {
                                    'type': index.get_type().element,
                                    'signed': True,
                                    'address': address
                                }
                return left_expression
            else:
                raise BaseException("the array isn't defined")
            
        else:
            '''
            对应语法: leftExpression:Identifier
            '''
            symbol = self.symbolTable.getProperty(ctx.getText())
            left_expression = {
                                'type': symbol.get_type(),
                                'signed': symbol.get_signed(),
                                'address': symbol.get_value(),
                            }
            return left_expression

    # Visit a parse tree produced by cpp14Parser#expression.
    def visitExpression(self, ctx: cpp14Parser.ExpressionContext):
        child_count = ctx.getChildCount()
        builder = self.irBuilder[-1]
        if child_count == 1:
            grand_children = ctx.getChild(0).getChildCount()
            if grand_children:
                '''
                对应语法: expression: Literals|functionCall;
                '''
                result = self.visit(ctx.getChild(0))
                return result
            else:
                '''
                对应语法: expression: Identifier
                '''
                
                symbol = self.symbolTable.getProperty(ctx.getText())
                # 读地址再 load 进来
                if isinstance(symbol.get_type(), ir.ArrayType):
                    expression = {
                                    'type': symbol.get_type().element.as_pointer(),
                                    'value': builder.gep(symbol.get_value(), [ir.Constant(int32, 0), ir.Constant(int32, 0)], inbounds=True)
                                }
                    return expression
                else:
                    ret_value = builder.load(symbol.get_value())
                    expression = {
                                    'type': ret_value.type,
                                    'signed': symbol.get_signed(),
                                    'value': ret_value
                                }
                    return expression

        elif child_count == 2:
            '''
            对应语法: expression: NOT expression | SUB expression
            对应语法: leftexpression MINUS_MINUS | leftexpression PLUS_PLUS
            '''  
            if ctx.getChild(0).getText() == '-' or ctx.getChild(0).getText() == '!' or ctx.getChild(0).getText() == '&':
                builder = self.irBuilder[-1]
                result = self.visit(ctx.getChild(1))
                if ctx.getChild(0).getText() == '!':
                    if result['type'] == double:
                        return_value = builder.fcmp_ordered('!=', result['value'], ir.Constant(int1, 0))
                    else:
                        return_value = builder.icmp_signed('!=', result['value'], ir.Constant(int1, 0))
                    expression = {
                                    'type': int1,
                                    'signed': True,
                                    'value': return_value
                                }
                    return expression
                elif ctx.getChild(0).getText() == '-':
                    if result['type'] == double:
                        return_value = builder.fneg(result['value'])
                    else:
                        return_value = builder.neg(result['value'])
                    expression = {
                                    'type': result['type'],
                                    'signed': True,
                                    'value': return_value
                                }
                    return expression
                elif ctx.getChild(0).getText() == '&':
                    expression = {
                                    'type': result['type'].as_pointer(),
                                    'signed': True,
                                    'value': result['address']
                                }
                    return expression
            else:
                # 减减或者加加
                builder = self.irBuilder[-1]
                lhs = self.visit(ctx.getChild(0))
                # 先 load, address 就是地址
                now_value = builder.load(lhs['address'])
                # 再 + 1 / -1
                if ctx.getChild(1).getText() == '++':
                    return_value = builder.add(now_value, ir.Constant(lhs['type'], 1))
                else:
                    return_value = builder.sub(now_value, ir.Constant(lhs['type'], 1))
                # 存储
                builder.store(return_value, lhs['address'])
                expression = {
                                'type': lhs['type'],
                                'signed': True,
                                'value': return_value
                            }    
                return expression
        elif child_count > 3:
            '''
            对应语法: expression: Identifier '[' expression ']'
            '''
            index = self.symbolTable.getProperty(ctx.getChild(0).getText())
            subscribe = self.visit(ctx.getChild(2))['value']
            if isinstance(index.get_type(), ir.types.ArrayType):
                builder = self.irBuilder[-1]
                address = builder.gep(index.get_value(), [ir.Constant(int32, 0), subscribe], inbounds=True)
                return_value = builder.load(address)
                print("call arrayItem", return_value)
                expression = {
                                'type': index.get_type().element,
                                'signed': True,
                                'value': return_value
                            }
                return expression
            else:
                raise BaseException("the array isn't defined")

        elif child_count == 3 and ctx.getChild(0).getText() == '(':
            '''
            对应语法: expression: '(' expression ')'
            '''
            result = self.visit(ctx.getChild(1))
            return result

        else:
            operation = ctx.getChild(1).getText()
            # print(f"operation:{operation},child0:{ctx.getChild(0).getText()},child2:{ctx.getChild(2).getText()}")

            left = self.visit(ctx.getChild(0))
            right = self.visit(ctx.getChild(2))
            if self.isExprJudge(operation):
                '''
                对应语法:  expression: expression '==' | '!=' | '<' | '<=' | '>' | '>=' expr
                '''
                left, right = exprTypeConvert(left, right, self.irBuilder[-1])
                if left['type'] == double:
                    return_value = builder.fcmp_ordered(operation, left['value'], right['value'])
                else:
                    if left['signed']:
                        return_value = builder.icmp_signed(operation, left['value'], right['value'])
                    else:
                        return_value = builder.icmp_unsigned(operation, left['value'], right['value'])
                expression = {
                                'type': int1,
                                'signed': True,
                                'value': return_value
                            }          
                return expression

            elif operation == '+' or operation == '-' or operation == '*' or operation == '/' or operation == '%' or operation == '<<' or operation == '>>':
                '''
                对应语法: expression: expression '+'|'-'|'*'|'/'|'%' expression
                '''
                left, right = exprTypeConvert(left, right, self.irBuilder[-1])
                if operation == '+':
                    if left['type'] == double:
                        return_value = builder.fadd(left['value'], right['value'])
                    else:
                        return_value = builder.add(left['value'], right['value'])
                elif operation == '-':
                    if left['type'] == double:
                        return_value = builder.fsub(left['value'], right['value'])
                    else:
                        return_value = builder.sub(left['value'], right['value'])
                elif operation == '*':
                    if left['type'] == double:
                        return_value = builder.fmul(left['value'], right['value'])
                    else:
                        return_value = builder.mul(left['value'], right['value'])
                elif operation == '/':
                    if left['type'] == double:
                        return_value = builder.fdiv(left['value'], right['value'])
                    else:
                        return_value = builder.sdiv(left['value'], right['value'])
                elif operation == '%':
                    if left['type'] == double:
                        return_value = builder.srem(left['value'], right['value'])
                    else:
                        return_value = builder.frem(left['value'], right['value'])
                elif operation == '<<':
                    return_value = builder.shl(left['value'], right['value'])
                else:
                    return_value = builder.lshr(left['value'], right['value'])
                expression = {
                                'type': right['type'],
                                'signed': True,
                                'value': return_value
                            }
                return expression

            elif operation == '=':
                '''
                对应语法:  expression: leftExpression '=' expression
                '''
                print(left, " is an variable")

                right = self.assignTypeConvert(left, right)  # 强制类型转换
                builder.store(right['value'], left['address'])
                expression = {'type': right['type'], 'value': builder.load(left['address'])}
                return expression

            elif operation == '|' or operation == '&' or operation == '^':
                '''
                对应语法:  expression: expression BITOR|BITAND|XOR expression
                '''
                left, right = exprTypeConvert(left, right, self.irBuilder[-1])
                signed = False
                if left['signed'] or right['signed']:
                    signed = True
                if operation == '|':
                    return_value = builder.or_(left['value'], right['value'])
                elif operation == '&':
                    return_value = builder.and_(left['value'], right['value'])
                else:
                    return_value = builder.xor(left['value'], right['value'])
                expression = {'type': left['type'], 'signed': signed, 'value': return_value}
                return expression
            
            elif operation == '&&' or operation == '||':
                '''
                对应语法: expression AND|OR expression
                '''
                left = toBool(left, self.irBuilder[-1])
                right = toBool(right, self.irBuilder[-1])
                if operation == '&&':
                    return_value = builder.and_(left['value'], right['value'])
                else:
                    return_value = builder.or_(left['value'], right['value'])
                expression = {'type': int1, 'signed': True, 'value': return_value}
                return expression

    # Visit a parse tree produced by cpp14Parser#block.
    def visitBlock(self, ctx: cpp14Parser.BlockContext):
        self.symbolTable.enterScope()
        super().visitBlock(ctx)
        self.symbolTable.exitScope()
        return

    # Visit a parse tree produced by cpp14Parser#functionCall.
    def visitFunctionCall(self, ctx: cpp14Parser.FunctionCallContext):
        '''
        对应语法: functionCall : Identifier LPAREN (expression (COMMA expression)*)? RPAREN;
        '''
        builder = self.irBuilder[-1]
        function_name = ctx.Identifier().getText()
        property = self.symbolTable.getProperty(function_name)
        if property.get_type().__class__.__name__ == ir.FunctionType.__name__:
            # 参数列表
            param_list = []
            for expression in ctx.expression():
                expression_value = self.visit(expression) 
                param_list.append(expression_value['value'])
            # 检查合法性

            if property.get_type().var_arg:
                # 只和vararg之前的比较
                valid_param_list = param_list[:len(property.get_type().args)]
            else:
                valid_param_list = param_list

            if len(valid_param_list) != len(property.get_type().args):
                raise BaseException("wrong args number")
            for real_param, param in zip(valid_param_list, property.get_type().args):
                if param != real_param.type:
                    raise BaseException("wrong args type", real_param.type, param)
            # 函数调用
            ret_value = builder.call(property.get_value(), param_list, name='', cconv=None, tail=False, fastmath=())
            ret_type = property.get_type().return_type
            return {
                "type": ret_type,
                'value': ret_value
            }
        else:
            raise BaseException("not a function name")

    # Visit a parse tree produced by cpp14Parser#ifStatement.
    def visitIfStatement(self, ctx: cpp14Parser.IfStatementContext):
        '''
        ifStatement : IF LPAREN expression RPAREN statement (ELSE statement)?;
        '''

        self.symbolTable.enterScope()
        builder = self.irBuilder[-1]
        true_block = builder.append_basic_block()

        # if else的情况
        if len(ctx.statement()) == 2:
            falseblock = builder.append_basic_block()
            end_block = builder.append_basic_block()
            
            # 条件跳转
            result = self.visit(ctx.getChild(2))
            condition = self.toBool(result)
            builder.cbranch(condition['value'], true_block, falseblock)
            
            # if块
            true_block_builder = ir.IRBuilder(true_block)
            self.irBuilder.pop()
            self.irBuilder.append(true_block_builder)
            self.visit(ctx.getChild(4))
            if not self.irBuilder[-1].block.is_terminated:
                self.irBuilder[-1].branch(end_block)
            
            # else块
            falseblockbuilder = ir.IRBuilder(falseblock)
            self.irBuilder.pop()
            self.irBuilder.append(falseblockbuilder)
            self.visit(ctx.getChild(6))
            # self.Builders[-1].branch(end_block)
            if not self.irBuilder[-1].block.is_terminated:
                self.irBuilder[-1].branch(end_block)
            
            # endif标识符
            self.irBuilder.pop()
            self.irBuilder.append(ir.IRBuilder(end_block))
            
        # 只有if没有else的情况
        else:
            end_block = builder.append_basic_block()
            
            # 条件跳转
            result = self.visit(ctx.getChild(2))
            condition = toBool(result, self.irBuilder[-1])
            builder.cbranch(condition['value'], true_block, end_block)
            
            # if块
            true_block_builder = ir.IRBuilder(true_block)
            self.irBuilder.pop()
            self.irBuilder.append(true_block_builder)
            self.visit(ctx.getChild(4))
            if not self.irBuilder[-1].block.is_terminated:
                self.irBuilder[-1].branch(end_block)
            
            # endif标识符
            self.irBuilder.pop()
            self.irBuilder.append(ir.IRBuilder(end_block))

        self.symbolTable.exitScope()

####################################################################################

    # Visit a parse tree produced by cpp14Parser#caseStatement.
    def visitCaseStatement(self, ctx: cpp14Parser.CaseStatementContext):
        """
        caseStatement : CASE constExpression COLON statement;
        """
        # return self.visitChildren(ctx)
        self.symbolTable.enterScope()
        judge_block = self.switch_case_label[-1][0]
        statement_block = self.switch_case_label[-1][1]
        target_judge_block = self.switch_case_label[-1][2]
        target_statement_block = self.switch_case_label[-1][3]

        judge_builder = ir.IRBuilder(judge_block)

        left = self.switch_expression[-1]
        right = self.visit(ctx.getChild(1))

        left, right = exprTypeConvert(left, right, self.irBuilder[-1])
        operation = '=='
        if left['type'] == double:
            return_value = judge_builder.fcmp_ordered(operation, left['value'], right['value'])
        else:
            if left['signed']:
                return_value = judge_builder.icmp_signed(operation, left['value'], right['value'])
            else:
                return_value = judge_builder.icmp_unsigned(operation, left['value'], right['value'])

        judge_builder.cbranch(return_value, statement_block, target_judge_block)

        self.irBuilder.pop()
        self.irBuilder.append(ir.IRBuilder(statement_block))
        self.visit(ctx.getChild(3))
        if not self.irBuilder[-1].block.is_terminated:
            self.irBuilder[-1].branch(target_statement_block)

        self.symbolTable.exitScope()

        self.switch_case_label[-1].pop(0)
        self.switch_case_label[-1].pop(0)
        return

    # Visit a parse tree produced by cpp14Parser#switchStatement.
    def visitSwitchStatement(self, ctx: cpp14Parser.SwitchStatementContext):
        # return self.visitChildren(ctx)
        self.symbolTable.enterScope()
        case_num = ctx.getChildCount() - 6
        builder = self.irBuilder[-1]

        result = self.visit(ctx.getChild(2))
        self.switch_expression.append(result)

        temp_array = []
        for i in range(case_num * 2 + 2):
            temp_array.append(builder.append_basic_block())
        self.switch_case_label.append(temp_array)
        self.blockToBreak.append(temp_array[-1])
        end_switch = temp_array[-1]

        builder.branch(temp_array[0])

        for i in range(case_num):
            self.visit(ctx.getChild(i + 5))

        assert len(self.switch_case_label[-1]) == 2
        ir.IRBuilder(self.switch_case_label[-1][0]).branch(self.switch_case_label[-1][1])
        self.irBuilder.pop()
        self.irBuilder.append(ir.IRBuilder(self.switch_case_label[-1][1]))

        self.switch_expression.pop()
        self.switch_case_label.pop()
        self.blockToBreak.pop()

        self.symbolTable.exitScope()
        return

    # Visit a parse tree produced by cpp14Parser#whileStatement.
    def visitWhileStatement(self, ctx: cpp14Parser.WhileStatementContext):
        builder = self.irBuilder[-1]
        # 新建三个块，代表判断条件，while循环内部块，while循环外
        expression_block = builder.append_basic_block()
        while_statement_block = builder.append_basic_block()
        end_while_block = builder.append_basic_block()

        self.blockToBreak.append(end_while_block)
        self.blockToContinue.append(expression_block)

        # expression_block
        builder.branch(expression_block)
        self.irBuilder.pop()
        self.irBuilder.append(ir.IRBuilder(expression_block))
        result = self.visit(ctx.getChild(2))
        condition = toBool(result, self.irBuilder[-1])
        self.irBuilder[-1].cbranch(condition['value'], while_statement_block, end_while_block)

        # while_statement_block
        self.irBuilder.pop()
        self.irBuilder.append(ir.IRBuilder(while_statement_block))
        print("this blocktobreak", self.blockToBreak[-1])
        self.visit(ctx.getChild(4))
        if not self.irBuilder[-1].block.is_terminated:
            self.irBuilder[-1].branch(expression_block)

        # end_while_block
        self.irBuilder.pop()
        self.irBuilder.append(ir.IRBuilder(end_while_block))

        self.blockToContinue.pop()
        self.blockToBreak.pop()
        return

    # Visit a parse tree produced by cpp14Parser#doWhileStatement.
    def visitDoWhileStatement(self, ctx: cpp14Parser.DoWhileStatementContext):
        builder = self.irBuilder[-1]
        # 新建语法块，do_statement_block,expression_block,end_while_block
        do_statement_block = builder.append_basic_block()
        expression_block = builder.append_basic_block()
        end_while_block = builder.append_basic_block()
        self.blockToBreak.append(end_while_block)
        self.blockToContinue.append(expression_block)

        # do_statement_block
        self.irBuilder.pop()
        self.irBuilder.append(ir.IRBuilder(do_statement_block))
        self.visit(ctx.getChild(1))
        if not self.irBuilder[-1].block.is_terminated:
            self.irBuilder[-1].branch(expression_block)

        # expression_block
        self.irBuilder[-1].branch(expression_block)
        self.irBuilder.pop()
        self.irBuilder.append(ir.IRBuilder(expression_block))
        result = self.visit(ctx.getChild(4))
        condition = toBool(result, self.irBuilder[-1])
        self.irBuilder[-1].cbranch(condition['value'], do_statement_block, end_while_block)

        # end_while_block
        self.irBuilder.pop()
        self.irBuilder.append(ir.IRBuilder(end_while_block))
        self.blockToContinue.pop()
        self.blockToBreak.pop()
        return

    # Visit a parse tree produced by cpp14Parser#forStatement.
    def visitForStatement(self, ctx: cpp14Parser.ForStatementContext):
        builder = self.irBuilder[-1]
        # 判断三个expression是否存在
        child_count = ctx.getChildCount()
        flag1 = True
        flag2 = True
        flag3 = True

        if ctx.getChild(2).getText() == ';':
            flag1 = False
        for i in range(child_count - 1):
            text1 = ctx.getChild(i).getText()
            text2 = ctx.getChild(i + 1).getText()
            if text1 == ';' and text2 != ';':
                expression_index = i + 1
                break
            if text1 == text2:
                flag2 = False
        if ctx.getChild(child_count - 3).getText() == ';':
            flag3 = False

        # 运行第一个forExprSet的语句
        if flag1:
            self.visit(ctx.getChild(2))

        # 新建语法块，judge_block,loop_block,for_expr3_block,end_loop_block
        judge_block = builder.append_basic_block()
        loop_block = builder.append_basic_block()
        for_expr3_block = builder.append_basic_block()
        end_loop_block = builder.append_basic_block()
        self.blockToBreak.append(end_loop_block)
        self.blockToContinue.append(for_expr3_block)

        # judge_block
        if flag2:
            self.irBuilder[-1].branch(judge_block)
            self.irBuilder.pop()
            self.irBuilder.append(ir.IRBuilder(judge_block))
            result = self.visit(ctx.getChild(expression_index))
            condition = toBool(result, self.irBuilder[-1])
            self.irBuilder[-1].cbranch(condition['value'], loop_block, end_loop_block)

        # loop_block
        self.irBuilder.pop()
        self.irBuilder.append(ir.IRBuilder(loop_block))
        self.visit(ctx.getChild(child_count - 1))
        if not self.irBuilder[-1].block.is_terminated:
            self.irBuilder[-1].branch(for_expr3_block)

        # for_expr3_block
        self.irBuilder.pop()
        self.irBuilder.append(ir.IRBuilder(for_expr3_block))
        if flag3:
            self.visit(ctx.getChild(child_count - 3))
        if flag2:
            self.irBuilder[-1].branch(judge_block)
        else:
            self.irBuilder[-1].branch(loop_block)

        # end_loop_block
        self.irBuilder.pop()
        self.irBuilder.append(ir.IRBuilder(end_loop_block))
        self.blockToBreak.pop()
        self.blockToContinue.pop()
        return

    # Visit a parse tree produced by cpp14Parser#returnStatement.
    def visitReturnStatement(self, ctx: cpp14Parser.ReturnStatementContext):
        if ctx.expression() is None:
            self.irBuilder[-1].ret_void()
        else:
            self.irBuilder[-1].ret(self.visit(ctx.expression())['value'])
        return

    # Visit a parse tree produced by cpp14Parser#breakStatement.
    def visitBreakStatement(self, ctx: cpp14Parser.BreakStatementContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by cpp14Parser#continueStatement.
    def visitContinueStatement(self, ctx: cpp14Parser.ContinueStatementContext):
        if self.blockToContinue:
            builder = self.irBuilder[-1]
            builder.branch(self.blockToContinue[-1])
        else:
            raise BaseException("cannot continue")
        return

    # Visit a parse tree produced by cpp14Parser#normalArrDecl.
    def visitNormalArrDecl(self, ctx:cpp14Parser.NormalArrDeclContext):
        array_length = int(ctx.getChild(3).getText())
        # 数据类型
        array_type = self.visit(ctx.getChild(0))
        llvm_array_type = ir.ArrayType(array_type, array_length)
        # 数据标识符
        array_name = ctx.getChild(1).getText()
        # 变量的声明
        if self.symbolTable.current_scope_level == 0:
            new_var = ir.GlobalVariable(self.irModule, llvm_array_type, name=array_name)
            new_var.linkage = 'internal'
            new_var.initializer = ir.Constant(llvm_array_type, None)
        else:
            builder = self.irBuilder[-1]
            new_var = builder.alloca(llvm_array_type, name=array_name)

        symbol_property = NameProperty(llvm_array_type, new_var)
        self.symbolTable.addLocal(array_name, symbol_property)
        child_count = ctx.getChildCount()
        if child_count > 6:
            # 赋初值给数组中的元素
            child_to_be_visited = 8
            element_index = 0
            builder = self.irBuilder[-1]
            while element_index < array_length and child_to_be_visited < child_count:
                address = builder.gep(new_var, [ir.Constant(int32, 0), ir.Constant(int32, element_index)])
                value_to_be_stored = self.visit(ctx.getChild(child_to_be_visited))['value']
                builder.store(value_to_be_stored, address)
                child_to_be_visited += 2
                element_index += 1

    # Visit a parse tree produced by cpp14Parser#stringDecl.
    def visitStringDecl(self, ctx: cpp14Parser.StringDeclContext):
        array_length = int(ctx.DecimalLiteral().getText())
        # 数据类型
        array_type = self.visit(ctx.charTypeSpecifier())
        llvm_array_type = ir.ArrayType(array_type, array_length)
        # 数据标识符
        array_name = ctx.Identifier().getText()
        # 变量的声明
        if self.symbolTable.current_scope_level == 0:
            if ctx.stringLiteral() is not None:
                new_var = self.visit(ctx.stringLiteral())['value']
            else:
                new_var = ir.GlobalVariable(self.irModule, llvm_array_type, name=array_name)
                new_var.linkage = 'internal'
                new_var.initializer = ir.Constant(llvm_array_type, None)
        else:
            builder = self.irBuilder[-1]
            new_var = builder.alloca(llvm_array_type, name=array_name)
            if ctx.stringLiteral() is not None:
                string = ast.literal_eval(ctx.stringLiteral().getText())
                char_num = len(string)
                element_index = 0
                while element_index < char_num:
                    char_to_be_stored = ir.Constant(array_type, ord(string[element_index]))
                    address = builder.gep(new_var, [ir.Constant(int32, 0), ir.Constant(int32, element_index)])
                    builder.store(char_to_be_stored, address)
                    element_index += 1

        symbol_property = NameProperty(llvm_array_type, new_var)
        self.symbolTable.addLocal(array_name, symbol_property)
        return

    # Visit a parse tree produced by cpp14Parser#varDeclWithoutInit.
    def visitVarDeclWithoutInit(self, ctx: cpp14Parser.VarDeclWithoutInitContext):
        if self.symbolTable.current_scope_level == 0:
            # 全局变量
            new_var = GlobalVariable(self.irModule, self.type, ctx.Identifier().getText())
            new_var.linkage = 'internal'
            new_var.initializer = ir.Constant(self.type, None)
            self.symbolTable.addGlobal(ctx.Identifier().getText(), NameProperty(_type=self.type, value=new_var))
        else:
            # 局部变量
            builder = self.irBuilder[-1]
            # 分配空间
            new_var = builder.alloca(self.type, name=ctx.Identifier().getText())
            # 存上初值
            builder.store(ir.Constant(self.type, None), new_var)
            # 存到符号表里面
            self.symbolTable.addLocal(ctx.Identifier().getText(), NameProperty(_type=self.type, value=new_var))
        return

    # Visit a parse tree produced by cpp14Parser#varDeclWithConstInit.
    def visitVarDeclWithConstInit(self, ctx: cpp14Parser.VarDeclWithConstInitContext):
        if self.symbolTable.current_scope_level == 0:
            new_var = GlobalVariable(self.irModule, self.type, ctx.Identifier().getText())
            new_var.linkage = 'internal'
            new_var.initializer = ir.Constant(self.type, self.visit(ctx.constExpression())['value'])
            self.symbolTable.addGlobal(ctx.Identifier().getText(), NameProperty(_type=self.type, value=new_var))
            # 只需要记录虚拟寄存器即可
        else:
            # 局部变量
            builder = self.irBuilder[-1]
            # 分配空间
            new_var = builder.alloca(self.type, name=ctx.Identifier().getText())
            # 存上初值
            builder.store(self.visit(ctx.constExpression())['value'], new_var)
            # 存入符号表
            self.symbolTable.addLocal(ctx.Identifier().getText(), NameProperty(_type=self.type, value=new_var))
##########################################################################################

    # Visit a parse tree produced by cpp14Parser#varDeclWithInit.
    def visitVarDeclWithInit(self, ctx: cpp14Parser.VarDeclWithInitContext):
        if self.symbolTable.current_scope_level != 0:
            builder = self.irBuilder[-1]
            address = builder.alloca(self.type, name=ctx.Identifier().getText())
            builder.store(self.visit(ctx.expression())['value'], address)
            self.symbolTable.addLocal(ctx.Identifier().getText(), NameProperty(_type=self.type, value=address))
            return

        raise BaseException("Incorrect initialization of global variables")

    # Visit a parse tree produced by cpp14Parser#variableDeclarator.
    def visitVariableDeclarator(self, ctx: cpp14Parser.VariableDeclaratorContext):
        self.type = self.visit(ctx.typeSpecifier())

        for declaration in ctx.variableDeclaration():
            self.visit(declaration)

    # Visit a parse tree produced by cpp14Parser#functionDecl.
    def visitFunctionDecl(self, ctx: cpp14Parser.FunctionDeclContext):
        parameter_list = []
        for param in ctx.functionParameter():
            parameter_list.append(self.visit(param))

        parameter_type_list = list(param['type'] for param in parameter_list)
        if "varargs" in parameter_type_list:
            if parameter_type_list.count("varargs") > 1:
                raise BaseException("too many varargs")
            if parameter_type_list[-1] != "varargs":
                raise BaseException("Wrong varargs position")
            parameter_type_list.pop()

        function_name = ctx.Identifier().getText()

        llvm_func_type = ir.FunctionType(
            self.visit(ctx.typeSpecifier()), parameter_type_list, var_arg="varargs" in parameter_type_list
        )
        llvm_func = ir.Function(self.irModule, llvm_func_type, name=function_name)
        self.symbolTable.addGlobal(function_name, NameProperty(_type=llvm_func_type, value=llvm_func))

    # Visit a parse tree produced by cpp14Parser#functionDef.
    def visitFunctionDef(self, ctx: cpp14Parser.FunctionDefContext):
        return_type = self.visit(ctx.getChild(0))
        parameter_list = []
        for param in ctx.functionParameter():
            parameter_list.append(self.visit(param))

        parameter_type_list = list(param['type'] for param in parameter_list)
        if "varargs" in parameter_type_list:
            raise BaseException("invalid varargs in function definition")

        function_name = ctx.getChild(1).getText()

        llvm_func_type = ir.FunctionType(return_type, parameter_type_list)
        llvm_func = ir.Function(self.irModule, llvm_func_type, name=function_name)

        self.symbolTable.addGlobal(function_name, NameProperty(_type=llvm_func_type, value=llvm_func))
        block = llvm_func.append_basic_block(name="__" + function_name)
        builder = ir.IRBuilder(block)
        self.irBuilder.append(builder)
        self.symbolTable.enterScope()

        for args_value, param in zip(llvm_func.args, parameter_list):
            address = builder.alloca(args_value.type, name=param['name'])
            builder.store(args_value, address)
            self.symbolTable.addLocal(param['name'], NameProperty(param['type'], address))

        builder = self.irBuilder[-1]
        if not builder.block.is_terminated:
            builder.ret_void()
        self.symbolTable.exitScope()

        expression = {'type': return_type, 'signed': True, 'value': self.visit(ctx.block())}
        return expression

    # Visit a parse tree produced by cpp14Parser#functionParameter.
    def visitFunctionParameter(self, ctx: cpp14Parser.FunctionParameterContext):
        expression = {}
        if ctx.DOTS() is not None:
            expression['type'] = 'varargs'
            expression['name'] = 'varargs'
        else:
            expression['type'] = self.visit(ctx.getChild(0))
            expression['name'] = ctx.Identifier().getText()
        return expression

    # Visit a parse tree produced by cpp14Parser#typeSpecifier.
    def visitTypeSpecifier(self, ctx: cpp14Parser.TypeSpecifierContext):
        return self.visit(ctx.getChild(0))

    # Visit a parse tree produced by cpp14Parser#pointerTypeSpecifier.
    def visitPointerTypeSpecifier(self, ctx: cpp14Parser.PointerTypeSpecifierContext):
        return ir.PointerType(self.visit(ctx.typeSpecifier()))

    # Visit a parse tree produced by cpp14Parser#integerTypeSpecifier.
    def visitIntegerTypeSpecifier(self, ctx: cpp14Parser.IntegerTypeSpecifierContext):
        text = ctx.getText()
        if text is 'short':
            return int16
        elif text is 'int':
            return int32
        elif text is 'long':
            return int32
        elif text is 'longlong':
            return int64

    # Visit a parse tree produced by cpp14Parser#realTypeSpecifier.
    def visitRealTypeSpecifier(self, ctx: cpp14Parser.RealTypeSpecifierContext):
        return double

    # Visit a parse tree produced by cpp14Parser#booleanTypeSpecifier.
    def visitBooleanTypeSpecifier(self, ctx: cpp14Parser.BooleanTypeSpecifierContext):
        return int1

    # Visit a parse tree produced by cpp14Parser#charTypeSpecifier.
    def visitCharTypeSpecifier(self, ctx: cpp14Parser.CharTypeSpecifierContext):
        return int8

    # Visit a parse tree produced by cpp14Parser#voidTypeSpecifier.
    def visitVoidTypeSpecifier(self, ctx: cpp14Parser.VoidTypeSpecifierContext):
        return void


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <input_filename>\n")
        exit(0)
    else:
        filename = sys.argv[1]
        outputFilename = filename.split(".")[0]+"ll"
        inputStream = FileStream(filename)

        lexer = cpp14Lexer(inputStream)
        stream = CommonTokenStream(lexer)

        parser = cpp14Parser(stream)
        tree = parser.translationUnit()

        newVisitor = NewCpp14Visitor()
        newVisitor.visit(tree)

        if outputFilename:
            with open(outputFilename, 'w') as f:
                f.write(str(newVisitor.irModule))
        exit(0)
