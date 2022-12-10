# Generated from grammar/cppparser.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .cppparser import cppparser
else:
    from cppparser import cppparser

# This class defines a complete listener for a parse tree produced by cppparser.
class cppparserListener(ParseTreeListener):

    # Enter a parse tree produced by cppparser#literals.
    def enterLiterals(self, ctx:cppparser.LiteralsContext):
        pass

    # Exit a parse tree produced by cppparser#literals.
    def exitLiterals(self, ctx:cppparser.LiteralsContext):
        pass


    # Enter a parse tree produced by cppparser#floatingLiteral.
    def enterFloatingLiteral(self, ctx:cppparser.FloatingLiteralContext):
        pass

    # Exit a parse tree produced by cppparser#floatingLiteral.
    def exitFloatingLiteral(self, ctx:cppparser.FloatingLiteralContext):
        pass


    # Enter a parse tree produced by cppparser#integerLiteral.
    def enterIntegerLiteral(self, ctx:cppparser.IntegerLiteralContext):
        pass

    # Exit a parse tree produced by cppparser#integerLiteral.
    def exitIntegerLiteral(self, ctx:cppparser.IntegerLiteralContext):
        pass


    # Enter a parse tree produced by cppparser#characterLiteral.
    def enterCharacterLiteral(self, ctx:cppparser.CharacterLiteralContext):
        pass

    # Exit a parse tree produced by cppparser#characterLiteral.
    def exitCharacterLiteral(self, ctx:cppparser.CharacterLiteralContext):
        pass


    # Enter a parse tree produced by cppparser#stringLiteral.
    def enterStringLiteral(self, ctx:cppparser.StringLiteralContext):
        pass

    # Exit a parse tree produced by cppparser#stringLiteral.
    def exitStringLiteral(self, ctx:cppparser.StringLiteralContext):
        pass


    # Enter a parse tree produced by cppparser#translationUnit.
    def enterTranslationUnit(self, ctx:cppparser.TranslationUnitContext):
        pass

    # Exit a parse tree produced by cppparser#translationUnit.
    def exitTranslationUnit(self, ctx:cppparser.TranslationUnitContext):
        pass


    # Enter a parse tree produced by cppparser#baseSpecifierList.
    def enterBaseSpecifierList(self, ctx:cppparser.BaseSpecifierListContext):
        pass

    # Exit a parse tree produced by cppparser#baseSpecifierList.
    def exitBaseSpecifierList(self, ctx:cppparser.BaseSpecifierListContext):
        pass


    # Enter a parse tree produced by cppparser#accessSpecifier.
    def enterAccessSpecifier(self, ctx:cppparser.AccessSpecifierContext):
        pass

    # Exit a parse tree produced by cppparser#accessSpecifier.
    def exitAccessSpecifier(self, ctx:cppparser.AccessSpecifierContext):
        pass


    # Enter a parse tree produced by cppparser#accessLabel.
    def enterAccessLabel(self, ctx:cppparser.AccessLabelContext):
        pass

    # Exit a parse tree produced by cppparser#accessLabel.
    def exitAccessLabel(self, ctx:cppparser.AccessLabelContext):
        pass


    # Enter a parse tree produced by cppparser#memberDeclaration.
    def enterMemberDeclaration(self, ctx:cppparser.MemberDeclarationContext):
        pass

    # Exit a parse tree produced by cppparser#memberDeclaration.
    def exitMemberDeclaration(self, ctx:cppparser.MemberDeclarationContext):
        pass


    # Enter a parse tree produced by cppparser#constructorDeclaration.
    def enterConstructorDeclaration(self, ctx:cppparser.ConstructorDeclarationContext):
        pass

    # Exit a parse tree produced by cppparser#constructorDeclaration.
    def exitConstructorDeclaration(self, ctx:cppparser.ConstructorDeclarationContext):
        pass


    # Enter a parse tree produced by cppparser#destructorDeclaration.
    def enterDestructorDeclaration(self, ctx:cppparser.DestructorDeclarationContext):
        pass

    # Exit a parse tree produced by cppparser#destructorDeclaration.
    def exitDestructorDeclaration(self, ctx:cppparser.DestructorDeclarationContext):
        pass


    # Enter a parse tree produced by cppparser#memberSpecification.
    def enterMemberSpecification(self, ctx:cppparser.MemberSpecificationContext):
        pass

    # Exit a parse tree produced by cppparser#memberSpecification.
    def exitMemberSpecification(self, ctx:cppparser.MemberSpecificationContext):
        pass


    # Enter a parse tree produced by cppparser#classDefinition.
    def enterClassDefinition(self, ctx:cppparser.ClassDefinitionContext):
        pass

    # Exit a parse tree produced by cppparser#classDefinition.
    def exitClassDefinition(self, ctx:cppparser.ClassDefinitionContext):
        pass


    # Enter a parse tree produced by cppparser#constExpression.
    def enterConstExpression(self, ctx:cppparser.ConstExpressionContext):
        pass

    # Exit a parse tree produced by cppparser#constExpression.
    def exitConstExpression(self, ctx:cppparser.ConstExpressionContext):
        pass


    # Enter a parse tree produced by cppparser#leftExpression.
    def enterLeftExpression(self, ctx:cppparser.LeftExpressionContext):
        pass

    # Exit a parse tree produced by cppparser#leftExpression.
    def exitLeftExpression(self, ctx:cppparser.LeftExpressionContext):
        pass


    # Enter a parse tree produced by cppparser#expression.
    def enterExpression(self, ctx:cppparser.ExpressionContext):
        pass

    # Exit a parse tree produced by cppparser#expression.
    def exitExpression(self, ctx:cppparser.ExpressionContext):
        pass


    # Enter a parse tree produced by cppparser#statement.
    def enterStatement(self, ctx:cppparser.StatementContext):
        pass

    # Exit a parse tree produced by cppparser#statement.
    def exitStatement(self, ctx:cppparser.StatementContext):
        pass


    # Enter a parse tree produced by cppparser#block.
    def enterBlock(self, ctx:cppparser.BlockContext):
        pass

    # Exit a parse tree produced by cppparser#block.
    def exitBlock(self, ctx:cppparser.BlockContext):
        pass


    # Enter a parse tree produced by cppparser#functionCall.
    def enterFunctionCall(self, ctx:cppparser.FunctionCallContext):
        pass

    # Exit a parse tree produced by cppparser#functionCall.
    def exitFunctionCall(self, ctx:cppparser.FunctionCallContext):
        pass


    # Enter a parse tree produced by cppparser#ifStatement.
    def enterIfStatement(self, ctx:cppparser.IfStatementContext):
        pass

    # Exit a parse tree produced by cppparser#ifStatement.
    def exitIfStatement(self, ctx:cppparser.IfStatementContext):
        pass


    # Enter a parse tree produced by cppparser#caseStatement.
    def enterCaseStatement(self, ctx:cppparser.CaseStatementContext):
        pass

    # Exit a parse tree produced by cppparser#caseStatement.
    def exitCaseStatement(self, ctx:cppparser.CaseStatementContext):
        pass


    # Enter a parse tree produced by cppparser#switchStatement.
    def enterSwitchStatement(self, ctx:cppparser.SwitchStatementContext):
        pass

    # Exit a parse tree produced by cppparser#switchStatement.
    def exitSwitchStatement(self, ctx:cppparser.SwitchStatementContext):
        pass


    # Enter a parse tree produced by cppparser#whileStatement.
    def enterWhileStatement(self, ctx:cppparser.WhileStatementContext):
        pass

    # Exit a parse tree produced by cppparser#whileStatement.
    def exitWhileStatement(self, ctx:cppparser.WhileStatementContext):
        pass


    # Enter a parse tree produced by cppparser#doWhileStatement.
    def enterDoWhileStatement(self, ctx:cppparser.DoWhileStatementContext):
        pass

    # Exit a parse tree produced by cppparser#doWhileStatement.
    def exitDoWhileStatement(self, ctx:cppparser.DoWhileStatementContext):
        pass


    # Enter a parse tree produced by cppparser#forStatement.
    def enterForStatement(self, ctx:cppparser.ForStatementContext):
        pass

    # Exit a parse tree produced by cppparser#forStatement.
    def exitForStatement(self, ctx:cppparser.ForStatementContext):
        pass


    # Enter a parse tree produced by cppparser#forExprSet.
    def enterForExprSet(self, ctx:cppparser.ForExprSetContext):
        pass

    # Exit a parse tree produced by cppparser#forExprSet.
    def exitForExprSet(self, ctx:cppparser.ForExprSetContext):
        pass


    # Enter a parse tree produced by cppparser#returnStatement.
    def enterReturnStatement(self, ctx:cppparser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by cppparser#returnStatement.
    def exitReturnStatement(self, ctx:cppparser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by cppparser#breakStatement.
    def enterBreakStatement(self, ctx:cppparser.BreakStatementContext):
        pass

    # Exit a parse tree produced by cppparser#breakStatement.
    def exitBreakStatement(self, ctx:cppparser.BreakStatementContext):
        pass


    # Enter a parse tree produced by cppparser#continueStatement.
    def enterContinueStatement(self, ctx:cppparser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by cppparser#continueStatement.
    def exitContinueStatement(self, ctx:cppparser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by cppparser#declaration.
    def enterDeclaration(self, ctx:cppparser.DeclarationContext):
        pass

    # Exit a parse tree produced by cppparser#declaration.
    def exitDeclaration(self, ctx:cppparser.DeclarationContext):
        pass


    # Enter a parse tree produced by cppparser#normalArrDecl.
    def enterNormalArrDecl(self, ctx:cppparser.NormalArrDeclContext):
        pass

    # Exit a parse tree produced by cppparser#normalArrDecl.
    def exitNormalArrDecl(self, ctx:cppparser.NormalArrDeclContext):
        pass


    # Enter a parse tree produced by cppparser#stringDecl.
    def enterStringDecl(self, ctx:cppparser.StringDeclContext):
        pass

    # Exit a parse tree produced by cppparser#stringDecl.
    def exitStringDecl(self, ctx:cppparser.StringDeclContext):
        pass


    # Enter a parse tree produced by cppparser#varDeclWithoutInit.
    def enterVarDeclWithoutInit(self, ctx:cppparser.VarDeclWithoutInitContext):
        pass

    # Exit a parse tree produced by cppparser#varDeclWithoutInit.
    def exitVarDeclWithoutInit(self, ctx:cppparser.VarDeclWithoutInitContext):
        pass


    # Enter a parse tree produced by cppparser#varDeclWithConstInit.
    def enterVarDeclWithConstInit(self, ctx:cppparser.VarDeclWithConstInitContext):
        pass

    # Exit a parse tree produced by cppparser#varDeclWithConstInit.
    def exitVarDeclWithConstInit(self, ctx:cppparser.VarDeclWithConstInitContext):
        pass


    # Enter a parse tree produced by cppparser#varDeclWithInit.
    def enterVarDeclWithInit(self, ctx:cppparser.VarDeclWithInitContext):
        pass

    # Exit a parse tree produced by cppparser#varDeclWithInit.
    def exitVarDeclWithInit(self, ctx:cppparser.VarDeclWithInitContext):
        pass


    # Enter a parse tree produced by cppparser#variableDeclarator.
    def enterVariableDeclarator(self, ctx:cppparser.VariableDeclaratorContext):
        pass

    # Exit a parse tree produced by cppparser#variableDeclarator.
    def exitVariableDeclarator(self, ctx:cppparser.VariableDeclaratorContext):
        pass


    # Enter a parse tree produced by cppparser#functionDecl.
    def enterFunctionDecl(self, ctx:cppparser.FunctionDeclContext):
        pass

    # Exit a parse tree produced by cppparser#functionDecl.
    def exitFunctionDecl(self, ctx:cppparser.FunctionDeclContext):
        pass


    # Enter a parse tree produced by cppparser#functionDef.
    def enterFunctionDef(self, ctx:cppparser.FunctionDefContext):
        pass

    # Exit a parse tree produced by cppparser#functionDef.
    def exitFunctionDef(self, ctx:cppparser.FunctionDefContext):
        pass


    # Enter a parse tree produced by cppparser#functionParameter.
    def enterFunctionParameter(self, ctx:cppparser.FunctionParameterContext):
        pass

    # Exit a parse tree produced by cppparser#functionParameter.
    def exitFunctionParameter(self, ctx:cppparser.FunctionParameterContext):
        pass


    # Enter a parse tree produced by cppparser#typeSpecifier.
    def enterTypeSpecifier(self, ctx:cppparser.TypeSpecifierContext):
        pass

    # Exit a parse tree produced by cppparser#typeSpecifier.
    def exitTypeSpecifier(self, ctx:cppparser.TypeSpecifierContext):
        pass


    # Enter a parse tree produced by cppparser#pointerTypeSpecifier.
    def enterPointerTypeSpecifier(self, ctx:cppparser.PointerTypeSpecifierContext):
        pass

    # Exit a parse tree produced by cppparser#pointerTypeSpecifier.
    def exitPointerTypeSpecifier(self, ctx:cppparser.PointerTypeSpecifierContext):
        pass


    # Enter a parse tree produced by cppparser#integerTypeSpecifier.
    def enterIntegerTypeSpecifier(self, ctx:cppparser.IntegerTypeSpecifierContext):
        pass

    # Exit a parse tree produced by cppparser#integerTypeSpecifier.
    def exitIntegerTypeSpecifier(self, ctx:cppparser.IntegerTypeSpecifierContext):
        pass


    # Enter a parse tree produced by cppparser#realTypeSpecifier.
    def enterRealTypeSpecifier(self, ctx:cppparser.RealTypeSpecifierContext):
        pass

    # Exit a parse tree produced by cppparser#realTypeSpecifier.
    def exitRealTypeSpecifier(self, ctx:cppparser.RealTypeSpecifierContext):
        pass


    # Enter a parse tree produced by cppparser#booleanTypeSpecifier.
    def enterBooleanTypeSpecifier(self, ctx:cppparser.BooleanTypeSpecifierContext):
        pass

    # Exit a parse tree produced by cppparser#booleanTypeSpecifier.
    def exitBooleanTypeSpecifier(self, ctx:cppparser.BooleanTypeSpecifierContext):
        pass


    # Enter a parse tree produced by cppparser#charTypeSpecifier.
    def enterCharTypeSpecifier(self, ctx:cppparser.CharTypeSpecifierContext):
        pass

    # Exit a parse tree produced by cppparser#charTypeSpecifier.
    def exitCharTypeSpecifier(self, ctx:cppparser.CharTypeSpecifierContext):
        pass


    # Enter a parse tree produced by cppparser#voidTypeSpecifier.
    def enterVoidTypeSpecifier(self, ctx:cppparser.VoidTypeSpecifierContext):
        pass

    # Exit a parse tree produced by cppparser#voidTypeSpecifier.
    def exitVoidTypeSpecifier(self, ctx:cppparser.VoidTypeSpecifierContext):
        pass



del cppparser