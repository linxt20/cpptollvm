# Generated from grammar/cpp14Parser.g4 by ANTLR 4.11.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .cpp14Parser import cpp14Parser
else:
    from cpp14Parser import cpp14Parser

# This class defines a complete listener for a parse tree produced by cpp14Parser.
class cpp14ParserListener(ParseTreeListener):

    # Enter a parse tree produced by cpp14Parser#literals.
    def enterLiterals(self, ctx:cpp14Parser.LiteralsContext):
        pass

    # Exit a parse tree produced by cpp14Parser#literals.
    def exitLiterals(self, ctx:cpp14Parser.LiteralsContext):
        pass


    # Enter a parse tree produced by cpp14Parser#floatingLiteral.
    def enterFloatingLiteral(self, ctx:cpp14Parser.FloatingLiteralContext):
        pass

    # Exit a parse tree produced by cpp14Parser#floatingLiteral.
    def exitFloatingLiteral(self, ctx:cpp14Parser.FloatingLiteralContext):
        pass


    # Enter a parse tree produced by cpp14Parser#integerLiteral.
    def enterIntegerLiteral(self, ctx:cpp14Parser.IntegerLiteralContext):
        pass

    # Exit a parse tree produced by cpp14Parser#integerLiteral.
    def exitIntegerLiteral(self, ctx:cpp14Parser.IntegerLiteralContext):
        pass


    # Enter a parse tree produced by cpp14Parser#characterLiteral.
    def enterCharacterLiteral(self, ctx:cpp14Parser.CharacterLiteralContext):
        pass

    # Exit a parse tree produced by cpp14Parser#characterLiteral.
    def exitCharacterLiteral(self, ctx:cpp14Parser.CharacterLiteralContext):
        pass


    # Enter a parse tree produced by cpp14Parser#stringLiteral.
    def enterStringLiteral(self, ctx:cpp14Parser.StringLiteralContext):
        pass

    # Exit a parse tree produced by cpp14Parser#stringLiteral.
    def exitStringLiteral(self, ctx:cpp14Parser.StringLiteralContext):
        pass


    # Enter a parse tree produced by cpp14Parser#translationUnit.
    def enterTranslationUnit(self, ctx:cpp14Parser.TranslationUnitContext):
        pass

    # Exit a parse tree produced by cpp14Parser#translationUnit.
    def exitTranslationUnit(self, ctx:cpp14Parser.TranslationUnitContext):
        pass


    # Enter a parse tree produced by cpp14Parser#baseSpecifierList.
    def enterBaseSpecifierList(self, ctx:cpp14Parser.BaseSpecifierListContext):
        pass

    # Exit a parse tree produced by cpp14Parser#baseSpecifierList.
    def exitBaseSpecifierList(self, ctx:cpp14Parser.BaseSpecifierListContext):
        pass


    # Enter a parse tree produced by cpp14Parser#accessSpecifier.
    def enterAccessSpecifier(self, ctx:cpp14Parser.AccessSpecifierContext):
        pass

    # Exit a parse tree produced by cpp14Parser#accessSpecifier.
    def exitAccessSpecifier(self, ctx:cpp14Parser.AccessSpecifierContext):
        pass


    # Enter a parse tree produced by cpp14Parser#accessLabel.
    def enterAccessLabel(self, ctx:cpp14Parser.AccessLabelContext):
        pass

    # Exit a parse tree produced by cpp14Parser#accessLabel.
    def exitAccessLabel(self, ctx:cpp14Parser.AccessLabelContext):
        pass


    # Enter a parse tree produced by cpp14Parser#memberDeclaration.
    def enterMemberDeclaration(self, ctx:cpp14Parser.MemberDeclarationContext):
        pass

    # Exit a parse tree produced by cpp14Parser#memberDeclaration.
    def exitMemberDeclaration(self, ctx:cpp14Parser.MemberDeclarationContext):
        pass


    # Enter a parse tree produced by cpp14Parser#constructorDeclaration.
    def enterConstructorDeclaration(self, ctx:cpp14Parser.ConstructorDeclarationContext):
        pass

    # Exit a parse tree produced by cpp14Parser#constructorDeclaration.
    def exitConstructorDeclaration(self, ctx:cpp14Parser.ConstructorDeclarationContext):
        pass


    # Enter a parse tree produced by cpp14Parser#destructorDeclaration.
    def enterDestructorDeclaration(self, ctx:cpp14Parser.DestructorDeclarationContext):
        pass

    # Exit a parse tree produced by cpp14Parser#destructorDeclaration.
    def exitDestructorDeclaration(self, ctx:cpp14Parser.DestructorDeclarationContext):
        pass


    # Enter a parse tree produced by cpp14Parser#memberSpecification.
    def enterMemberSpecification(self, ctx:cpp14Parser.MemberSpecificationContext):
        pass

    # Exit a parse tree produced by cpp14Parser#memberSpecification.
    def exitMemberSpecification(self, ctx:cpp14Parser.MemberSpecificationContext):
        pass


    # Enter a parse tree produced by cpp14Parser#classDefinition.
    def enterClassDefinition(self, ctx:cpp14Parser.ClassDefinitionContext):
        pass

    # Exit a parse tree produced by cpp14Parser#classDefinition.
    def exitClassDefinition(self, ctx:cpp14Parser.ClassDefinitionContext):
        pass


    # Enter a parse tree produced by cpp14Parser#constExpression.
    def enterConstExpression(self, ctx:cpp14Parser.ConstExpressionContext):
        pass

    # Exit a parse tree produced by cpp14Parser#constExpression.
    def exitConstExpression(self, ctx:cpp14Parser.ConstExpressionContext):
        pass


    # Enter a parse tree produced by cpp14Parser#leftExpression.
    def enterLeftExpression(self, ctx:cpp14Parser.LeftExpressionContext):
        pass

    # Exit a parse tree produced by cpp14Parser#leftExpression.
    def exitLeftExpression(self, ctx:cpp14Parser.LeftExpressionContext):
        pass


    # Enter a parse tree produced by cpp14Parser#expression.
    def enterExpression(self, ctx:cpp14Parser.ExpressionContext):
        pass

    # Exit a parse tree produced by cpp14Parser#expression.
    def exitExpression(self, ctx:cpp14Parser.ExpressionContext):
        pass


    # Enter a parse tree produced by cpp14Parser#statement.
    def enterStatement(self, ctx:cpp14Parser.StatementContext):
        pass

    # Exit a parse tree produced by cpp14Parser#statement.
    def exitStatement(self, ctx:cpp14Parser.StatementContext):
        pass


    # Enter a parse tree produced by cpp14Parser#block.
    def enterBlock(self, ctx:cpp14Parser.BlockContext):
        pass

    # Exit a parse tree produced by cpp14Parser#block.
    def exitBlock(self, ctx:cpp14Parser.BlockContext):
        pass


    # Enter a parse tree produced by cpp14Parser#functionCall.
    def enterFunctionCall(self, ctx:cpp14Parser.FunctionCallContext):
        pass

    # Exit a parse tree produced by cpp14Parser#functionCall.
    def exitFunctionCall(self, ctx:cpp14Parser.FunctionCallContext):
        pass


    # Enter a parse tree produced by cpp14Parser#ifStatement.
    def enterIfStatement(self, ctx:cpp14Parser.IfStatementContext):
        pass

    # Exit a parse tree produced by cpp14Parser#ifStatement.
    def exitIfStatement(self, ctx:cpp14Parser.IfStatementContext):
        pass


    # Enter a parse tree produced by cpp14Parser#caseStatement.
    def enterCaseStatement(self, ctx:cpp14Parser.CaseStatementContext):
        pass

    # Exit a parse tree produced by cpp14Parser#caseStatement.
    def exitCaseStatement(self, ctx:cpp14Parser.CaseStatementContext):
        pass


    # Enter a parse tree produced by cpp14Parser#switchStatement.
    def enterSwitchStatement(self, ctx:cpp14Parser.SwitchStatementContext):
        pass

    # Exit a parse tree produced by cpp14Parser#switchStatement.
    def exitSwitchStatement(self, ctx:cpp14Parser.SwitchStatementContext):
        pass


    # Enter a parse tree produced by cpp14Parser#whileStatement.
    def enterWhileStatement(self, ctx:cpp14Parser.WhileStatementContext):
        pass

    # Exit a parse tree produced by cpp14Parser#whileStatement.
    def exitWhileStatement(self, ctx:cpp14Parser.WhileStatementContext):
        pass


    # Enter a parse tree produced by cpp14Parser#doWhileStatement.
    def enterDoWhileStatement(self, ctx:cpp14Parser.DoWhileStatementContext):
        pass

    # Exit a parse tree produced by cpp14Parser#doWhileStatement.
    def exitDoWhileStatement(self, ctx:cpp14Parser.DoWhileStatementContext):
        pass


    # Enter a parse tree produced by cpp14Parser#forStatement.
    def enterForStatement(self, ctx:cpp14Parser.ForStatementContext):
        pass

    # Exit a parse tree produced by cpp14Parser#forStatement.
    def exitForStatement(self, ctx:cpp14Parser.ForStatementContext):
        pass


    # Enter a parse tree produced by cpp14Parser#forExprSet.
    def enterForExprSet(self, ctx:cpp14Parser.ForExprSetContext):
        pass

    # Exit a parse tree produced by cpp14Parser#forExprSet.
    def exitForExprSet(self, ctx:cpp14Parser.ForExprSetContext):
        pass


    # Enter a parse tree produced by cpp14Parser#returnStatement.
    def enterReturnStatement(self, ctx:cpp14Parser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by cpp14Parser#returnStatement.
    def exitReturnStatement(self, ctx:cpp14Parser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by cpp14Parser#breakStatement.
    def enterBreakStatement(self, ctx:cpp14Parser.BreakStatementContext):
        pass

    # Exit a parse tree produced by cpp14Parser#breakStatement.
    def exitBreakStatement(self, ctx:cpp14Parser.BreakStatementContext):
        pass


    # Enter a parse tree produced by cpp14Parser#continueStatement.
    def enterContinueStatement(self, ctx:cpp14Parser.ContinueStatementContext):
        pass

    # Exit a parse tree produced by cpp14Parser#continueStatement.
    def exitContinueStatement(self, ctx:cpp14Parser.ContinueStatementContext):
        pass


    # Enter a parse tree produced by cpp14Parser#declaration.
    def enterDeclaration(self, ctx:cpp14Parser.DeclarationContext):
        pass

    # Exit a parse tree produced by cpp14Parser#declaration.
    def exitDeclaration(self, ctx:cpp14Parser.DeclarationContext):
        pass


    # Enter a parse tree produced by cpp14Parser#normalArrDecl.
    def enterNormalArrDecl(self, ctx:cpp14Parser.NormalArrDeclContext):
        pass

    # Exit a parse tree produced by cpp14Parser#normalArrDecl.
    def exitNormalArrDecl(self, ctx:cpp14Parser.NormalArrDeclContext):
        pass


    # Enter a parse tree produced by cpp14Parser#stringDecl.
    def enterStringDecl(self, ctx:cpp14Parser.StringDeclContext):
        pass

    # Exit a parse tree produced by cpp14Parser#stringDecl.
    def exitStringDecl(self, ctx:cpp14Parser.StringDeclContext):
        pass


    # Enter a parse tree produced by cpp14Parser#varDeclWithoutInit.
    def enterVarDeclWithoutInit(self, ctx:cpp14Parser.VarDeclWithoutInitContext):
        pass

    # Exit a parse tree produced by cpp14Parser#varDeclWithoutInit.
    def exitVarDeclWithoutInit(self, ctx:cpp14Parser.VarDeclWithoutInitContext):
        pass


    # Enter a parse tree produced by cpp14Parser#varDeclWithConstInit.
    def enterVarDeclWithConstInit(self, ctx:cpp14Parser.VarDeclWithConstInitContext):
        pass

    # Exit a parse tree produced by cpp14Parser#varDeclWithConstInit.
    def exitVarDeclWithConstInit(self, ctx:cpp14Parser.VarDeclWithConstInitContext):
        pass


    # Enter a parse tree produced by cpp14Parser#varDeclWithInit.
    def enterVarDeclWithInit(self, ctx:cpp14Parser.VarDeclWithInitContext):
        pass

    # Exit a parse tree produced by cpp14Parser#varDeclWithInit.
    def exitVarDeclWithInit(self, ctx:cpp14Parser.VarDeclWithInitContext):
        pass


    # Enter a parse tree produced by cpp14Parser#variableDeclarator.
    def enterVariableDeclarator(self, ctx:cpp14Parser.VariableDeclaratorContext):
        pass

    # Exit a parse tree produced by cpp14Parser#variableDeclarator.
    def exitVariableDeclarator(self, ctx:cpp14Parser.VariableDeclaratorContext):
        pass


    # Enter a parse tree produced by cpp14Parser#functionDecl.
    def enterFunctionDecl(self, ctx:cpp14Parser.FunctionDeclContext):
        pass

    # Exit a parse tree produced by cpp14Parser#functionDecl.
    def exitFunctionDecl(self, ctx:cpp14Parser.FunctionDeclContext):
        pass


    # Enter a parse tree produced by cpp14Parser#functionDef.
    def enterFunctionDef(self, ctx:cpp14Parser.FunctionDefContext):
        pass

    # Exit a parse tree produced by cpp14Parser#functionDef.
    def exitFunctionDef(self, ctx:cpp14Parser.FunctionDefContext):
        pass


    # Enter a parse tree produced by cpp14Parser#functionParameter.
    def enterFunctionParameter(self, ctx:cpp14Parser.FunctionParameterContext):
        pass

    # Exit a parse tree produced by cpp14Parser#functionParameter.
    def exitFunctionParameter(self, ctx:cpp14Parser.FunctionParameterContext):
        pass


    # Enter a parse tree produced by cpp14Parser#typeSpecifier.
    def enterTypeSpecifier(self, ctx:cpp14Parser.TypeSpecifierContext):
        pass

    # Exit a parse tree produced by cpp14Parser#typeSpecifier.
    def exitTypeSpecifier(self, ctx:cpp14Parser.TypeSpecifierContext):
        pass


    # Enter a parse tree produced by cpp14Parser#pointerTypeSpecifier.
    def enterPointerTypeSpecifier(self, ctx:cpp14Parser.PointerTypeSpecifierContext):
        pass

    # Exit a parse tree produced by cpp14Parser#pointerTypeSpecifier.
    def exitPointerTypeSpecifier(self, ctx:cpp14Parser.PointerTypeSpecifierContext):
        pass


    # Enter a parse tree produced by cpp14Parser#integerTypeSpecifier.
    def enterIntegerTypeSpecifier(self, ctx:cpp14Parser.IntegerTypeSpecifierContext):
        pass

    # Exit a parse tree produced by cpp14Parser#integerTypeSpecifier.
    def exitIntegerTypeSpecifier(self, ctx:cpp14Parser.IntegerTypeSpecifierContext):
        pass


    # Enter a parse tree produced by cpp14Parser#realTypeSpecifier.
    def enterRealTypeSpecifier(self, ctx:cpp14Parser.RealTypeSpecifierContext):
        pass

    # Exit a parse tree produced by cpp14Parser#realTypeSpecifier.
    def exitRealTypeSpecifier(self, ctx:cpp14Parser.RealTypeSpecifierContext):
        pass


    # Enter a parse tree produced by cpp14Parser#booleanTypeSpecifier.
    def enterBooleanTypeSpecifier(self, ctx:cpp14Parser.BooleanTypeSpecifierContext):
        pass

    # Exit a parse tree produced by cpp14Parser#booleanTypeSpecifier.
    def exitBooleanTypeSpecifier(self, ctx:cpp14Parser.BooleanTypeSpecifierContext):
        pass


    # Enter a parse tree produced by cpp14Parser#charTypeSpecifier.
    def enterCharTypeSpecifier(self, ctx:cpp14Parser.CharTypeSpecifierContext):
        pass

    # Exit a parse tree produced by cpp14Parser#charTypeSpecifier.
    def exitCharTypeSpecifier(self, ctx:cpp14Parser.CharTypeSpecifierContext):
        pass


    # Enter a parse tree produced by cpp14Parser#voidTypeSpecifier.
    def enterVoidTypeSpecifier(self, ctx:cpp14Parser.VoidTypeSpecifierContext):
        pass

    # Exit a parse tree produced by cpp14Parser#voidTypeSpecifier.
    def exitVoidTypeSpecifier(self, ctx:cpp14Parser.VoidTypeSpecifierContext):
        pass



del cpp14Parser