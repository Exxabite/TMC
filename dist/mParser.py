# Generated from m.g4 by ANTLR 4.9.3
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\20")
        buf.write("=\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\3\2")
        buf.write("\3\2\3\2\6\2\22\n\2\r\2\16\2\23\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\3\5\3\36\n\3\3\4\3\4\5\4\"\n\4\3\5\3\5\3\5\3")
        buf.write("\5\3\5\3\5\3\5\5\5+\n\5\3\5\3\5\3\5\3\5\3\5\3\5\7\5\63")
        buf.write("\n\5\f\5\16\5\66\13\5\3\6\3\6\3\6\3\7\3\7\3\7\2\3\b\b")
        buf.write("\2\4\6\b\n\f\2\4\3\2\5\6\3\2\7\b\2=\2\21\3\2\2\2\4\35")
        buf.write("\3\2\2\2\6!\3\2\2\2\b*\3\2\2\2\n\67\3\2\2\2\f:\3\2\2\2")
        buf.write("\16\17\5\6\4\2\17\20\7\3\2\2\20\22\3\2\2\2\21\16\3\2\2")
        buf.write("\2\22\23\3\2\2\2\23\21\3\2\2\2\23\24\3\2\2\2\24\3\3\2")
        buf.write("\2\2\25\26\5\f\7\2\26\27\7\20\2\2\27\30\7\4\2\2\30\31")
        buf.write("\5\b\5\2\31\36\3\2\2\2\32\33\7\20\2\2\33\34\7\4\2\2\34")
        buf.write("\36\5\b\5\2\35\25\3\2\2\2\35\32\3\2\2\2\36\5\3\2\2\2\37")
        buf.write("\"\5\4\3\2 \"\5\n\6\2!\37\3\2\2\2! \3\2\2\2\"\7\3\2\2")
        buf.write("\2#$\b\5\1\2$+\7\f\2\2%&\7\t\2\2&\'\5\b\5\2\'(\7\n\2\2")
        buf.write("(+\3\2\2\2)+\7\20\2\2*#\3\2\2\2*%\3\2\2\2*)\3\2\2\2+\64")
        buf.write("\3\2\2\2,-\f\7\2\2-.\t\2\2\2.\63\5\b\5\b/\60\f\6\2\2\60")
        buf.write("\61\t\3\2\2\61\63\5\b\5\7\62,\3\2\2\2\62/\3\2\2\2\63\66")
        buf.write("\3\2\2\2\64\62\3\2\2\2\64\65\3\2\2\2\65\t\3\2\2\2\66\64")
        buf.write("\3\2\2\2\678\5\f\7\289\7\20\2\29\13\3\2\2\2:;\7\13\2\2")
        buf.write(";\r\3\2\2\2\b\23\35!*\62\64")
        return buf.getvalue()


class mParser ( Parser ):

    grammarFileName = "m.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'='", "'*'", "'/'", "'+'", "'-'", 
                     "'('", "')'", "'int'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "INT", "STRING", "WS", "Newline", 
                      "WORD" ]

    RULE_main = 0
    RULE_assignVariable = 1
    RULE_segment = 2
    RULE_expr = 3
    RULE_defineVariable = 4
    RULE_typeSpecifier = 5

    ruleNames =  [ "main", "assignVariable", "segment", "expr", "defineVariable", 
                   "typeSpecifier" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    INT=10
    STRING=11
    WS=12
    Newline=13
    WORD=14

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class MainContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return mParser.RULE_main

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class MainExpContext(MainContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mParser.MainContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def segment(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mParser.SegmentContext)
            else:
                return self.getTypedRuleContext(mParser.SegmentContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMainExp" ):
                listener.enterMainExp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMainExp" ):
                listener.exitMainExp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMainExp" ):
                return visitor.visitMainExp(self)
            else:
                return visitor.visitChildren(self)



    def main(self):

        localctx = mParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_main)
        self._la = 0 # Token type
        try:
            localctx = mParser.MainExpContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 15 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 12
                self.segment()
                self.state = 13
                self.match(mParser.T__0)
                self.state = 17 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==mParser.T__8 or _la==mParser.WORD):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignVariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return mParser.RULE_assignVariable

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AssignVarContext(AssignVariableContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mParser.AssignVariableContext
            super().__init__(parser)
            self.name = None # Token
            self.value = None # ExprContext
            self.copyFrom(ctx)

        def WORD(self):
            return self.getToken(mParser.WORD, 0)
        def expr(self):
            return self.getTypedRuleContext(mParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignVar" ):
                listener.enterAssignVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignVar" ):
                listener.exitAssignVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignVar" ):
                return visitor.visitAssignVar(self)
            else:
                return visitor.visitChildren(self)


    class AssignExprContext(AssignVariableContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mParser.AssignVariableContext
            super().__init__(parser)
            self.type = None # TypeSpecifierContext
            self.name = None # Token
            self.value = None # ExprContext
            self.copyFrom(ctx)

        def typeSpecifier(self):
            return self.getTypedRuleContext(mParser.TypeSpecifierContext,0)

        def WORD(self):
            return self.getToken(mParser.WORD, 0)
        def expr(self):
            return self.getTypedRuleContext(mParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignExpr" ):
                listener.enterAssignExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignExpr" ):
                listener.exitAssignExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignExpr" ):
                return visitor.visitAssignExpr(self)
            else:
                return visitor.visitChildren(self)



    def assignVariable(self):

        localctx = mParser.AssignVariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_assignVariable)
        try:
            self.state = 27
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [mParser.T__8]:
                localctx = mParser.AssignExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 19
                localctx.type = self.typeSpecifier()
                self.state = 20
                localctx.name = self.match(mParser.WORD)
                self.state = 21
                self.match(mParser.T__1)
                self.state = 22
                localctx.value = self.expr(0)
                pass
            elif token in [mParser.WORD]:
                localctx = mParser.AssignVarContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 24
                localctx.name = self.match(mParser.WORD)
                self.state = 25
                self.match(mParser.T__1)
                self.state = 26
                localctx.value = self.expr(0)
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SegmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return mParser.RULE_segment

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SegDefineContext(SegmentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mParser.SegmentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def defineVariable(self):
            return self.getTypedRuleContext(mParser.DefineVariableContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSegDefine" ):
                listener.enterSegDefine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSegDefine" ):
                listener.exitSegDefine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSegDefine" ):
                return visitor.visitSegDefine(self)
            else:
                return visitor.visitChildren(self)


    class SegAssignContext(SegmentContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mParser.SegmentContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def assignVariable(self):
            return self.getTypedRuleContext(mParser.AssignVariableContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSegAssign" ):
                listener.enterSegAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSegAssign" ):
                listener.exitSegAssign(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSegAssign" ):
                return visitor.visitSegAssign(self)
            else:
                return visitor.visitChildren(self)



    def segment(self):

        localctx = mParser.SegmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_segment)
        try:
            self.state = 31
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = mParser.SegAssignContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 29
                self.assignVariable()
                pass

            elif la_ == 2:
                localctx = mParser.SegDefineContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 30
                self.defineVariable()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return mParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class NumberExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mParser.ExprContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(mParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNumberExpr" ):
                listener.enterNumberExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNumberExpr" ):
                listener.exitNumberExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNumberExpr" ):
                return visitor.visitNumberExpr(self)
            else:
                return visitor.visitChildren(self)


    class VariableExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mParser.ExprContext
            super().__init__(parser)
            self.atom = None # Token
            self.copyFrom(ctx)

        def WORD(self):
            return self.getToken(mParser.WORD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVariableExpr" ):
                listener.enterVariableExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVariableExpr" ):
                listener.exitVariableExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitVariableExpr" ):
                return visitor.visitVariableExpr(self)
            else:
                return visitor.visitChildren(self)


    class ParenExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(mParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenExpr" ):
                listener.enterParenExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenExpr" ):
                listener.exitParenExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenExpr" ):
                return visitor.visitParenExpr(self)
            else:
                return visitor.visitChildren(self)


    class InfixExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mParser.ExprContext
            super().__init__(parser)
            self.left = None # ExprContext
            self.op = None # Token
            self.right = None # ExprContext
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mParser.ExprContext)
            else:
                return self.getTypedRuleContext(mParser.ExprContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInfixExpr" ):
                listener.enterInfixExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInfixExpr" ):
                listener.exitInfixExpr(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitInfixExpr" ):
                return visitor.visitInfixExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = mParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 6
        self.enterRecursionRule(localctx, 6, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 40
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [mParser.INT]:
                localctx = mParser.NumberExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 34
                localctx.atom = self.match(mParser.INT)
                pass
            elif token in [mParser.T__6]:
                localctx = mParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 35
                self.match(mParser.T__6)
                self.state = 36
                self.expr(0)
                self.state = 37
                self.match(mParser.T__7)
                pass
            elif token in [mParser.WORD]:
                localctx = mParser.VariableExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 39
                localctx.atom = self.match(mParser.WORD)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 50
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 48
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = mParser.InfixExprContext(self, mParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 42
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 43
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==mParser.T__2 or _la==mParser.T__3):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 44
                        localctx.right = self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = mParser.InfixExprContext(self, mParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 45
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 46
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==mParser.T__4 or _la==mParser.T__5):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 47
                        localctx.right = self.expr(5)
                        pass

             
                self.state = 52
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,5,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class DefineVariableContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return mParser.RULE_defineVariable

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DefineVarContext(DefineVariableContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mParser.DefineVariableContext
            super().__init__(parser)
            self.type = None # TypeSpecifierContext
            self.name = None # Token
            self.copyFrom(ctx)

        def typeSpecifier(self):
            return self.getTypedRuleContext(mParser.TypeSpecifierContext,0)

        def WORD(self):
            return self.getToken(mParser.WORD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDefineVar" ):
                listener.enterDefineVar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDefineVar" ):
                listener.exitDefineVar(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDefineVar" ):
                return visitor.visitDefineVar(self)
            else:
                return visitor.visitChildren(self)



    def defineVariable(self):

        localctx = mParser.DefineVariableContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_defineVariable)
        try:
            localctx = mParser.DefineVarContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            localctx.type = self.typeSpecifier()
            self.state = 54
            localctx.name = self.match(mParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TypeSpecifierContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return mParser.RULE_typeSpecifier

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTypeSpecifier" ):
                listener.enterTypeSpecifier(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTypeSpecifier" ):
                listener.exitTypeSpecifier(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTypeSpecifier" ):
                return visitor.visitTypeSpecifier(self)
            else:
                return visitor.visitChildren(self)




    def typeSpecifier(self):

        localctx = mParser.TypeSpecifierContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_typeSpecifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(mParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[3] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




