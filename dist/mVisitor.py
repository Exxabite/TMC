# Generated from m.g4 by ANTLR 4.9.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .mParser import mParser
else:
    from mParser import mParser

# This class defines a complete generic visitor for a parse tree produced by mParser.

class mVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by mParser#MainExp.
    def visitMainExp(self, ctx:mParser.MainExpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mParser#AssignExpr.
    def visitAssignExpr(self, ctx:mParser.AssignExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mParser#AssignVar.
    def visitAssignVar(self, ctx:mParser.AssignVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mParser#AssignFunction.
    def visitAssignFunction(self, ctx:mParser.AssignFunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mParser#functions.
    def visitFunctions(self, ctx:mParser.FunctionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mParser#operation.
    def visitOperation(self, ctx:mParser.OperationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mParser#opera.
    def visitOpera(self, ctx:mParser.OperaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mParser#NumberExpr.
    def visitNumberExpr(self, ctx:mParser.NumberExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mParser#VariableExpr.
    def visitVariableExpr(self, ctx:mParser.VariableExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mParser#ParenExpr.
    def visitParenExpr(self, ctx:mParser.ParenExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mParser#InfixExpr.
    def visitInfixExpr(self, ctx:mParser.InfixExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mParser#DefineVar.
    def visitDefineVar(self, ctx:mParser.DefineVarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mParser#typeSpecifier.
    def visitTypeSpecifier(self, ctx:mParser.TypeSpecifierContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mParser#statement.
    def visitStatement(self, ctx:mParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mParser#condition.
    def visitCondition(self, ctx:mParser.ConditionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mParser#selectionStatement.
    def visitSelectionStatement(self, ctx:mParser.SelectionStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mParser#compoundStatement.
    def visitCompoundStatement(self, ctx:mParser.CompoundStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mParser#param.
    def visitParam(self, ctx:mParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mParser#returnStatement.
    def visitReturnStatement(self, ctx:mParser.ReturnStatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mParser#paramList.
    def visitParamList(self, ctx:mParser.ParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mParser#callParam.
    def visitCallParam(self, ctx:mParser.CallParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mParser#callParamList.
    def visitCallParamList(self, ctx:mParser.CallParamListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mParser#functionDefinition.
    def visitFunctionDefinition(self, ctx:mParser.FunctionDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mParser#functionCall.
    def visitFunctionCall(self, ctx:mParser.FunctionCallContext):
        return self.visitChildren(ctx)



del mParser