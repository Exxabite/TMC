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


    # Enter a parse tree produced by mParser#SegAssign.
    def enterSegAssign(self, ctx:mParser.SegAssignContext):
        pass

    # Exit a parse tree produced by mParser#SegAssign.
    def exitSegAssign(self, ctx:mParser.SegAssignContext):
        pass


    # Enter a parse tree produced by mParser#SegDefine.
    def enterSegDefine(self, ctx:mParser.SegDefineContext):
        pass

    # Exit a parse tree produced by mParser#SegDefine.
    def exitSegDefine(self, ctx:mParser.SegDefineContext):
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



del mParser