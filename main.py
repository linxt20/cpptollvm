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
        Signed = True                                                           ## 考虑需不需要
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
                            'signed':Signed,                                    ## 和上面一起
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
    def visitStringLiteral(self, ctx:cpp14Parser.StringLiteralContext): 

        ## 一个不大确定的操作，可以在这里用全局变量，将识别到的字符串归于其中
        s = ast.literal_eval(ctx.getText()) + '\0'
        
        string_type = ArrayType(int8,len(s))
        string_address = ir.GlobalVariable(self.Module,string_type,'__string_'+str(self.string_count))
        string_address.linkage='internal'
        string_address.initializer=ir.Constant(string_type,None)
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
        if(ctx.getText()[-1]==']'):
            
            '''
            对应语法: leftExpression:Identifier (LSQUARE expression RSQUARE)
            '''
            index = self.symbolTable.getProperty(ctx.getChild(0).getText())
            subscribe = self.visit(ctx.getChild(2))['value']
            if(isinstance(index.get_type(),ir.types.ArrayType)):
                Builder = self.Builders[-1]
                Address = Builder.gep(index.get_value(),[ir.Constant(int32,0),subscribe],inbounds=True)
                ValueToReturn = Builder.load(Address)
                print("call arrayItem",ValueToReturn)
                LeftExpression = {
                                    'type':index.get_type().element,
                                    'signed':True,
                                    'address':Address
                                }
                return LeftExpression
            else:
                raise BaseException("the array isn't defined")
            
        else:
            '''
            对应语法: leftExpression:Identifier
            '''
            symbol = self.symbolTable.getProperty(ctx.getText())
            LeftExpression = {
                                'type':symbol.get_type(),
                                'signed':symbol.get_signed(),
                                'address':symbol.get_value(),
                            }
            return LeftExpression


    # Visit a parse tree produced by cpp14Parser#expression.
    def visitExpression(self, ctx:cpp14Parser.ExpressionContext):
        ChildCount=ctx.getChildCount()
        Builder = self.Builders[-1]
        if(ChildCount == 1):
            grandChildren = ctx.getChild(0).getChildCount()
            if(grandChildren):
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
                if( isinstance(symbol.get_type(),ir.ArrayType)):
                    Expression = {
                                    'type': symbol.get_type().element.as_pointer(),
                                    'value': Builder.gep(symbol.get_value(),[ir.Constant(int32,0),ir.Constant(int32,0)],inbounds=True)
                                }
                    return Expression
                else:
                    ret_value = Builder.load(symbol.get_value())
                    Expression = {
                                    'type':ret_value.type,
                                    'signed':symbol.get_signed(),
                                    'value':ret_value
                                }
                    return Expression

        elif(ChildCount == 2):
            '''
            对应语法: expression: NOT expression | SUB expression
            对应语法: leftexpression MINUS_MINUS | leftexpression PLUS_PLUS
            '''  
            if(ctx.getChild(0).getText() == '-' or ctx.getChild(0).getText() == '!' or ctx.getChild(0).getText() == '&'):
                Builder = self.Builders[-1]
                result = self.visit(ctx.getChild(1))
                if(ctx.getChild(0).getText() == '!'):
                    if result['type'] == double:
                        ValueToReturn = Builder.fcmp_ordered('!=', result['value'], ir.Constant(int1,0))
                    else:
                        ValueToReturn = Builder.icmp_signed('!=', result['value'], ir.Constant(int1,0))
                    Expression = {
                                    'type':int1,
                                    'signed':True,
                                    'value':ValueToReturn
                                }
                    return Expression
                elif(ctx.getChild(0).getText() == '-'):
                    if result['type'] == double:
                        ValueToReturn = Builder.fneg(result['value'])
                    else:
                        ValueToReturn = Builder.neg(result['value'])
                    Expression = {
                                    'type':result['type'],
                                    'signed':True,
                                    'value':ValueToReturn
                                }
                    return Expression
                elif(ctx.getChild(0).getText() == '&'):
                    Expression = {
                                    'type': result['type'].as_pointer(),
                                    'signed' : True,
                                    'value' : result['address']
                                }
                    return Expression
            else:
                # 减减或者加加
                Builder = self.Builders[-1]
                lhs = self.visit(ctx.getChild(0))
                # 先 load, address 就是地址
                now_value = Builder.load(lhs['address'])
                # 再 + 1 / -1
                if(ctx.getChild(1).getText() == '++'):
                    ValueToReturn = Builder.add(now_value,ir.Constant(lhs['type'],1))
                else:
                    ValueToReturn = Builder.sub(now_value,ir.Constant(lhs['type'],1))
                # 存储
                Builder.store(ValueToReturn, lhs['address'])
                Expression = {
                                'type':lhs['type'],
                                'signed':True,
                                'value': ValueToReturn
                            }    
                return Expression
        elif(ChildCount > 3):
            '''
            对应语法: expression: Identifier '[' expression ']'
            '''
            index = self.symbolTable.getProperty(ctx.getChild(0).getText())
            subscribe = self.visit(ctx.getChild(2))['value']
            if(isinstance(index.get_type(),ir.types.ArrayType)):
                Builder = self.Builders[-1]
                Address = Builder.gep(index.get_value(),[ir.Constant(int32,0),subscribe],inbounds=True)
                ValueToReturn = Builder.load(Address)
                print("call arrayItem",ValueToReturn)
                Expression = {
                                'type':index.get_type().element,
                                'signed':True,
                                'value':ValueToReturn
                            }
                return Expression
            else:
                raise BaseException("the array isn't defined")

        elif(ChildCount == 3 and ctx.getChild(0).getText()=='('):
            '''
            对应语法: expression: '(' expression ')'
            '''
            result = self.visit(ctx.getChild(1))
            return result

        else:
            Operation = ctx.getChild(1).getText()
            # print(f"Operation:{Operation},child0:{ctx.getChild(0).getText()},child2:{ctx.getChild(2).getText()}")

            left = self.visit(ctx.getChild(0))
            right = self.visit(ctx.getChild(2))
            if(self.isExprJudge(Operation)):
                '''
                对应语法:  expression: expression '==' | '!=' | '<' | '<=' | '>' | '>=' expr
                '''
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

            elif(Operation == '+' or Operation == '-' or Operation == '*' or Operation == '/' or Operation == '%' or Operation == '<<' or Operation == '>>'):
                '''
                对应语法: expression: expression '+'|'-'|'*'|'/'|'%' expression
                '''
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
                return Expression

            elif(Operation == '='):
                '''
                对应语法:  expression: leftExpression '=' expression
                '''
                # result = self.visit(ctx.expression())
                ChildCount=ctx.getChild(0).getChildCount()
                print(left," is an varible")

                right = self.assignTypeConvert(left,right) # 强制类型转换
                Builder.store(right['value'],left['address'])
                Expression = {
                                'type':right['type'],   
                                'value': Builder.load(left['address'])
                            }
                return Expression

            elif(Operation == '|' or Operation == 'bitor' or Operation == '&' or Operation == 'bitand' or Operation == '^' or Operation == 'xor'):
                '''
                对应语法:  expression: expression BITOR|BITAND|XOR expression
                '''
                left,right = self.exprTypeConvert(left,right)
                Signed = False
                if left['signed'] or right['signed']:
                    Signed = True
                if(Operation == '|' or Operation == 'bitor'):
                    ValueToReturn = Builder.or_(left['value'],right['value'])
                elif(Operation == '&' or Operation == 'bitand' ):
                    ValueToReturn = Builder.and_(left['value'],right['value'])
                elif(Operation == '^' or Operation == 'xor'):
                    ValueToReturn = Builder.xor(left['value'],right['value'])
                Expression = {
                                'type':left['type'],
                                'signed':Signed,
                                'value':ValueToReturn
                            }
                return Expression
            
            elif(Operation == '&&' or Operation == 'and' or Operation == '||' or Operation == 'or'):
                '''
                对应语法: expression AND|OR expression
                '''
                left = self.toBool(left)
                right = self.toBool(right)
                if(Operation == '&&' or Operation == 'and'):
                    ValueToReturn = Builder.and_(left['value'],right['value'])
                elif(Operation == '||' or Operation == 'or'):
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
        '''
        对应语法: functionCall : Identifier LPAREN (expression (COMMA expression)*)? RPAREN;
        '''
        Builder = self.Builders[-1]
        functionName = ctx.Identifier().getText()
        property = self.symbolTable.getProperty(functionName)
        if(property.get_type().__class__.__name__ == ir.FunctionType.__name__):
            # 参数列表
            paramList = []
            for expression in ctx.expression():
                expression_value = self.visit(expression) 
                paramList.append(expression_value['value'])
            # 检查合法性
            # print("paramList & argsList: ", paramList,property.get_type().args)
            if(property.get_type().var_arg):
                # 只和vararg之前的比较
                vaild_paramList = paramList[:len(property.get_type().args)]
            else:
                vaild_paramList = paramList

            if(len(vaild_paramList) != len(property.get_type().args)):
                raise BaseException("wrong args number")
            for real_param, param in zip(vaild_paramList,property.get_type().args):
                if(param != real_param.type):
                    raise BaseException("wrong args type",real_param.type,param)
            # 函数调用
            ret_value = Builder.call(property.get_value(), paramList, name='', cconv=None, tail=False, fastmath=())
            ret_type = property.get_type().return_type
            return {
                "type" : ret_type,
                'value': ret_value
            }
        else:
            raise BaseException("not a function name")


    # Visit a parse tree produced by cpp14Parser#ifStatement.
    def visitIfStatement(self, ctx:cpp14Parser.IfStatementContext):
        '''
        ifStatement : IF LPAREN expression RPAREN statement (ELSE statement)?;
        '''
        #print(f"visitIfStatement:{ctx.getText()}, {ctx.getChildCount()}")
        self.symbolTable.enterScope()
        Builder = self.Builders[-1]
        trueblock = Builder.append_basic_block()

        #if else的情况
        if len(ctx.statement())==2:
            falseblock = Builder.append_basic_block()
            endblock = Builder.append_basic_block()
            
            #条件跳转
            result = self.visit(ctx.getChild(2))
            condition = self.toBool(result)
            Builder.cbranch(condition['value'], trueblock, falseblock)
            
            #if块
            trueblockbuilder = ir.IRBuilder(trueblock)
            self.Builders.pop()
            self.Builders.append(trueblockbuilder)
            self.visit(ctx.getChild(4))
            if(not self.Builders[-1].block.is_terminated):
                self.Builders[-1].branch(endblock)
            
            #else块
            falseblockbuilder = ir.IRBuilder(falseblock)
            self.Builders.pop()
            self.Builders.append(falseblockbuilder)
            self.visit(ctx.getChild(6))
            #self.Builders[-1].branch(endblock)
            if(not self.Builders[-1].block.is_terminated):
                self.Builders[-1].branch(endblock)
            
            #endif标识符
            self.Builders.pop()
            self.Builders.append(ir.IRBuilder(endblock))
            
        #只有if没有else的情况
        else:
            endblock = Builder.append_basic_block()
            
            #条件跳转
            result = self.visit(ctx.getChild(2))
            condition = self.toBool(result)
            Builder.cbranch(condition['value'], trueblock, endblock)
            
            #if块
            trueblockbuilder = ir.IRBuilder(trueblock)
            self.Builders.pop()
            self.Builders.append(trueblockbuilder)
            self.visit(ctx.getChild(4))
            if(not self.Builders[-1].block.is_terminated):
                self.Builders[-1].branch(endblock)
            
            #endif标识符
            self.Builders.pop()
            self.Builders.append(ir.IRBuilder(endblock))

        self.symbolTable.exitScope()
        return

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
