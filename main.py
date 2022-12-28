from antlr4 import *
import sys, os
import ast
import json

from src.cpp14Lexer import cpp14Lexer
from src.cpp14Parser import cpp14Parser
from src.cpp14ParserListener import cpp14ParserListener as cpp14Listener
from src.cpp14ParserVisitor import cpp14ParserVisitor as cpp14Visitor
from llvmlite.ir.types import ArrayType
from llvmlite.ir.values import GlobalVariable, ReturnValue
from table import *
import llvmlite.ir as ir


class NewCpp14Visitor(cpp14Visitor):
    def __init__(self):
        super(cpp14Visitor, self).__init__()

        self.irModule = ir.Module()
        self.irBuilder = []
        self.irModule.triple = "x86_64-pc-linux"

    def visitLiterals(self, ctx:cpp14Parser.LiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp14Parser#floatingLiteral.
    def visitFloatingLiteral(self, ctx:cpp14Parser.FloatingLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp14Parser#integerLiteral.
    def visitIntegerLiteral(self, ctx:cpp14Parser.IntegerLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp14Parser#characterLiteral.
    def visitCharacterLiteral(self, ctx:cpp14Parser.CharacterLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp14Parser#stringLiteral.
    def visitStringLiteral(self, ctx:cpp14Parser.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp14Parser#constExpression.
    def visitConstExpression(self, ctx:cpp14Parser.ConstExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp14Parser#leftExpression.
    def visitLeftExpression(self, ctx:cpp14Parser.LeftExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp14Parser#expression.
    def visitExpression(self, ctx:cpp14Parser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp14Parser#block.
    def visitBlock(self, ctx:cpp14Parser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp14Parser#functionCall.
    def visitFunctionCall(self, ctx:cpp14Parser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp14Parser#ifStatement.
    def visitIfStatement(self, ctx:cpp14Parser.IfStatementContext):
        return self.visitChildren(ctx)


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
    def visitVarDeclWithInit(self, ctx:cpp14Parser.VarDeclWithInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp14Parser#variableDeclarator.
    def visitVariableDeclarator(self, ctx:cpp14Parser.VariableDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp14Parser#functionDecl.
    def visitFunctionDecl(self, ctx:cpp14Parser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp14Parser#functionDef.
    def visitFunctionDef(self, ctx:cpp14Parser.FunctionDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp14Parser#functionParameter.
    def visitFunctionParameter(self, ctx:cpp14Parser.FunctionParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp14Parser#typeSpecifier.
    def visitTypeSpecifier(self, ctx:cpp14Parser.TypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp14Parser#pointerTypeSpecifier.
    def visitPointerTypeSpecifier(self, ctx:cpp14Parser.PointerTypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp14Parser#integerTypeSpecifier.
    def visitIntegerTypeSpecifier(self, ctx:cpp14Parser.IntegerTypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp14Parser#realTypeSpecifier.
    def visitRealTypeSpecifier(self, ctx:cpp14Parser.RealTypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp14Parser#booleanTypeSpecifier.
    def visitBooleanTypeSpecifier(self, ctx:cpp14Parser.BooleanTypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp14Parser#charTypeSpecifier.
    def visitCharTypeSpecifier(self, ctx:cpp14Parser.CharTypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp14Parser#voidTypeSpecifier.
    def visitVoidTypeSpecifier(self, ctx:cpp14Parser.VoidTypeSpecifierContext):
        return self.visitChildren(ctx)


jsonString = ""
# global lasttype
def translate(text:str):
    text = text.replace("\\","\\\\")
    text = text.replace("\"","\\\"")
    if(len(text)>50):
        text = text[0:49]+"...(too long)"
    return text

def printTree(tree,k):
    global jsonString
    content = translate(tree.getText())
    if tree.getChildCount() == 0 :
        jsonString += ("{ \"" + f"type\": \"{content}\",  \"content\": \"{content}\", \"children\": []" + "},")
        return
    jsonString += ("{ \"" + f"type\": \"{str(type(tree))[36:-9]}\",  \"content\": \"{content}\",  \"children\": [")
    for i in range(tree.getChildCount()):
        printTree(tree.getChild(i), k + 1)
    jsonString += ("]},")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py (input_filename)")
        exit(0)
    else:
        filename = sys.argv[1]
        output_filename = filename.split(".")[0]+"parser.json"
        input_stream = FileStream(filename)
        # print(input_stream)
        # lexer
        lexer = cpp14Lexer(input_stream)
        stream = CommonTokenStream(lexer)
        # stream.fill()
        # tokennum = stream.getNumberOfOnChannelTokens()
        # tokens = stream.getTokens(0,tokennum)

        # if(output_filename):
        #     with open(output_filename, 'w') as f:
        #         for token in tokens:
        #             f.write(str(token)+' ')
        # parser
        parser = cpp14Parser(stream)
        tree = parser.translationUnit()
        printTree(tree,0)
        # print(output_filename)
        # print(jsonString)

        # print(tree)
        # print(tree.toStringTree(recog=parser))
        # if(output_filename):
        #     with open(output_filename, 'w') as f:
        #         f.write(str(tree.toStringTree(recog=parser)))
        jsonString = jsonString.replace(",]","]")
        jsonString = jsonString[0:len(jsonString)-1]

        final_json = json.loads(jsonString)

        final_string=json.dumps(final_json,indent=4)
        if(output_filename):
            with open(output_filename, 'w') as f:
                f.write(final_string)
        exit(0)