# Generated from m.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .mParser import mParser
else:
    from mParser import mParser

# This class defines a complete listener for a parse tree produced by mParser.
class mListener(ParseTreeListener):

    # Enter a parse tree produced by mParser#MainExp.
    def enterMainExp(self, ctx:mParser.MainExpContext):
        pass

    # Exit a parse tree produced by mParser#MainExp.
    def exitMainExp(self, ctx:mParser.MainExpContext):
        pass


    # Enter a parse tree produced by mParser#AssignExpr.
    def enterAssignExpr(self, ctx:mParser.AssignExprContext):
        pass

    # Exit a parse tree produced by mParser#AssignExpr.
    def exitAssignExpr(self, ctx:mParser.AssignExprContext):
        pass


    # Enter a parse tree produced by mParser#AssignVar.
    def enterAssignVar(self, ctx:mParser.AssignVarContext):
        pass

    # Exit a parse tree produced by mParser#AssignVar.
    def exitAssignVar(self, ctx:mParser.AssignVarContext):
        pass


    # Enter a parse tree produced by mParser#AssignFunction.
    def enterAssignFunction(self, ctx:mParser.AssignFunctionContext):
        pass

    # Exit a parse tree produced by mParser#AssignFunction.
    def exitAssignFunction(self, ctx:mParser.AssignFunctionContext):
        pass


    # Enter a parse tree produced by mParser#functions.
    def enterFunctions(self, ctx:mParser.FunctionsContext):
        pass

    # Exit a parse tree produced by mParser#functions.
    def exitFunctions(self, ctx:mParser.FunctionsContext):
        pass


    # Enter a parse tree produced by mParser#operation.
    def enterOperation(self, ctx:mParser.OperationContext):
        pass

    # Exit a parse tree produced by mParser#operation.
    def exitOperation(self, ctx:mParser.OperationContext):
        pass


    # Enter a parse tree produced by mParser#opera.
    def enterOpera(self, ctx:mParser.OperaContext):
        pass

    # Exit a parse tree produced by mParser#opera.
    def exitOpera(self, ctx:mParser.OperaContext):
        pass


    # Enter a parse tree produced by mParser#NumberExpr.
    def enterNumberExpr(self, ctx:mParser.NumberExprContext):
        pass

    # Exit a parse tree produced by mParser#NumberExpr.
    def exitNumberExpr(self, ctx:mParser.NumberExprContext):
        pass


    # Enter a parse tree produced by mParser#VariableExpr.
    def enterVariableExpr(self, ctx:mParser.VariableExprContext):
        pass

    # Exit a parse tree produced by mParser#VariableExpr.
    def exitVariableExpr(self, ctx:mParser.VariableExprContext):
        pass


    # Enter a parse tree produced by mParser#ParenExpr.
    def enterParenExpr(self, ctx:mParser.ParenExprContext):
        pass

    # Exit a parse tree produced by mParser#ParenExpr.
    def exitParenExpr(self, ctx:mParser.ParenExprContext):
        pass


    # Enter a parse tree produced by mParser#InfixExpr.
    def enterInfixExpr(self, ctx:mParser.InfixExprContext):
        pass

    # Exit a parse tree produced by mParser#InfixExpr.
    def exitInfixExpr(self, ctx:mParser.InfixExprContext):
        pass


    # Enter a parse tree produced by mParser#DefineVar.
    def enterDefineVar(self, ctx:mParser.DefineVarContext):
        pass

    # Exit a parse tree produced by mParser#DefineVar.
    def exitDefineVar(self, ctx:mParser.DefineVarContext):
        pass


    # Enter a parse tree produced by mParser#typeSpecifier.
    def enterTypeSpecifier(self, ctx:mParser.TypeSpecifierContext):
        pass

    # Exit a parse tree produced by mParser#typeSpecifier.
    def exitTypeSpecifier(self, ctx:mParser.TypeSpecifierContext):
        pass


    # Enter a parse tree produced by mParser#compoundStatement.
    def enterCompoundStatement(self, ctx:mParser.CompoundStatementContext):
        pass

    # Exit a parse tree produced by mParser#compoundStatement.
    def exitCompoundStatement(self, ctx:mParser.CompoundStatementContext):
        pass


    # Enter a parse tree produced by mParser#param.
    def enterParam(self, ctx:mParser.ParamContext):
        pass

    # Exit a parse tree produced by mParser#param.
    def exitParam(self, ctx:mParser.ParamContext):
        pass


    # Enter a parse tree produced by mParser#returnStatement.
    def enterReturnStatement(self, ctx:mParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by mParser#returnStatement.
    def exitReturnStatement(self, ctx:mParser.ReturnStatementContext):
        pass


    # Enter a parse tree produced by mParser#paramList.
    def enterParamList(self, ctx:mParser.ParamListContext):
        pass

    # Exit a parse tree produced by mParser#paramList.
    def exitParamList(self, ctx:mParser.ParamListContext):
        pass


    # Enter a parse tree produced by mParser#callParam.
    def enterCallParam(self, ctx:mParser.CallParamContext):
        pass

    # Exit a parse tree produced by mParser#callParam.
    def exitCallParam(self, ctx:mParser.CallParamContext):
        pass


    # Enter a parse tree produced by mParser#callParamList.
    def enterCallParamList(self, ctx:mParser.CallParamListContext):
        pass

    # Exit a parse tree produced by mParser#callParamList.
    def exitCallParamList(self, ctx:mParser.CallParamListContext):
        pass


    # Enter a parse tree produced by mParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:mParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by mParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:mParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by mParser#functionCall.
    def enterFunctionCall(self, ctx:mParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by mParser#functionCall.
    def exitFunctionCall(self, ctx:mParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by mParser#macroDefinition.
    def enterMacroDefinition(self, ctx:mParser.MacroDefinitionContext):
        pass

    # Exit a parse tree produced by mParser#macroDefinition.
    def exitMacroDefinition(self, ctx:mParser.MacroDefinitionContext):
        pass


    # Enter a parse tree produced by mParser#include.
    def enterInclude(self, ctx:mParser.IncludeContext):
        pass

    # Exit a parse tree produced by mParser#include.
    def exitInclude(self, ctx:mParser.IncludeContext):
        pass


    # Enter a parse tree produced by mParser#macroParamList.
    def enterMacroParamList(self, ctx:mParser.MacroParamListContext):
        pass

    # Exit a parse tree produced by mParser#macroParamList.
    def exitMacroParamList(self, ctx:mParser.MacroParamListContext):
        pass


    # Enter a parse tree produced by mParser#macroParam.
    def enterMacroParam(self, ctx:mParser.MacroParamContext):
        pass

    # Exit a parse tree produced by mParser#macroParam.
    def exitMacroParam(self, ctx:mParser.MacroParamContext):
        pass


    # Enter a parse tree produced by mParser#macroCall.
    def enterMacroCall(self, ctx:mParser.MacroCallContext):
        pass

    # Exit a parse tree produced by mParser#macroCall.
    def exitMacroCall(self, ctx:mParser.MacroCallContext):
        pass


    # Enter a parse tree produced by mParser#macroCallParam.
    def enterMacroCallParam(self, ctx:mParser.MacroCallParamContext):
        pass

    # Exit a parse tree produced by mParser#macroCallParam.
    def exitMacroCallParam(self, ctx:mParser.MacroCallParamContext):
        pass


    # Enter a parse tree produced by mParser#macroCallParamList.
    def enterMacroCallParamList(self, ctx:mParser.MacroCallParamListContext):
        pass

    # Exit a parse tree produced by mParser#macroCallParamList.
    def exitMacroCallParamList(self, ctx:mParser.MacroCallParamListContext):
        pass



del mParser