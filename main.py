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
    def __init__(self, _name: str):
        super(cpp14Visitor, self).__init__()

        self.irModule = ir.Module()  # llvm生成模块
        self.irBuilder = []  # 待生成的llvm语句块，新生成的语句在末尾
        self.symbolTable = NameTable()  # 符号表
        
        self.switch_expression = []  # 用于存储switch表达式的结果，来与case匹配
        self.switch_case_label = []  # 用于存储switch表达式中label的值

        # break,continue语句跳转到的block
        self.block_to_break = []
        self.block_to_continue = []

        self.string_count = 0  # 全局字符串的数量

        # self.irModule.data_layout = "e-m:e-p270:32:32-p271:32:32-p272:64:64-i64:64-f80:128-n8:16:32:64-S128"
        self.irModule.triple = "x86_64-pc-linux-gnu"
        if _name.count("/") > 0:
            self.irModule.name = _name.split("/")[-1]
        elif _name.count("\\") > 0:
            self.irModule.name = _name.split("\\")[-1]
        else:
            self.irModule.name = _name

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
                            'signed': True,
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
    def visitStringLiteral(self, ctx: cpp14Parser.StringLiteralContext):  # 这个搞不明白

        s = ast.literal_eval(ctx.getText()) + '\0'
        
        string_type = ArrayType(int8, len(s))
        string_address = ir.GlobalVariable(self.irModule, string_type, '__string_'+str(self.string_count))
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
        text = ctx.getText()
        if text[-1] != ']':
            symbol = self.symbolTable.getProperty(text)
            left_expression = {
                                'type': symbol.get_type(),
                                'signed': symbol.get_signed(),
                                'address': symbol.get_value(),
                            }
            return left_expression
        
        else:
            text = ctx.getChild(0).getText()
            index = self.symbolTable.getProperty(text)
            value = index.get_value()
            if isinstance(index.get_type(), ir.types.ArrayType):
                builder = self.irBuilder[-1]
                left_expression = {
                                    'type': index.get_type().element,
                                    'signed': True,
                                    'address': builder.gep(
                                        value,
                                        [ir.Constant(int32, 0), self.visit(ctx.getChild(2))['value']],
                                        inbounds=True
                                    )
                                }
                return left_expression
            else:
                raise BaseException("the array isn't defined")

    # Visit a parse tree produced by cpp14Parser#expression.
    def visitExpression(self, ctx: cpp14Parser.ExpressionContext):
        child_count = ctx.getChildCount()
        child0 = ctx.getChild(0)
        text = ctx.getText()
        text_child = ctx.getChild(0).getText()
        builder = self.irBuilder[-1]
        if child_count == 1:
            grand_children = child0.getChildCount()
            if grand_children:
                expression = self.visit(child0)
            else:
                symbol = self.symbolTable.getProperty(text)
                if isinstance(symbol.get_type(), ir.ArrayType):
                    expression = {
                                    'type': symbol.get_type().element.as_pointer(),
                                    'value': builder.gep(
                                        symbol.get_value(),
                                        [ir.Constant(int32, 0), ir.Constant(int32, 0)],
                                        inbounds=True
                                    )
                                }
                else:
                    ret_value = builder.load(symbol.get_value())
                    expression = {
                                    'type': ret_value.type,
                                    'signed': symbol.get_signed(),
                                    'value': ret_value
                                }
            return expression

        elif child_count == 2:
            if text_child in ['-', '!', '&']:
                builder = self.irBuilder[-1]
                result = self.visit(ctx.getChild(1))
                if text_child == '-':
                    _type = result['type']
                    if result['type'] == double:
                        return_value = builder.fneg(result['value'])
                    else:
                        return_value = builder.neg(result['value'])
                elif text_child == '!':
                    _type = int1
                    if result['type'] == double:
                        return_value = builder.fcmp_ordered('!=', result['value'], ir.Constant(int1, 0))
                    else:
                        return_value = builder.icmp_signed('!=', result['value'], ir.Constant(int1, 0))
                else:
                    _type = result['type'].as_pointer()
                    return_value = result['address']
                
            else:
                # 减减或者加加
                builder = self.irBuilder[-1]
                lhs = self.visit(child0)
                # 先 load, address 就是地址
                now_value = builder.load(lhs['address'])
                # 再 + 1 / -1
                if ctx.getChild(1).getText() == '++':
                    return_value = builder.add(now_value, ir.Constant(lhs['type'], 1))
                else:
                    return_value = builder.sub(now_value, ir.Constant(lhs['type'], 1))
                builder.store(return_value, lhs['address'])
                _type = lhs['type']
            expression = {
                            'type': _type,
                            'signed': True,
                            'value': return_value
                        }    
            return expression
        elif child_count == 3 and text_child == '(':

            expression = self.visit(ctx.getChild(1))
            return expression
        
        elif child_count > 3:

            index = self.symbolTable.getProperty(text_child)
            subscribe = self.visit(ctx.getChild(2))['value']
            if isinstance(index.get_type(), ir.types.ArrayType):
                builder = self.irBuilder[-1]
                address = builder.gep(index.get_value(), [ir.Constant(int32, 0), subscribe], inbounds=True)
                return_value = builder.load(address)
                expression = {
                                'type': index.get_type().element,
                                'signed': True,
                                'value': return_value
                            }
                return expression
            else:
                raise BaseException("the array isn't defined")

        else:
            operation = ctx.getChild(1).getText()

            left = self.visit(child0)
            right = self.visit(ctx.getChild(2))
            if operation in ['>', '<', '>=', '<=', '==', '!=']:
                left, right = expr_type_convert(left, right, self.irBuilder[-1])
                if left['type'] == double:
                    return_value = builder.fcmp_ordered(operation, left['value'], right['value'])
                elif left['type'] in [int32, int64, int8, int1]:
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

            elif operation in ['+', '-', '*', '/', '%', '<<', '>>']:

                left, right = expr_type_convert(left, right, self.irBuilder[-1])
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

            elif operation == '=':
                right = assign_type_convert(left, right, self.irBuilder[-1])  # 在这里需要强制类型转换
                builder.store(right['value'], left['address'])
                expression = {
                                'type': right['type'],
                                'value': builder.load(left['address'])
                            }

            elif operation in ['|', '&', '^']:

                left, right = expr_type_convert(left, right, self.irBuilder[-1])
                signed = False
                if left['signed'] or right['signed']:
                    signed = True
                if operation == '|':
                    return_value = builder.or_(left['value'], right['value'])
                elif operation == '&':
                    return_value = builder.and_(left['value'], right['value'])
                else:
                    return_value = builder.xor(left['value'], right['value'])
                expression = {
                                'type': left['type'],
                                'signed': signed,
                                'value': return_value
                            }
            
            elif operation in ['&&', '||']:

                left = to_bool(left, self.irBuilder[-1])
                right = to_bool(right, self.irBuilder[-1])
                if operation == '&&':
                    return_value = builder.and_(left['value'], right['value'])
                else:
                    return_value = builder.or_(left['value'], right['value'])
                expression = {
                                'type': int1,
                                'signed': True,
                                'value': return_value
                            }
            return expression

    # Visit a parse tree produced by cpp14Parser#block.
    def visitBlock(self, ctx: cpp14Parser.BlockContext):
        self.symbolTable.enterScope()
        super().visitBlock(ctx)
        self.symbolTable.exitScope()
        return

    # Visit a parse tree produced by cpp14Parser#functionCall.
    def visitFunctionCall(self, ctx: cpp14Parser.FunctionCallContext):
        builder = self.irBuilder[-1]
        function_name = ctx.Identifier().getText()
        _property = self.symbolTable.getProperty(function_name)
        # print("_property.get_type().__class__.__name__",_property.get_type().__class__.__name__)
        if _property.get_type().__class__.__name__ == ir.FunctionType.__name__:
            
            param_list = []
            for expression in ctx.expression():
                expression_value = self.visit(expression) 
                param_list.append(expression_value['value'])
            # print("_property.get_type().var_arg",_property.get_type().var_arg)
            # print("paramList & argsList: ", param_list,_property.get_type().args)
            if _property.get_type().var_arg:
                valid_param_list = param_list[:len(_property.get_type().args)]
            else:
                valid_param_list = param_list
            # print("valid_param_list \n",valid_param_list)
            # print("_property.get_type() \n",_property.get_type())
            if len(valid_param_list) != len(_property.get_type().args):
                raise BaseException("wrong args number")
            for real_param, param in zip(valid_param_list, _property.get_type().args):
                if param != real_param.type:
                    raise BaseException("wrong args type", real_param.type, param)
                    
            ret_value = builder.call(
                _property.get_value(), param_list, name='', cconv=None, tail=False, fastmath=()
            )
            ret_type = _property.get_type().return_type
            function_call = {
                                "type": ret_type,
                                'value': ret_value
                            }
            return function_call
        else:    
            raise BaseException("not a function name")
            

    # Visit a parse tree produced by cpp14Parser#ifStatement.
    def visitIfStatement(self, ctx: cpp14Parser.IfStatementContext):

        self.symbolTable.enterScope()
        builder = self.irBuilder[-1]
        true_block = builder.append_basic_block()

        if len(ctx.statement()) == 2:
            false_block = builder.append_basic_block()
            end_block = builder.append_basic_block()
            
            result = self.visit(ctx.getChild(2))
            condition = to_bool(result, self.irBuilder[-1])
            builder.cbranch(condition['value'], true_block, false_block)
            
            self.operator_if_else(true_block, ctx.getChild(4), end_block)
            self.operator_if_else(false_block, ctx.getChild(6), end_block)
            
        else:
            end_block = builder.append_basic_block()
            
            result = self.visit(ctx.getChild(2))
            condition = to_bool(result, self.irBuilder[-1])
            builder.cbranch(condition['value'], true_block, end_block)
            
            self.operator_if_else(true_block, ctx.getChild(4), end_block)
            
        self.irBuilder.pop()
        self.irBuilder.append(ir.IRBuilder(end_block))

        self.symbolTable.exitScope()

    def operator_if_else(self, block, child, end_block):
        block_builder = ir.IRBuilder(block)
        self.irBuilder.pop()
        self.irBuilder.append(block_builder)
        self.visit(child)
        if not self.irBuilder[-1].block.is_terminated:
            self.irBuilder[-1].branch(end_block)

####################################################################################

    # Visit a parse tree produced by cpp14Parser#caseStatement.
    def visitCaseStatement(self, ctx: cpp14Parser.CaseStatementContext):
        self.symbolTable.enterScope()
        judge_block = self.switch_case_label[-1][0]
        judge_builder = ir.IRBuilder(judge_block)

        statement_block = self.switch_case_label[-1][1]
        target_judge_block = self.switch_case_label[-1][2]
        target_statement_block = self.switch_case_label[-1][3]

        left = self.switch_expression[-1]
        right = self.visit(ctx.getChild(1))
        left, right = expr_type_convert(left, right, self.irBuilder[-1])

        if (left['type'] != double) and left['signed']:
            return_value = judge_builder.icmp_signed('==', left['value'], right['value'])
        elif (left['type'] != double) and not (left['signed']):
            return_value = judge_builder.icmp_unsigned('==', left['value'], right['value'])
        else:
            return_value = judge_builder.fcmp_ordered('==', left['value'], right['value'])
        judge_builder.cbranch(return_value, statement_block, target_judge_block)

        self.irBuilder.pop()
        self.irBuilder.append(ir.IRBuilder(statement_block))
        self.visit(ctx.getChild(3))

        if not self.irBuilder[-1].block.is_terminated:
            self.irBuilder[-1].branch(target_statement_block)

        self.symbolTable.exitScope()
        self.switch_case_label[-1].pop()
        self.switch_case_label[-1].pop()

    # Visit a parse tree produced by cpp14Parser#switchStatement.
    def visitSwitchStatement(self, ctx: cpp14Parser.SwitchStatementContext):
        # return self.visitChildren(ctx)
        self.symbolTable.enterScope()
        builder = self.irBuilder[-1]
        case_num = ctx.getChildCount() - 6

        self.switch_expression.append(self.visit(ctx.getChild(2)))
        temp_array = []
        for i in range(case_num * 2 + 2):
            temp_array.append(builder.append_basic_block())
        self.switch_case_label.append(temp_array)
        self.block_to_break.append(temp_array[-1])

        builder.branch(temp_array[0])
        for i in range(case_num):
            self.visit(ctx.getChild(i + 5))

        # assert len(self.switch_case_label[-1]) == 2
        ir.IRBuilder(self.switch_case_label[-1][0]).branch(self.switch_case_label[-1][1])
        self.irBuilder.pop()
        self.irBuilder.append(ir.IRBuilder(self.switch_case_label[-1][1]))

        self.symbolTable.exitScope()
        self.block_to_break.pop()
        self.switch_case_label.pop()
        self.switch_expression.pop()

    # Visit a parse tree produced by cpp14Parser#whileStatement.
    def visitWhileStatement(self, ctx: cpp14Parser.WhileStatementContext):
        builder = self.irBuilder[-1]
        expression_block = builder.append_basic_block()
        while_statement_block = builder.append_basic_block()
        end_while_block = builder.append_basic_block()

        self.block_to_continue.append(expression_block)
        self.block_to_break.append(end_while_block)

        builder.branch(expression_block)
        self.irBuilder.pop()
        self.irBuilder.append(ir.IRBuilder(expression_block))
        result = self.visit(ctx.getChild(2))
        self.irBuilder[-1].cbranch(to_bool(result, self.irBuilder[-1])['value'], while_statement_block, end_while_block)

        self.irBuilder.pop()
        self.irBuilder.append(ir.IRBuilder(while_statement_block))
        self.visit(ctx.getChild(4))
        if not self.irBuilder[-1].block.is_terminated:
            self.irBuilder[-1].branch(expression_block)

        self.irBuilder.pop()
        self.irBuilder.append(ir.IRBuilder(end_while_block))
        self.block_to_break.pop()
        self.block_to_continue.pop()

    # Visit a parse tree produced by cpp14Parser#doWhileStatement.
    def visitDoWhileStatement(self, ctx: cpp14Parser.DoWhileStatementContext):
        builder = self.irBuilder[-1]
        do_statement_block = builder.append_basic_block()
        expression_block = builder.append_basic_block()
        end_while_block = builder.append_basic_block()

        self.block_to_continue.append(expression_block)
        self.block_to_break.append(end_while_block)

        self.irBuilder.pop()
        self.irBuilder.append(ir.IRBuilder(do_statement_block))
        self.visit(ctx.getChild(1))
        if not self.irBuilder[-1].block.is_terminated:
            self.irBuilder[-1].branch(expression_block)

        self.irBuilder[-1].branch(expression_block)
        self.irBuilder.pop()
        self.irBuilder.append(ir.IRBuilder(expression_block))
        result = self.visit(ctx.getChild(4))
        self.irBuilder[-1].cbranch(to_bool(result, self.irBuilder[-1])['value'], do_statement_block, end_while_block)

        self.irBuilder.pop()
        self.irBuilder.append(ir.IRBuilder(end_while_block))
        self.block_to_break.pop()
        self.block_to_continue.pop()

    # Visit a parse tree produced by cpp14Parser#forStatement.
    def visitForStatement(self, ctx: cpp14Parser.ForStatementContext):
        child_count = ctx.getChildCount()
        builder = self.irBuilder[-1]
        expression_index = None

        flags = [True, True, True, True]  # 三个表达式是否在, 第0个是占位符
        if ctx.getChild(2).getText() == ';':
            flags[1] = False
        for i in range(child_count - 1):
            text1 = ctx.getChild(i).getText()
            text2 = ctx.getChild(i + 1).getText()
            if text1 == ';' and text2 != ';':
                expression_index = i + 1
                break
            if text1 == text2:
                flags[2] = False
        if ctx.getChild(child_count - 3).getText() == ';':
            flags[3] = False

        if flags[1]:
            self.visit(ctx.getChild(2))

        judge_block = builder.append_basic_block()
        loop_block = builder.append_basic_block()
        for_expr3_block = builder.append_basic_block()
        end_loop_block = builder.append_basic_block()
        self.block_to_continue.append(for_expr3_block)
        self.block_to_break.append(end_loop_block)

        if flags[2]:
            self.irBuilder[-1].branch(judge_block)
            self.irBuilder.pop()
            self.irBuilder.append(ir.IRBuilder(judge_block))
            result = self.visit(ctx.getChild(expression_index))
            self.irBuilder[-1].cbranch(to_bool(result, self.irBuilder[-1])['value'], loop_block, end_loop_block)

        self.irBuilder.pop()
        self.irBuilder.append(ir.IRBuilder(loop_block))
        self.visit(ctx.getChild(child_count - 1))
        if not self.irBuilder[-1].block.is_terminated:
            self.irBuilder[-1].branch(for_expr3_block)

        self.irBuilder.pop()
        self.irBuilder.append(ir.IRBuilder(for_expr3_block))
        if flags[3]:
            self.visit(ctx.getChild(child_count - 3))
        if flags[2]:
            self.irBuilder[-1].branch(judge_block)
        else:
            self.irBuilder[-1].branch(loop_block)

        self.irBuilder.pop()
        self.irBuilder.append(ir.IRBuilder(end_loop_block))
        self.block_to_break.pop()
        self.block_to_continue.pop()

    # Visit a parse tree produced by cpp14Parser#returnStatement.
    def visitReturnStatement(self, ctx: cpp14Parser.ReturnStatementContext):
        if ctx.expression() is None:
            self.irBuilder[-1].ret_void()
        else:
            return_value = self.visit(ctx.expression())['value']
            self.irBuilder[-1].ret(return_value)
        return

    # Visit a parse tree produced by cpp14Parser#breakStatement.
    def visitBreakStatement(self, ctx: cpp14Parser.BreakStatementContext):
        if self.block_to_break:
            builder = self.irBuilder[-1]
            builder.branch(self.block_to_break[-1])
        else:
            raise BaseException("cannot break")        
        return

    # Visit a parse tree produced by cpp14Parser#continueStatement.
    def visitContinueStatement(self, ctx: cpp14Parser.ContinueStatementContext):
        if self.block_to_continue:
            builder = self.irBuilder[-1]
            builder.branch(self.block_to_continue[-1])
        else:
            raise BaseException("cannot continue")
        return

    # Visit a parse tree produced by cpp14Parser#normalArrDecl.
    def visitNormalArrDecl(self, ctx: cpp14Parser.NormalArrDeclContext):
        array_length = int(ctx.getChild(3).getText())
        array_type = self.visit(ctx.getChild(0))
        llvm_array_type = ir.ArrayType(array_type, array_length)
        array_name = ctx.getChild(1).getText()
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
        array_type = self.visit(ctx.charTypeSpecifier())
        llvm_array_type = ir.ArrayType(array_type, array_length)
        array_name = ctx.Identifier().getText()
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

    # def VarDecl(self, ctx):

    # Visit a parse tree produced by cpp14Parser#varDeclWithoutInit.
    def visitVarDeclWithoutInit(self, ctx: cpp14Parser.VarDeclWithoutInitContext):
        if self.symbolTable.current_scope_level != 0:
            builder = self.irBuilder[-1]
            new_var = builder.alloca(self.type, name=ctx.Identifier().getText())
            builder.store(ir.Constant(self.type, None), new_var)
            self.symbolTable.addLocal(ctx.Identifier().getText(), NameProperty(type=self.type, value=new_var))
        else:
            new_var = GlobalVariable(self.irModule, self.type, ctx.Identifier().getText())
            new_var.linkage = 'internal'
            new_var.initializer = ir.Constant(self.type, None)
            self.symbolTable.addGlobal(ctx.Identifier().getText(), NameProperty(type=self.type, value=new_var))

    # Visit a parse tree produced by cpp14Parser#varDeclWithConstInit.
    def visitVarDeclWithConstInit(self, ctx: cpp14Parser.VarDeclWithConstInitContext):
        if self.symbolTable.current_scope_level != 0:
            builder = self.irBuilder[-1]
            new_var = builder.alloca(self.type, name=ctx.Identifier().getText())
            builder.store(self.visit(ctx.constExpression())['value'], new_var)
            self.symbolTable.addLocal(ctx.Identifier().getText(), NameProperty(type=self.type, value=new_var))
        else:
            new_var = GlobalVariable(self.irModule, self.type, ctx.Identifier().getText())
            new_var.linkage = 'internal'
            new_var.initializer = ir.Constant(self.type, self.visit(ctx.constExpression())['value'])
            self.symbolTable.addGlobal(ctx.Identifier().getText(), NameProperty(type=self.type, value=new_var))

    # Visit a parse tree produced by cpp14Parser#varDeclWithInit.
    def visitVarDeclWithInit(self, ctx: cpp14Parser.VarDeclWithInitContext):
        if self.symbolTable.current_scope_level != 0:
            builder = self.irBuilder[-1]
            address = builder.alloca(self.type, name=ctx.Identifier().getText())
            builder.store(self.visit(ctx.expression())['value'], address)
            self.symbolTable.addLocal(ctx.Identifier().getText(), NameProperty(type=self.type, value=address))
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
        # print(ctx.functionParameter())
        for param in ctx.functionParameter():
            # print("test1",param)
            # print("test2",self.visit(param))
            parameter_list.append(self.visit(param))

        parameter_type_list = list(param['type'] for param in parameter_list)
        # print("111",parameter_type_list)
        is_var_arg = "varargs" in parameter_type_list
        if is_var_arg:
            if parameter_type_list.count("varargs") > 1:
                raise BaseException("too many varargs")
            if parameter_type_list[-1] != "varargs":
                raise BaseException("Wrong varargs position")
            parameter_type_list =  parameter_type_list[:-1]
        # print("222",parameter_type_list)
        function_name = ctx.Identifier().getText()

        llvm_func_type = ir.FunctionType(
            self.visit(ctx.typeSpecifier()), parameter_type_list, var_arg= is_var_arg
        )
        llvm_func = ir.Function(self.irModule, llvm_func_type, name=function_name)
        self.symbolTable.addGlobal(function_name, NameProperty(type=llvm_func_type, value=llvm_func))

    # Visit a parse tree produced by cpp14Parser#functionDef.
    def visitFunctionDef(self, ctx: cpp14Parser.FunctionDefContext):
        function_name = ctx.getChild(1).getText()
        return_type = self.visit(ctx.getChild(0))
        parameter_list = []
        for param in ctx.functionParameter():
            parameter_list.append(self.visit(param))
        parameter_list = tuple(parameter_list)
        parameter_type_list = tuple(param['type'] for param in parameter_list)
        # print(parameter_list)
        # print(parameter_type_list)
        if "varargs" in parameter_type_list:
            raise BaseException("invalid varargs in function definition")

        llvm_func_type = ir.FunctionType(return_type, parameter_type_list)
        llvm_func = ir.Function(self.irModule, llvm_func_type, name=function_name)

        self.symbolTable.addGlobal(function_name, NameProperty(type=llvm_func_type, value=llvm_func))
        block = llvm_func.append_basic_block(name="__" + function_name)
        builder = ir.IRBuilder(block)
        self.irBuilder.append(builder)
        self.symbolTable.enterScope()

        for args_value, param in zip(llvm_func.args, parameter_list):
            address = builder.alloca(args_value.type, name=param['name'])
            builder.store(args_value, address)
            self.symbolTable.addLocal(param['name'], NameProperty(param['type'], address))

        ValueToReturn=self.visit(ctx.block())

        builder = self.irBuilder[-1]
        if not builder.block.is_terminated:
            builder.ret_void()
        self.symbolTable.exitScope()

        expression = {'type': return_type, 'signed': True, 'value': ValueToReturn}
        return expression

    # Visit a parse tree produced by cpp14Parser#functionParameter.
    def visitFunctionParameter(self, ctx: cpp14Parser.FunctionParameterContext):
        expression = {}
        # print(ctx.DOTS())
        if ctx.DOTS() is not None:
            expression['type'] = 'varargs'
            expression['name'] = 'varargs'
        else:
            expression['type'] = self.visit(ctx.getChild(0))
            expression['name'] = ctx.Identifier().getText()
        # print(expression)
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
        if text == 'short':
            return int16
        elif text == 'int':
            return int32
        elif text == 'long':
            return int32
        elif text == 'longlong':
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
        outputFilename = filename.split(".")[0]+".ll"
        inputStream = FileStream(filename)
        print(inputStream)
        lexer = cpp14Lexer(inputStream)
        stream = CommonTokenStream(lexer)

        parser = cpp14Parser(stream)
        tree = parser.translationUnit()

        newVisitor = NewCpp14Visitor(filename)
        newVisitor.visit(tree)

        if outputFilename:
            with open(outputFilename, 'w') as f:
                f.write(str(newVisitor.irModule))
        exit(0)
