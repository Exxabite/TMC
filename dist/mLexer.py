# Generated from m.g4 by ANTLR 4.9.3
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\20")
        buf.write("V\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\3\2\3\2\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3")
        buf.write("\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3\n\3\n\3\13\6\13\65")
        buf.write("\n\13\r\13\16\13\66\3\f\3\f\7\f;\n\f\f\f\16\f>\13\f\3")
        buf.write("\f\3\f\3\r\6\rC\n\r\r\r\16\rD\3\r\3\r\3\16\3\16\5\16K")
        buf.write("\n\16\3\16\5\16N\n\16\3\16\3\16\3\17\6\17S\n\17\r\17\16")
        buf.write("\17T\3<\2\20\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13")
        buf.write("\25\f\27\r\31\16\33\17\35\20\3\2\5\3\2\62;\4\2\13\13\"")
        buf.write("\"\5\2C\\aac|\2[\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2")
        buf.write("\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21")
        buf.write("\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3")
        buf.write("\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\3\37\3\2\2\2\5!\3\2\2")
        buf.write("\2\7#\3\2\2\2\t%\3\2\2\2\13\'\3\2\2\2\r)\3\2\2\2\17+\3")
        buf.write("\2\2\2\21-\3\2\2\2\23/\3\2\2\2\25\64\3\2\2\2\278\3\2\2")
        buf.write("\2\31B\3\2\2\2\33M\3\2\2\2\35R\3\2\2\2\37 \7=\2\2 \4\3")
        buf.write("\2\2\2!\"\7?\2\2\"\6\3\2\2\2#$\7,\2\2$\b\3\2\2\2%&\7\61")
        buf.write("\2\2&\n\3\2\2\2\'(\7-\2\2(\f\3\2\2\2)*\7/\2\2*\16\3\2")
        buf.write("\2\2+,\7*\2\2,\20\3\2\2\2-.\7+\2\2.\22\3\2\2\2/\60\7k")
        buf.write("\2\2\60\61\7p\2\2\61\62\7v\2\2\62\24\3\2\2\2\63\65\t\2")
        buf.write("\2\2\64\63\3\2\2\2\65\66\3\2\2\2\66\64\3\2\2\2\66\67\3")
        buf.write("\2\2\2\67\26\3\2\2\28<\7$\2\29;\13\2\2\2:9\3\2\2\2;>\3")
        buf.write("\2\2\2<=\3\2\2\2<:\3\2\2\2=?\3\2\2\2><\3\2\2\2?@\7$\2")
        buf.write("\2@\30\3\2\2\2AC\t\3\2\2BA\3\2\2\2CD\3\2\2\2DB\3\2\2\2")
        buf.write("DE\3\2\2\2EF\3\2\2\2FG\b\r\2\2G\32\3\2\2\2HJ\7\17\2\2")
        buf.write("IK\7\f\2\2JI\3\2\2\2JK\3\2\2\2KN\3\2\2\2LN\7\f\2\2MH\3")
        buf.write("\2\2\2ML\3\2\2\2NO\3\2\2\2OP\b\16\2\2P\34\3\2\2\2QS\t")
        buf.write("\4\2\2RQ\3\2\2\2ST\3\2\2\2TR\3\2\2\2TU\3\2\2\2U\36\3\2")
        buf.write("\2\2\t\2\66<DJMT\3\b\2\2")
        return buf.getvalue()


class mLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    INT = 10
    STRING = 11
    WS = 12
    Newline = 13
    WORD = 14

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "';'", "'='", "'*'", "'/'", "'+'", "'-'", "'('", "')'", "'int'" ]

    symbolicNames = [ "<INVALID>",
            "INT", "STRING", "WS", "Newline", "WORD" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "INT", "STRING", "WS", "Newline", "WORD" ]

    grammarFileName = "m.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.3")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


