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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\24")
        buf.write("o\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\3\2\6\2\36\n\2\r\2\16\2\37\3\3\3\3\3\3\3\3\3\3\3\3")
        buf.write("\3\3\3\3\5\3*\n\3\3\4\3\4\3\5\3\5\3\5\3\6\3\6\3\6\5\6")
        buf.write("\64\n\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\5\7=\n\7\3\7\3\7\3")
        buf.write("\7\3\7\3\7\3\7\7\7E\n\7\f\7\16\7H\13\7\3\b\3\b\3\b\3\t")
        buf.write("\3\t\3\n\3\n\7\nQ\n\n\f\n\16\nT\13\n\3\n\3\n\3\13\3\13")
        buf.write("\3\13\3\f\3\f\3\f\3\r\3\r\3\r\7\ra\n\r\f\r\16\rd\13\r")
        buf.write("\3\16\3\16\3\16\3\16\5\16j\n\16\3\16\3\16\3\16\3\16\2")
        buf.write("\3\f\17\2\4\6\b\n\f\16\20\22\24\26\30\32\2\4\3\2\5\6\3")
        buf.write("\2\7\b\2l\2\35\3\2\2\2\4)\3\2\2\2\6+\3\2\2\2\b-\3\2\2")
        buf.write("\2\n\63\3\2\2\2\f<\3\2\2\2\16I\3\2\2\2\20L\3\2\2\2\22")
        buf.write("N\3\2\2\2\24W\3\2\2\2\26Z\3\2\2\2\30]\3\2\2\2\32e\3\2")
        buf.write("\2\2\34\36\5\6\4\2\35\34\3\2\2\2\36\37\3\2\2\2\37\35\3")
        buf.write("\2\2\2\37 \3\2\2\2 \3\3\2\2\2!\"\5\20\t\2\"#\7\24\2\2")
        buf.write("#$\7\3\2\2$%\5\f\7\2%*\3\2\2\2&\'\7\24\2\2\'(\7\3\2\2")
        buf.write("(*\5\f\7\2)!\3\2\2\2)&\3\2\2\2*\5\3\2\2\2+,\5\32\16\2")
        buf.write(",\7\3\2\2\2-.\5\n\6\2./\7\4\2\2/\t\3\2\2\2\60\64\5\4\3")
        buf.write("\2\61\64\5\16\b\2\62\64\5\26\f\2\63\60\3\2\2\2\63\61\3")
        buf.write("\2\2\2\63\62\3\2\2\2\64\13\3\2\2\2\65\66\b\7\1\2\66=\7")
        buf.write("\20\2\2\678\7\t\2\289\5\f\7\29:\7\n\2\2:=\3\2\2\2;=\7")
        buf.write("\24\2\2<\65\3\2\2\2<\67\3\2\2\2<;\3\2\2\2=F\3\2\2\2>?")
        buf.write("\f\7\2\2?@\t\2\2\2@E\5\f\7\bAB\f\6\2\2BC\t\3\2\2CE\5\f")
        buf.write("\7\7D>\3\2\2\2DA\3\2\2\2EH\3\2\2\2FD\3\2\2\2FG\3\2\2\2")
        buf.write("G\r\3\2\2\2HF\3\2\2\2IJ\5\20\t\2JK\7\24\2\2K\17\3\2\2")
        buf.write("\2LM\7\13\2\2M\21\3\2\2\2NR\7\f\2\2OQ\5\b\5\2PO\3\2\2")
        buf.write("\2QT\3\2\2\2RP\3\2\2\2RS\3\2\2\2SU\3\2\2\2TR\3\2\2\2U")
        buf.write("V\7\r\2\2V\23\3\2\2\2WX\5\20\t\2XY\7\24\2\2Y\25\3\2\2")
        buf.write("\2Z[\7\16\2\2[\\\7\24\2\2\\\27\3\2\2\2]b\5\24\13\2^_\7")
        buf.write("\17\2\2_a\5\24\13\2`^\3\2\2\2ad\3\2\2\2b`\3\2\2\2bc\3")
        buf.write("\2\2\2c\31\3\2\2\2db\3\2\2\2ef\5\20\t\2fg\7\24\2\2gi\7")
        buf.write("\t\2\2hj\5\30\r\2ih\3\2\2\2ij\3\2\2\2jk\3\2\2\2kl\7\n")
        buf.write("\2\2lm\5\22\n\2m\33\3\2\2\2\13\37)\63<DFRbi")
        return buf.getvalue()


class mParser ( Parser ):

    grammarFileName = "m.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "';'", "'*'", "'/'", "'+'", "'-'", 
                     "'('", "')'", "'int'", "'{'", "'}'", "'return'", "','" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "INT", "STRING", "WS", "Newline", 
                      "WORD" ]

    RULE_main = 0
    RULE_assignVariable = 1
    RULE_functions = 2
    RULE_operation = 3
    RULE_opera = 4
    RULE_expr = 5
    RULE_defineVariable = 6
    RULE_typeSpecifier = 7
    RULE_compoundStatement = 8
    RULE_param = 9
    RULE_returnStatement = 10
    RULE_paramList = 11
    RULE_functionDefinition = 12

    ruleNames =  [ "main", "assignVariable", "functions", "operation", "opera", 
                   "expr", "defineVariable", "typeSpecifier", "compoundStatement", 
                   "param", "returnStatement", "paramList", "functionDefinition" ]

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
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    INT=14
    STRING=15
    WS=16
    Newline=17
    WORD=18

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

        def functions(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mParser.FunctionsContext)
            else:
                return self.getTypedRuleContext(mParser.FunctionsContext,i)


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
            self.state = 27 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 26
                self.functions()
                self.state = 29 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==mParser.T__8):
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
            self.state = 39
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [mParser.T__8]:
                localctx = mParser.AssignExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                localctx.type = self.typeSpecifier()
                self.state = 32
                localctx.name = self.match(mParser.WORD)
                self.state = 33
                self.match(mParser.T__0)
                self.state = 34
                localctx.value = self.expr(0)
                pass
            elif token in [mParser.WORD]:
                localctx = mParser.AssignVarContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                localctx.name = self.match(mParser.WORD)
                self.state = 37
                self.match(mParser.T__0)
                self.state = 38
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


    class FunctionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def functionDefinition(self):
            return self.getTypedRuleContext(mParser.FunctionDefinitionContext,0)


        def getRuleIndex(self):
            return mParser.RULE_functions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctions" ):
                listener.enterFunctions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctions" ):
                listener.exitFunctions(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctions" ):
                return visitor.visitFunctions(self)
            else:
                return visitor.visitChildren(self)




    def functions(self):

        localctx = mParser.FunctionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_functions)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.functionDefinition()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperationContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def opera(self):
            return self.getTypedRuleContext(mParser.OperaContext,0)


        def getRuleIndex(self):
            return mParser.RULE_operation

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOperation" ):
                listener.enterOperation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOperation" ):
                listener.exitOperation(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitOperation" ):
                return visitor.visitOperation(self)
            else:
                return visitor.visitChildren(self)




    def operation(self):

        localctx = mParser.OperationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_operation)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self.opera()
            self.state = 44
            self.match(mParser.T__1)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class OperaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return mParser.RULE_opera

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class SegDefineContext(OperaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mParser.OperaContext
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


    class RetStatementContext(OperaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mParser.OperaContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def returnStatement(self):
            return self.getTypedRuleContext(mParser.ReturnStatementContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRetStatement" ):
                listener.enterRetStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRetStatement" ):
                listener.exitRetStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRetStatement" ):
                return visitor.visitRetStatement(self)
            else:
                return visitor.visitChildren(self)


    class SegAssignContext(OperaContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a mParser.OperaContext
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



    def opera(self):

        localctx = mParser.OperaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_opera)
        try:
            self.state = 49
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = mParser.SegAssignContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.assignVariable()
                pass

            elif la_ == 2:
                localctx = mParser.SegDefineContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.defineVariable()
                pass

            elif la_ == 3:
                localctx = mParser.RetStatementContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 48
                self.returnStatement()
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
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 58
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [mParser.INT]:
                localctx = mParser.NumberExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 52
                localctx.atom = self.match(mParser.INT)
                pass
            elif token in [mParser.T__6]:
                localctx = mParser.ParenExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 53
                self.match(mParser.T__6)
                self.state = 54
                self.expr(0)
                self.state = 55
                self.match(mParser.T__7)
                pass
            elif token in [mParser.WORD]:
                localctx = mParser.VariableExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 57
                localctx.atom = self.match(mParser.WORD)
                pass
            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 68
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,5,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 66
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
                    if la_ == 1:
                        localctx = mParser.InfixExprContext(self, mParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 60
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 61
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==mParser.T__2 or _la==mParser.T__3):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 62
                        localctx.right = self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = mParser.InfixExprContext(self, mParser.ExprContext(self, _parentctx, _parentState))
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 63
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 64
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==mParser.T__4 or _la==mParser.T__5):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 65
                        localctx.right = self.expr(5)
                        pass

             
                self.state = 70
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
        self.enterRule(localctx, 12, self.RULE_defineVariable)
        try:
            localctx = mParser.DefineVarContext(self, localctx)
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            localctx.type = self.typeSpecifier()
            self.state = 72
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
        self.enterRule(localctx, 14, self.RULE_typeSpecifier)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 74
            self.match(mParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompoundStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def operation(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mParser.OperationContext)
            else:
                return self.getTypedRuleContext(mParser.OperationContext,i)


        def getRuleIndex(self):
            return mParser.RULE_compoundStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompoundStatement" ):
                listener.enterCompoundStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompoundStatement" ):
                listener.exitCompoundStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompoundStatement" ):
                return visitor.visitCompoundStatement(self)
            else:
                return visitor.visitChildren(self)




    def compoundStatement(self):

        localctx = mParser.CompoundStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_compoundStatement)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(mParser.T__9)
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << mParser.T__8) | (1 << mParser.T__11) | (1 << mParser.WORD))) != 0):
                self.state = 77
                self.operation()
                self.state = 82
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 83
            self.match(mParser.T__10)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.type = None # TypeSpecifierContext
            self.name = None # Token

        def typeSpecifier(self):
            return self.getTypedRuleContext(mParser.TypeSpecifierContext,0)


        def WORD(self):
            return self.getToken(mParser.WORD, 0)

        def getRuleIndex(self):
            return mParser.RULE_param

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParam" ):
                listener.enterParam(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParam" ):
                listener.exitParam(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParam" ):
                return visitor.visitParam(self)
            else:
                return visitor.visitChildren(self)




    def param(self):

        localctx = mParser.ParamContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_param)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            localctx.type = self.typeSpecifier()
            self.state = 86
            localctx.name = self.match(mParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token

        def WORD(self):
            return self.getToken(mParser.WORD, 0)

        def getRuleIndex(self):
            return mParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = mParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(mParser.T__11)
            self.state = 89
            localctx.name = self.match(mParser.WORD)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParamListContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def param(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(mParser.ParamContext)
            else:
                return self.getTypedRuleContext(mParser.ParamContext,i)


        def getRuleIndex(self):
            return mParser.RULE_paramList

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParamList" ):
                listener.enterParamList(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParamList" ):
                listener.exitParamList(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParamList" ):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = mParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 91
            self.param()
            self.state = 96
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==mParser.T__12:
                self.state = 92
                self.match(mParser.T__12)
                self.state = 93
                self.param()
                self.state = 98
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser
            self.name = None # Token

        def typeSpecifier(self):
            return self.getTypedRuleContext(mParser.TypeSpecifierContext,0)


        def compoundStatement(self):
            return self.getTypedRuleContext(mParser.CompoundStatementContext,0)


        def WORD(self):
            return self.getToken(mParser.WORD, 0)

        def paramList(self):
            return self.getTypedRuleContext(mParser.ParamListContext,0)


        def getRuleIndex(self):
            return mParser.RULE_functionDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDefinition" ):
                listener.enterFunctionDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDefinition" ):
                listener.exitFunctionDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDefinition" ):
                return visitor.visitFunctionDefinition(self)
            else:
                return visitor.visitChildren(self)




    def functionDefinition(self):

        localctx = mParser.FunctionDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_functionDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.typeSpecifier()
            self.state = 100
            localctx.name = self.match(mParser.WORD)
            self.state = 101
            self.match(mParser.T__6)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==mParser.T__8:
                self.state = 102
                self.paramList()


            self.state = 105
            self.match(mParser.T__7)
            self.state = 106
            self.compoundStatement()
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
        self._predicates[5] = self.expr_sempred
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
         




