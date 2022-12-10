# Generated from grammar/cppparser.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .cppparser import cppparser
else:
    from cppparser import cppparser

# This class defines a complete generic visitor for a parse tree produced by cppparser.

class cppparserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by cppparser#literals.
    def visitLiterals(self, ctx:cppparser.LiteralsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppparser#floatingLiteral.
    def visitFloatingLiteral(self, ctx:cppparser.FloatingLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppparser#integerLiteral.
    def visitIntegerLiteral(self, ctx:cppparser.IntegerLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppparser#characterLiteral.
    def visitCharacterLiteral(self, ctx:cppparser.CharacterLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppparser#stringLiteral.
    def visitStringLiteral(self, ctx:cppparser.StringLiteralContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppparser#translationUnit.
    def visitTranslationUnit(self, ctx:cppparser.TranslationUnitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppparser#baseSpecifierList.
    def visitBaseSpecifierList(self, ctx:cppparser.BaseSpecifierListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppparser#accessSpecifier.
    def visitAccessSpecifier(self, ctx:cppparser.AccessSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppparser#accessLabel.
    def visitAccessLabel(self, ctx:cppparser.AccessLabelContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppparser#memberDeclaration.
    def visitMemberDeclaration(self, ctx:cppparser.MemberDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppparser#constructorDeclaration.
    def visitConstructorDeclaration(self, ctx:cppparser.ConstructorDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppparser#destructorDeclaration.
    def visitDestructorDeclaration(self, ctx:cppparser.DestructorDeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppparser#memberSpecification.
    def visitMemberSpecification(self, ctx:cppparser.MemberSpecificationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppparser#classDefinition.
    def visitClassDefinition(self, ctx:cppparser.ClassDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppparser#constExpression.
    def visitConstExpression(self, ctx:cppparser.ConstExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppparser#leftExpression.
    def visitLeftExpression(self, ctx:cppparser.LeftExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppparser#expression.
    def visitExpression(self, ctx:cppparser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppparser#statement.
    def visitStatement(self, ctx:cppparser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppparser#block.
    def visitBlock(self, ctx:cppparser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppparser#functionCall.
    def visitFunctionCall(self, ctx:cppparser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppparser#ifStatement.
    def visitIfStatement(self, ctx:cppparser.IfStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppparser#caseStatement.
    def visitCaseStatement(self, ctx:cppparser.CaseStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppparser#switchStatement.
    def visitSwitchStatement(self, ctx:cppparser.SwitchStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppparser#whileStatement.
    def visitWhileStatement(self, ctx:cppparser.WhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppparser#doWhileStatement.
    def visitDoWhileStatement(self, ctx:cppparser.DoWhileStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppparser#forStatement.
    def visitForStatement(self, ctx:cppparser.ForStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppparser#forExprSet.
    def visitForExprSet(self, ctx:cppparser.ForExprSetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppparser#returnStatement.
    def visitReturnStatement(self, ctx:cppparser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppparser#breakStatement.
    def visitBreakStatement(self, ctx:cppparser.BreakStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppparser#continueStatement.
    def visitContinueStatement(self, ctx:cppparser.ContinueStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppparser#declaration.
    def visitDeclaration(self, ctx:cppparser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppparser#normalArrDecl.
    def visitNormalArrDecl(self, ctx:cppparser.NormalArrDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppparser#stringDecl.
    def visitStringDecl(self, ctx:cppparser.StringDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppparser#varDeclWithoutInit.
    def visitVarDeclWithoutInit(self, ctx:cppparser.VarDeclWithoutInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppparser#varDeclWithConstInit.
    def visitVarDeclWithConstInit(self, ctx:cppparser.VarDeclWithConstInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppparser#varDeclWithInit.
    def visitVarDeclWithInit(self, ctx:cppparser.VarDeclWithInitContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppparser#variableDeclarator.
    def visitVariableDeclarator(self, ctx:cppparser.VariableDeclaratorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppparser#functionDecl.
    def visitFunctionDecl(self, ctx:cppparser.FunctionDeclContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppparser#functionDef.
    def visitFunctionDef(self, ctx:cppparser.FunctionDefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppparser#functionParameter.
    def visitFunctionParameter(self, ctx:cppparser.FunctionParameterContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppparser#typeSpecifier.
    def visitTypeSpecifier(self, ctx:cppparser.TypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppparser#pointerTypeSpecifier.
    def visitPointerTypeSpecifier(self, ctx:cppparser.PointerTypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppparser#integerTypeSpecifier.
    def visitIntegerTypeSpecifier(self, ctx:cppparser.IntegerTypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppparser#realTypeSpecifier.
    def visitRealTypeSpecifier(self, ctx:cppparser.RealTypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppparser#booleanTypeSpecifier.
    def visitBooleanTypeSpecifier(self, ctx:cppparser.BooleanTypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppparser#charTypeSpecifier.
    def visitCharTypeSpecifier(self, ctx:cppparser.CharTypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by cppparser#voidTypeSpecifier.
    def visitVoidTypeSpecifier(self, ctx:cppparser.VoidTypeSpecifierContext):
        return self.visitChildren(ctx)



del cppparser