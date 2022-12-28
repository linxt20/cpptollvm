from antlr4 import *
import sys, os
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

        self.Module = ir.Module() # llvm生成模块        
        self.Builders=[]  # 待生成的llvm语句块，新生成的语句在末尾
        self.symbolTable = NameTable() # 符号表
        
        self.Switchexpression = [] # 用于存储switch表达式的结果，来与case匹配
        self.Switchcaselabel = [] # 用于存储switch表达式中label的值

        # break,continue语句跳转到的block
        self.blockToBreak=[]
        self.blockToContinue=[]

        self.string_count = 0 # 全局字符串的数量

        self.Module.triple="x86_64-pc-linux"

        self.type = None

    def visitLiterals(self, ctx:cpp14Parser.LiteralsContext):
        Literals = self.visit(ctx.getChild(0))
        return Literals

    # Visit a parse tree produced by cpp14Parser#floatingLiteral.
    def visitFloatingLiteral(self, ctx:cpp14Parser.FloatingLiteralContext):
        FloatingLiteral = {
                            'type':double,
                            'value':ir.Constant(double,float(ctx.getText()))
                          }
        return FloatingLiteral

    # Visit a parse tree produced by cpp14Parser#integerLiteral.
    def visitIntegerLiteral(self, ctx:cpp14Parser.IntegerLiteralContext):
        text = ctx.getText()
        if(text[-2:] == 'll' or text[-2:] == 'LL'):
            ReturnType = int64
            textwithoutsuffix = text[:-2]
        else:
            ReturnType = int32
            if(text[-1]=='l' or text[-2:-1] == 'L'):                
                textwithoutsuffix = text[:-1]
            else:
                textwithoutsuffix = text
        
        IntegerLiteral = {
                            'type':ReturnType,
                            'signed':True, 
                            'value':ir.Constant(ReturnType,int(textwithoutsuffix))
                        }
        return IntegerLiteral


    # Visit a parse tree produced by cpp14Parser#characterLiteral.
    def visitCharacterLiteral(self, ctx:cpp14Parser.CharacterLiteralContext):
        CharacterLiteral = {
                                'type':int8,
                                'value':ir.Constant(int8,ord(ctx.getText()[1]))
                            }
        return CharacterLiteral


    # Visit a parse tree produced by cpp14Parser#stringLiteral.
    def visitStringLiteral(self, ctx:cpp14Parser.StringLiteralContext):  ## 这个搞不明白

        s = ast.literal_eval(ctx.getText()) + '\0'
        
        string_type = ArrayType(int8,len(s))
        string_address = ir.GlobalVariable(self.Module,string_type,'__string_'+str(self.string_count))
        string_address.linkage='internal'
        string_address.initializer = ir.Constant(string_type,None)
        string_address.initializer = ir.Constant(string_type,bytearray(s,encoding='ascii'))
        self.string_count += 1
        if(self.symbolTable.current_scope_level != 0):
            # a local variable
            Builder = self.Builders[-1]
            string_address = Builder.gep(string_address, [ir.Constant(int32,0),ir.Constant(int32,0)], inbounds=True)
        StringLiteral = {
                            'type' : string_type,
                            'value' : string_address
                        }     

        return StringLiteral


    # Visit a parse tree produced by cpp14Parser#constExpression.
    def visitConstExpression(self, ctx:cpp14Parser.ConstExpressionContext):
        return self.visit(ctx.literals())


    # Visit a parse tree produced by cpp14Parser#leftExpression.
    def visitLeftExpression(self, ctx:cpp14Parser.LeftExpressionContext):
        text = ctx.getText()
        if(text[-1]!=']'):
            symbol = self.symbolTable.getProperty(text)
            LeftExpression = {
                                'type':symbol.get_type(),
                                'signed':symbol.get_signed(),
                                'address':symbol.get_value(),
                            }
            return LeftExpression
        
        else:
            text = ctx.getChild(0).getText()
            index = self.symbolTable.getProperty(text)
            value = index.get_value()
            if(isinstance(index.get_type(),ir.types.ArrayType)):
                Builder = self.Builders[-1]
                LeftExpression = {
                                    'type':index.get_type().element,
                                    'signed':True,
                                    'address':Builder.gep(value,[ir.Constant(int32,0),self.visit(ctx.getChild(2))['value']],inbounds=True)
                                }
                return LeftExpression
            else:
                raise BaseException("the array isn't defined")
            
        


    # Visit a parse tree produced by cpp14Parser#expression.
    def visitExpression(self, ctx:cpp14Parser.ExpressionContext):
        count=ctx.getChildCount()
        child0 = ctx.getChild(0)
        text = ctx.getText()
        textchild = ctx.getChild(0).getText()
        Builder = self.Builders[-1]
        if(count == 1):
            grandChildren = child0.getChildCount()
            if(grandChildren):
                Expression = self.visit(child0)
            else:
                symbol = self.symbolTable.getProperty(text)
                if( isinstance(symbol.get_type(),ir.ArrayType)):
                    Expression = {
                                    'type': symbol.get_type().element.as_pointer(),
                                    'value': Builder.gep(symbol.get_value(),[ir.Constant(int32,0),ir.Constant(int32,0)],inbounds=True)
                                }
                else:
                    ret_value = Builder.load(symbol.get_value())
                    Expression = {
                                    'type':ret_value.type,
                                    'signed':symbol.get_signed(),
                                    'value':ret_value
                                }
            return Expression

        elif(count == 2):
            if(textchild in ['-','!','&']):
                Builder = self.Builders[-1]
                result = self.visit(ctx.getChild(1))
                if(textchild == '-'):
                    type = result['type']
                    if result['type'] == double:
                        ValueToReturn = Builder.fneg(result['value'])
                    else:
                        ValueToReturn = Builder.neg(result['value'])
                elif(textchild == '!'):
                    type = int1
                    if result['type'] == double:
                        ValueToReturn = Builder.fcmp_ordered('!=', result['value'], ir.Constant(int1,0))
                    else:
                        ValueToReturn = Builder.icmp_signed('!=', result['value'], ir.Constant(int1,0))
                elif(textchild == '&'):
                    type = result['type'].as_pointer()
                    ValueToReturn = result['address']
                
            else:
                # 减减或者加加
                Builder = self.Builders[-1]
                lhs = self.visit(child0)
                # 先 load, address 就是地址
                now_value = Builder.load(lhs['address'])
                # 再 + 1 / -1
                if(ctx.getChild(1).getText() == '++'):
                    ValueToReturn = Builder.add(now_value,ir.Constant(lhs['type'],1))
                else:
                    ValueToReturn = Builder.sub(now_value,ir.Constant(lhs['type'],1))
                Builder.store(ValueToReturn, lhs['address'])
                type = lhs['type']
            Expression = {
                            'type': type,
                            'signed':True,
                            'value': ValueToReturn
                        }    
            return Expression
        elif(count == 3 and textchild=='('):

            Expression = self.visit(ctx.getChild(1))
            return Expression
        
        elif(count > 3):

            index = self.symbolTable.getProperty(textchild)
            subscribe = self.visit(ctx.getChild(2))['value']
            if(isinstance(index.get_type(),ir.types.ArrayType)):
                Builder = self.Builders[-1]
                Address = Builder.gep(index.get_value(),[ir.Constant(int32,0),subscribe],inbounds=True)
                ValueToReturn = Builder.load(Address)
                Expression = {
                                'type':index.get_type().element,
                                'signed':True,
                                'value':ValueToReturn
                            }
                return Expression
            else:
                raise BaseException("the array isn't defined")

        else:
            Operation = ctx.getChild(1).getText()

            left = self.visit(child0)
            right = self.visit(ctx.getChild(2))
            if(Operation in ['>','<','>=','<=','==','!=']):
                left,right = self.exprTypeConvert(left,right)
                if(left['type']==double):
                    valueToReturn = Builder.fcmp_ordered(Operation,left['value'],right['value'])
                elif(left['type']==int32 or left['type'] == int64 or left['type'] == int8 or left['type']==int1):
                    if(left['signed']):
                        valueToReturn = Builder.icmp_signed(Operation,left['value'],right['value'])
                    else:
                        valueToReturn = Builder.icmp_unsigned(Operation,left['value'],right['value'])     
                Expression =  {
                                'type':int1,
                                'signed':True,
                                'value':valueToReturn
                            }          
                return Expression

            elif(Operation in ['+','-','*','/','%','<<','>>']):

                left,right = self.exprTypeConvert(left,right)
                if(Operation == '+'):
                    if(left['type']==double):
                        valueToReturn = Builder.fadd(left['value'],right['value'])
                    else:
                        valueToReturn = Builder.add(left['value'],right['value'])
                elif(Operation == '-'):
                    if(left['type']==double): 
                        valueToReturn = Builder.fsub(left['value'],right['value'])
                    else:
                        valueToReturn = Builder.sub(left['value'],right['value'])
                elif(Operation == '*'):
                    if left['type']==double:
                        valueToReturn = Builder.fmul(left['value'],right['value'])
                    else:
                        valueToReturn = Builder.mul(left['value'],right['value'])
                elif(Operation == '/'):
                    if left['type'] == double:
                        valueToReturn = Builder.fdiv(left['value'],right['value'])
                    else:
                        valueToReturn = Builder.sdiv(left['value'],right['value'])
                elif(Operation == '%'):
                    if left['type']==double:
                        valueToReturn = Builder.srem(left['value'],right['value'])
                    else:
                        valueToReturn = Builder.frem(left['value'],right['value'])
                elif(Operation == '<<'):
                    valueToReturn = Builder.shl(left['value'],right['value'])
                elif(Operation == '>>'):
                    valueToReturn = Builder.lshr(left['value'],right['value'])
                Expression = {
                                'type':right['type'],
                                'signed':True,
                                'value':valueToReturn
                            }

            elif(Operation == '='):

                count=child0.getChildCount()

                right = self.assignTypeConvert(left,right) # 在这里需要强制类型转换
                Builder.store(right['value'],left['address'])
                Expression = {
                                'type':right['type'],   
                                'value': Builder.load(left['address'])
                            }

            elif(Operation in ['|','&','^']):

                left,right = self.exprTypeConvert(left,right)
                Signed = False
                if left['signed'] or right['signed']:
                    Signed = True
                if(Operation == '|' ):
                    ValueToReturn = Builder.or_(left['value'],right['value'])
                elif(Operation == '&' ):
                    ValueToReturn = Builder.and_(left['value'],right['value'])
                elif(Operation == '^'):
                    ValueToReturn = Builder.xor(left['value'],right['value'])
                Expression = {
                                'type':left['type'],
                                'signed':Signed,
                                'value':ValueToReturn
                            }
            
            elif(Operation in ['&&' ,'||' ] ):
                '''
                对应语法: expression AND|OR expression
                '''
                left = self.toBool(left)
                right = self.toBool(right)
                if(Operation == '&&'):
                    ValueToReturn = Builder.and_(left['value'],right['value'])
                elif(Operation == '||' ):
                    ValueToReturn = Builder.or_(left['value'],right['value'])
                Expression = {
                                'type':int1,
                                'signed':True,
                                'value':ValueToReturn
                            }
            return Expression

    # Visit a parse tree produced by cpp14Parser#block.
    def visitBlock(self, ctx:cpp14Parser.BlockContext):
        self.symbolTable.enterScope()
        super().visitBlock(ctx)
        self.symbolTable.exitScope()
        return

    # Visit a parse tree produced by cpp14Parser#functionCall.
    def visitFunctionCall(self, ctx:cpp14Parser.FunctionCallContext):
        Builder = self.Builders[-1]
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
                        
                ret_value = Builder.call(property.get_value(), paramList, name='', cconv=None, tail=False, fastmath=())
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
        Builder = self.Builders[-1]
        trueblock = Builder.append_basic_block()

        if len(ctx.statement())==2:
            falseblock = Builder.append_basic_block()
            endblock = Builder.append_basic_block()
            
            result = self.visit(ctx.getChild(2))
            condition = self.toBool(result)
            Builder.cbranch(condition['value'], trueblock, falseblock)
            
            self.operatorif_else(self,trueblock,ctx.getChild(4),endblock)
            self.operatorif_else(self,falseblock,ctx.getChild(6),endblock)
            
            self.Builders.pop()
            self.Builders.append(ir.IRBuilder(endblock))
            
        else:
            endblock = Builder.append_basic_block()
            
            result = self.visit(ctx.getChild(2))
            condition = self.toBool(result)
            Builder.cbranch(condition['value'], trueblock, endblock)
            
            self.operatorif_else(self,trueblock,ctx.getChild(4),endblock)
            
            self.Builders.pop()
            self.Builders.append(ir.IRBuilder(endblock))

        self.symbolTable.exitScope()
        return

    def operatorif_else(self,block,child,endblock):
        blockbuilder = ir.IRBuilder(block)
        self.Builders.pop()
        self.Builders.append(blockbuilder)
        self.visit(child)
        if(not self.Builders[-1].block.is_terminated):
            self.Builders[-1].branch(endblock)

    def intConvert(self,src,target):
        Builder = self.Builders[-1] 
        if(target['type'].width < src['type'].width):
            ValueToReturn = Builder.trunc(src['value'],target['type'])
        else:
            if(src['type'].width != 1 and src['signed']):
                ValueToReturn = Builder.sext(src['value'],target['type'])
                
            else:
                ValueToReturn = Builder.zext(src['value'],target['type'])
        
        temp = {
                'type':target['type'],
                'signed':src['signed'],
                'value':ValueToReturn
        }
        return temp
            
    def intToDouble(self,llvmNum):
        Builder = self.Builders[-1]
        if(llvmNum['signed']):
            ValueToReturn = Builder.sitofp(llvmNum['value'],double)
        else:
            ValueToReturn = Builder.uitofp(llvmNum['value'],double)

        temp = {
            'type':double,
            'value':ValueToReturn
        }
        return temp

    
    def doubleToInt(self,llvmNum,target):
        Builder = self.Builders[-1]
        if(llvmNum['signed']):
            ValueToReturn = Builder.fptosi(llvmNum['value'],target['type'])
        else:
            ValueToReturn = Builder.fptoui(llvmNum['value'],target['type'])
        temp = {
            'type':target['type'],
            'value':ValueToReturn
        }
        return temp
    

    def toBool(self,llvmNum):
        Builder = self.Builders[-1]
        if llvmNum['type'] == double:
            ValueToReturn = Builder.fcmp_ordered('!=', llvmNum['value'], ir.Constant(int1,0))
        else:
            ValueToReturn = Builder.icmp_signed('!=', llvmNum['value'], ir.Constant(int1,0))
        temp = {
            'type':int1,
            'signed':True,
            'value':ValueToReturn
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
    def visitCaseStatement(self, ctx:cpp14Parser.CaseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp14Parser#switchStatement.
    def visitSwitchStatement(self, ctx:cpp14Parser.SwitchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp14Parser#whileStatement.
    def visitWhileStatement(self, ctx:cpp14Parser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp14Parser#doWhileStatement.
    def visitDoWhileStatement(self, ctx:cpp14Parser.DoWhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp14Parser#forStatement.
    def visitForStatement(self, ctx:cpp14Parser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp14Parser#returnStatement.
    def visitReturnStatement(self, ctx:cpp14Parser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp14Parser#breakStatement.
    def visitBreakStatement(self, ctx:cpp14Parser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp14Parser#continueStatement.
    def visitContinueStatement(self, ctx:cpp14Parser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp14Parser#normalArrDecl.
    def visitNormalArrDecl(self, ctx:cpp14Parser.NormalArrDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp14Parser#stringDecl.
    def visitStringDecl(self, ctx:cpp14Parser.StringDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp14Parser#varDeclWithoutInit.
    def visitVarDeclWithoutInit(self, ctx:cpp14Parser.VarDeclWithoutInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp14Parser#varDeclWithConstInit.
    def visitVarDeclWithConstInit(self, ctx:cpp14Parser.VarDeclWithConstInitContext):
        return self.visitChildren(ctx)

    # Visit a parse tree produced by cpp14Parser#varDeclWithInit.
    def visitVarDeclWithInit(self, ctx: cpp14Parser.VarDeclWithInitContext):
        if self.symbolTable.current_scope_level != 0:
            builder = self.Builders[-1]
            new_var_address = builder.alloca(self.type, name=ctx.Identifier().getText())
            builder.store(self.visit(ctx.expression())['value'], new_var_address)
            self.symbolTable.addLocal(ctx.Identifier().getText(), NameProperty(type=self.type, value=new_var_address))
            return

        raise Exception("Incorrect initialization of global variables")

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
        llvm_func = ir.Function(self.Module, llvm_func_type, name=function_name)
        self.symbolTable.addGlobal(function_name, NameProperty(type=llvm_func_type, value=llvm_func))

    # Visit a parse tree produced by cpp14Parser#functionDef.
    def visitFunctionDef(self, ctx: cpp14Parser.FunctionDefContext):
        return_type = self.visit(ctx.getChild(0))
        parameter_list = []
        for param in ctx.functionParameter():
            parameter_list.append(self.visit(param))

        parameter_type_list = list(param['type'] for param in parameter_list)
        if "varargs" in parameter_type_list:
            raise BaseException("varargs not allowed in function definition")

        function_name = ctx.getChild(1).getText()

        llvm_func_type = ir.FunctionType(return_type, parameter_type_list)
        llvm_func = ir.Function(self.Module, llvm_func_type, name=function_name)

        self.symbolTable.addGlobal(function_name, NameProperty(type=llvm_func_type, value=llvm_func))
        block = llvm_func.append_basic_block(name="__" + function_name)
        builder = ir.IRBuilder(block)
        self.Builders.append(builder)
        self.symbolTable.enterScope()

        for args_value, param in zip(llvm_func.args, parameter_list):
            address = builder.alloca(args_value.type, name=param['name'])
            builder.store(args_value, address)
            self.symbolTable.addLocal(param['name'], NameProperty(param['type'], address))

        if not self.Builders[-1].block.is_terminated:
            self.Builders[-1].ret_void()
        self.symbolTable.exitScope()

        return {'type': return_type, 'signed': True, 'value': self.visit(ctx.block())}

    # Visit a parse tree produced by cpp14Parser#functionParameter.
    def visitFunctionParameter(self, ctx: cpp14Parser.FunctionParameterContext):
        if ctx.DOTS() is not None:
            return {"type": "varargs", "name": "varargs"}
        else:
            return {"type": self.visit(ctx.getChild(0)), "name": ctx.Identifier().getText()}

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
