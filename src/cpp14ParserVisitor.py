# Generated from grammar/cpp14Parser.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .cpp14Parser import cpp14Parser
else:
    from cpp14Parser import cpp14Parser

# This class defines a complete generic visitor for a parse tree produced by cpp14Parser.

class cpp14ParserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by cpp14Parser#literals.
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


    # Visit a parse tree produced by cpp14Parser#translationUnit.
    def visitTranslationUnit(self, ctx:cpp14Parser.TranslationUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp14Parser#baseSpecifierList.
    def visitBaseSpecifierList(self, ctx:cpp14Parser.BaseSpecifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp14Parser#accessSpecifier.
    def visitAccessSpecifier(self, ctx:cpp14Parser.AccessSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp14Parser#accessLabel.
    def visitAccessLabel(self, ctx:cpp14Parser.AccessLabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp14Parser#memberDeclaration.
    def visitMemberDeclaration(self, ctx:cpp14Parser.MemberDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp14Parser#constructorDeclaration.
    def visitConstructorDeclaration(self, ctx:cpp14Parser.ConstructorDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp14Parser#destructorDeclaration.
    def visitDestructorDeclaration(self, ctx:cpp14Parser.DestructorDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp14Parser#memberSpecification.
    def visitMemberSpecification(self, ctx:cpp14Parser.MemberSpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cpp14Parser#classDefinition.
    def visitClassDefinition(self, ctx:cpp14Parser.ClassDefinitionContext):
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


    # Visit a parse tree produced by cpp14Parser#statement.
    def visitStatement(self, ctx:cpp14Parser.StatementContext):
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


    # Visit a parse tree produced by cpp14Parser#forExprSet.
    def visitForExprSet(self, ctx:cpp14Parser.ForExprSetContext):
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


    # Visit a parse tree produced by cpp14Parser#declaration.
    def visitDeclaration(self, ctx:cpp14Parser.DeclarationContext):
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



del cpp14Parser