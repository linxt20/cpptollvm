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
    def visitIntegerLiteral(self, ctx:cpp14Parser.IntegerLiteralContext):
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
                            'type':return_type,
                            'signed':True, 
                            'value':ir.Constant(return_type,int(text_without_suffix))
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
    def visitStringLiteral(self, ctx:cpp14Parser.StringLiteralContext):  ## 这个搞不明白

        s = ast.literal_eval(ctx.getText()) + '\0'
        
        string_type = ArrayType(int8,len(s))
        string_address = ir.GlobalVariable(self.irModule,string_type,'__string_'+str(self.string_count))
        string_address.linkage='internal'
        string_address.initializer = ir.Constant(string_type,None)
        string_address.initializer = ir.Constant(string_type,bytearray(s,encoding='ascii'))
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
    def visitLeftExpression(self, ctx:cpp14Parser.LeftExpressionContext):
        text = ctx.getText()
        if(text[-1]!=']'):
            symbol = self.symbolTable.getProperty(text)
            left_expression = {
                                'type':symbol.get_type(),
                                'signed':symbol.get_signed(),
                                'address':symbol.get_value(),
                            }
            return left_expression
        
        else:
            text = ctx.getChild(0).getText()
            index = self.symbolTable.getProperty(text)
            value = index.get_value()
            if(isinstance(index.get_type(),ir.types.ArrayType)):
                builder = self.irBuilder[-1]
                left_expression = {
                                    'type':index.get_type().element,
                                    'signed':True,
                                    'address':builder.gep(value,[ir.Constant(int32,0),self.visit(ctx.getChild(2))['value']],inbounds=True)
                                }
                return left_expression
            else:
                raise BaseException("the array isn't defined")

    # Visit a parse tree produced by cpp14Parser#expression.
    def visitExpression(self, ctx:cpp14Parser.ExpressionContext):
        child_count=ctx.getChildCount()
        child0 = ctx.getChild(0)
        text = ctx.getText()
        textchild = ctx.getChild(0).getText()
        builder = self.irBuilder[-1]
        if(child_count == 1):
            grand_children = child0.getChildCount()
            if(grand_children):
                expression = self.visit(child0)
            else:
                symbol = self.symbolTable.getProperty(text)
                if( isinstance(symbol.get_type(),ir.ArrayType)):
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

        elif(child_count == 2):
            if(textchild in ['-','!','&']):
                builder = self.irBuilder[-1]
                result = self.visit(ctx.getChild(1))
                if(textchild == '-'):
                    type = result['type']
                    if result['type'] == double:
                        return_value = builder.fneg(result['value'])
                    else:
                        return_value = builder.neg(result['value'])
                elif(textchild == '!'):
                    type = int1
                    if result['type'] == double:
                        return_value = builder.fcmp_ordered('!=', result['value'], ir.Constant(int1,0))
                    else:
                        return_value = builder.icmp_signed('!=', result['value'], ir.Constant(int1,0))
                elif(textchild == '&'):
                    type = result['type'].as_pointer()
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
                    return_value = builder.sub(now_value,ir.Constant(lhs['type'],1))
                builder.store(return_value, lhs['address'])
                type = lhs['type']
            expression = {
                            'type': type,
                            'signed':True,
                            'value': return_value
                        }    
            return expression
        elif(child_count == 3 and textchild=='('):

            expression = self.visit(ctx.getChild(1))
            return expression
        
        elif(child_count > 3):

            index = self.symbolTable.getProperty(textchild)
            subscribe = self.visit(ctx.getChild(2))['value']
            if(isinstance(index.get_type(),ir.types.ArrayType)):
                builder = self.irBuilder[-1]
                Address = builder.gep(index.get_value(),[ir.Constant(int32,0),subscribe],inbounds=True)
                return_value = builder.load(Address)
                expression = {
                                'type':index.get_type().element,
                                'signed':True,
                                'value':return_value
                            }
                return expression
            else:
                raise BaseException("the array isn't defined")

        else:
            operation = ctx.getChild(1).getText()

            left = self.visit(child0)
            right = self.visit(ctx.getChild(2))
            if(operation in ['>','<','>=','<=','==','!=']):
                left,right = self.exprTypeConvert(left,right)
                if(left['type']==double):
                    return_value = builder.fcmp_ordered(operation,left['value'],right['value'])
                elif(left['type']==int32 or left['type'] == int64 or left['type'] == int8 or left['type']==int1):
                    if(left['signed']):
                        return_value = builder.icmp_signed(operation,left['value'],right['value'])
                    else:
                        return_value = builder.icmp_unsigned(operation, left['value'], right['value'])
                expression = {
                                'type': int1,
                                'signed': True,
                                'value': return_value
                            }          
                return expression

            elif(operation in ['+','-','*','/','%','<<','>>']):

                left,right = self.exprTypeConvert(left,right)
                if(operation == '+'):
                    if(left['type']==double):
                        return_value = builder.fadd(left['value'],right['value'])
                    else:
                        return_value = builder.add(left['value'],right['value'])
                elif(operation == '-'):
                    if(left['type']==double): 
                        return_value = builder.fsub(left['value'],right['value'])
                    else:
                        return_value = builder.sub(left['value'],right['value'])
                elif(operation == '*'):
                    if left['type']==double:
                        return_value = builder.fmul(left['value'],right['value'])
                    else:
                        return_value = builder.mul(left['value'],right['value'])
                elif(operation == '/'):
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

            elif(operation == '='):

                child_count=child0.getChildCount()

                right = self.assignTypeConvert(left,right) # 在这里需要强制类型转换
                builder.store(right['value'],left['address'])
                expression = {
                                'type':right['type'],   
                                'value': builder.load(left['address'])
                            }

            elif(operation in ['|','&','^']):

                left,right = self.exprTypeConvert(left,right)
                Signed = False
                if left['signed'] or right['signed']:
                    Signed = True
                if(operation == '|' ):
                    return_value = builder.or_(left['value'],right['value'])
                elif(operation == '&' ):
                    return_value = builder.and_(left['value'],right['value'])
                elif(operation == '^'):
                    return_value = builder.xor(left['value'],right['value'])
                expression = {
                                'type':left['type'],
                                'signed':Signed,
                                'value':return_value
                            }
            
            elif(operation in ['&&' ,'||' ] ):
                '''
                对应语法: expression AND|OR expression
                '''
                left = self.toBool(left)
                right = self.toBool(right)
                if(operation == '&&'):
                    return_value = builder.and_(left['value'],right['value'])
                elif(operation == '||' ):
                    return_value = builder.or_(left['value'],right['value'])
                expression = {
                                'type':int1,
                                'signed':True,
                                'value':return_value
                            }
            return expression

    # Visit a parse tree produced by cpp14Parser#block.
    def visitBlock(self, ctx: cpp14Parser.BlockContext):
        self.symbolTable.enterScope()
        super().visitBlock(ctx)
        self.symbolTable.exitScope()
        return

    # Visit a parse tree produced by cpp14Parser#functionCall.
    def visitFunctionCall(self, ctx:cpp14Parser.FunctionCallContext):
        builder = self.irBuilder[-1]
        property = self.symbolTable.getProperty(ctx.Identifier().getText())
        if(property.get_type().__class__.__name__ != ir.FunctionType.__name__):
            raise BaseException("not a function name")
        else:
            paramList = []
            for expression in ctx.expression():
                expression_value = self.visit(expression) 
                paramList.append(expression_value['value'])

            if(property.get_type().var_arg):
                vaild_paramList = paramList[:len(property.get_type().args)]
            else:
                vaild_paramList = paramList

            if(len(vaild_paramList) == len(property.get_type().args)):
                
                for real_param, param in zip(vaild_paramList,property.get_type().args):
                    if(param != real_param.type):
                        raise BaseException("wrong args type",real_param.type,param)
                        
                ret_value = builder.call(property.get_value(), paramList, name='', cconv=None, tail=False, fastmath=())
                ret_type = property.get_type().return_type
                FunctionCall = {
                                    "type" : ret_type,
                                    'value': ret_value
                                }
                return FunctionCall
            else:
                raise BaseException("wrong args number")

    # Visit a parse tree produced by cpp14Parser#ifStatement.
    def visitIfStatement(self, ctx:cpp14Parser.IfStatementContext):

        self.symbolTable.enterScope()
        builder = self.irBuilder[-1]
        true_block = builder.append_basic_block()

        if len(ctx.statement())==2:
            false_block = builder.append_basic_block()
            endblock = builder.append_basic_block()
            
            result = self.visit(ctx.getChild(2))
            condition = to_bool(result, self.irBuilder[-1])
            builder.cbranch(condition['value'], true_block, false_block)
            
            self.operatorif_else(self,true_block,ctx.getChild(4),endblock)
            self.operatorif_else(self,false_block,ctx.getChild(6),endblock)
            
            self.irBuilder.pop()
            self.irBuilder.append(ir.IRBuilder(endblock))
            
        else:
            end_block = builder.append_basic_block()
            
            result = self.visit(ctx.getChild(2))
            condition = to_bool(result, self.irBuilder[-1])
            builder.cbranch(condition['value'], true_block, end_block)
            
            self.operatorif_else(self,true_block,ctx.getChild(4),endblock)
            
            self.irBuilder.pop()
            self.irBuilder.append(ir.IRBuilder(endblock))

        self.symbolTable.exitScope()

    def operatorif_else(self,block,child,endblock):
        blockbuilder = ir.IRBuilder(block)
        self.irBuilder.pop()
        self.irBuilder.append(blockbuilder)
        self.visit(child)
        if(not self.irBuilder[-1].block.is_terminated):
            self.irBuilder[-1].branch(endblock)

    def intConvert(self,src,target):
        builder = self.irBuilder[-1] 
        if(target['type'].width < src['type'].width):
            return_value = builder.trunc(src['value'],target['type'])
        else:
            if(src['type'].width != 1 and src['signed']):
                return_value = builder.sext(src['value'],target['type'])
                
            else:
                return_value = builder.zext(src['value'],target['type'])
        
        temp = {
                'type':target['type'],
                'signed':src['signed'],
                'value':return_value
        }
        return temp
            
    def intToDouble(self,llvmNum):
        builder = self.irBuilder[-1]
        if(llvmNum['signed']):
            return_value = builder.sitofp(llvmNum['value'],double)
        else:
            return_value = builder.uitofp(llvmNum['value'],double)

        temp = {
            'type':double,
            'value':return_value
        }
        return temp

    
    def doubleToInt(self,llvmNum,target):
        builder = self.irBuilder[-1]
        if(llvmNum['signed']):
            return_value = builder.fptosi(llvmNum['value'],target['type'])
        else:
            return_value = builder.fptoui(llvmNum['value'],target['type'])
        temp = {
            'type':target['type'],
            'value':return_value
        }
        return temp
    

    def toBool(self,llvmNum):
        builder = self.irBuilder[-1]
        if llvmNum['type'] == double:
            return_value = builder.fcmp_ordered('!=', llvmNum['value'], ir.Constant(int1,0))
        else:
            return_value = builder.icmp_signed('!=', llvmNum['value'], ir.Constant(int1,0))
        temp = {
            'type':int1,
            'signed':True,
            'value':return_value
        }
        return temp

    def assignTypeConvert(self,left,right):
        isint_left = False
        isint_right = False

        if left['type'] ==int32 or left['type']== int64 or left['type'] == int16 or left['type'] == int8 or left['type'] == int1:
            isint_left = True
        if right['type']==int32 or right['type']== int64 or right['type'] == int16 or right['type'] == int8 or right['type'] == int1:
            isint_right = True

        if(left['type'] != right['type']):
            if(isint_left and isint_right):
                right = self.intConvert(right,left)
            elif(isint_left and isint_right==False):
                right = self.doubleToInt(right,left)
            elif(isint_left==False and isint_right):
                right = self.intToDouble(right)
            else:
                pass
        return right
    
    def exprTypeConvert(self,left,right):
        left_isint = self.isInt(left)
        right_isint = self.isInt(right)
        if(left['type']==right['type']):
            return left,right
        elif left_isint and right_isint:
            if left['type'].width < right['type'].width:
                left = self.intConvert(left,right)
            else:
                right = self.intConvert(right,left)
        elif left_isint and right['type']==double: 
            left = self.intToDouble(left)
        elif left['type']==double and right_isint:
            right = self.intToDouble(right)
        return left,right

####################################################################################

    # Visit a parse tree produced by cpp14Parser#caseStatement.
    def visitCaseStatement(self, ctx: cpp14Parser.CaseStatementContext):
        """
        caseStatement : CASE constExpression COLON statement;
        """
        self.symbolTable.enterScope()
        judge_block = self.switch_case_label[-1][0]
        statement_block = self.switch_case_label[-1][1]
        target_judge_block = self.switch_case_label[-1][2]
        target_statement_block = self.switch_case_label[-1][3]

        judge_builder = ir.IRBuilder(judge_block)

        left = self.switch_expression[-1]
        right = self.visit(ctx.getChild(1))

        left, right = expr_type_convert(left, right, self.irBuilder[-1])

        if left['type'] == double:
            return_value = judge_builder.fcmp_ordered('==', left['value'], right['value'])
        else:
            if left['signed']:
                return_value = judge_builder.icmp_signed('==', left['value'], right['value'])
            else:
                return_value = judge_builder.icmp_unsigned('==', left['value'], right['value'])

        judge_builder.cbranch(return_value, statement_block, target_judge_block)

        self.irBuilder.pop()
        self.irBuilder.append(ir.IRBuilder(statement_block))
        self.visit(ctx.getChild(3))
        if not self.irBuilder[-1].block.is_terminated:
            self.irBuilder[-1].branch(target_statement_block)

        self.symbolTable.exitScope()

        self.switch_case_label[-1].pop(0)
        self.switch_case_label[-1].pop(0)

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
        condition = to_bool(result, self.irBuilder[-1])
        self.irBuilder[-1].cbranch(condition['value'], while_statement_block, end_while_block)

        # while_statement_block
        self.irBuilder.pop()
        self.irBuilder.append(ir.IRBuilder(while_statement_block))
        # print("this block to break", self.blockToBreak[-1])
        self.visit(ctx.getChild(4))
        if not self.irBuilder[-1].block.is_terminated:
            self.irBuilder[-1].branch(expression_block)

        # end_while_block
        self.irBuilder.pop()
        self.irBuilder.append(ir.IRBuilder(end_while_block))

        self.blockToContinue.pop()
        self.blockToBreak.pop()

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
        condition = to_bool(result, self.irBuilder[-1])
        self.irBuilder[-1].cbranch(condition['value'], do_statement_block, end_while_block)

        # end_while_block
        self.irBuilder.pop()
        self.irBuilder.append(ir.IRBuilder(end_while_block))
        self.blockToContinue.pop()
        self.blockToBreak.pop()

    # Visit a parse tree produced by cpp14Parser#forStatement.
    def visitForStatement(self, ctx: cpp14Parser.ForStatementContext):
        builder = self.irBuilder[-1]
        # 判断三个expression是否存在
        child_count = ctx.getChildCount()
        flag1 = True
        flag2 = True
        flag3 = True
        expression_index = None

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
            condition = to_bool(result, self.irBuilder[-1])
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

    # Visit a parse tree produced by cpp14Parser#returnStatement.
    def visitReturnStatement(self, ctx: cpp14Parser.ReturnStatementContext):
        if ctx.expression() is None:
            self.irBuilder[-1].ret_void()
        else:
            self.irBuilder[-1].ret(self.visit(ctx.expression())['value'])

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

    # Visit a parse tree produced by cpp14Parser#normalArrDecl.
    def visitNormalArrDecl(self, ctx: cpp14Parser.NormalArrDeclContext):
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
            if parameter_type_list.child_count("varargs") > 1:
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
