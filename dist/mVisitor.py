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


    # Visit a parse tree produced by mParser#SegAssign.
    def visitSegAssign(self, ctx:mParser.SegAssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mParser#SegDefine.
    def visitSegDefine(self, ctx:mParser.SegDefineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by mParser#NumberExpr.
    def visitNumberExpr(self, ctx:mParser.NumberExprContext):
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



del mParser