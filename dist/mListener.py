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


    # Enter a parse tree produced by mParser#statement.
    def enterStatement(self, ctx:mParser.StatementContext):
        pass

    # Exit a parse tree produced by mParser#statement.
    def exitStatement(self, ctx:mParser.StatementContext):
        pass


    # Enter a parse tree produced by mParser#condition.
    def enterCondition(self, ctx:mParser.ConditionContext):
        pass

    # Exit a parse tree produced by mParser#condition.
    def exitCondition(self, ctx:mParser.ConditionContext):
        pass


    # Enter a parse tree produced by mParser#selectionStatement.
    def enterSelectionStatement(self, ctx:mParser.SelectionStatementContext):
        pass

    # Exit a parse tree produced by mParser#selectionStatement.
    def exitSelectionStatement(self, ctx:mParser.SelectionStatementContext):
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


    # Enter a parse tree produced by mParser#elseString.
    def enterElseString(self, ctx:mParser.ElseStringContext):
        pass

    # Exit a parse tree produced by mParser#elseString.
    def exitElseString(self, ctx:mParser.ElseStringContext):
        pass



del mParser