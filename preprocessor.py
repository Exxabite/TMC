from antlr4 import *
from dist.mLexer import mLexer
from dist.mParser import mParser
from dist.mVisitor import mVisitor

Macros = {}

class preprocessorListener(ParseTreeListener):
    def __init__(self, code):
        self.NewCode = code
   
    def enterMacroDefinition(self, ctx:mParser.MacroDefinitionContext):
        visitor = MyVisitor()
        global Macros
        name = str(ctx.getChild(1))
        params = visitor.visit(ctx.getChild(3))

        Macros[name] = "def " + name + "(" + params + ")" + ":\n"
        Macros[name] += str(ctx.getChild(5))[2:-2]

    def exitMacroDefinition(self, ctx:mParser.MacroDefinitionContext):

        name = str(ctx.getChild(1))
        exec(Macros[name])
        #print(input_stream.getText(start, stop))
        self.NewCode = self.NewCode.replace(extract_original_text(ctx), "")

    def enterMacroCall(self, ctx:mParser.MacroCallContext):
        visitor = MyVisitor()

        name = str(ctx.getChild(1))
        params = visitor.visit(ctx.getChild(3))

        call = name + "("+ params +")"

        #This code is very bad
        exec(Macros[name] + "global Result \nResult = " + call)

        self.NewCode = self.NewCode.replace(extract_original_text(ctx), Result)

    def enterInclude(self, ctx):
        name = str(ctx.getChild(1))
        text = open(name[1:-1]).read()
        self.NewCode = self.NewCode.replace(extract_original_text(ctx), preprocess(text))

class MyVisitor(mVisitor):
    def visitMacroParamList(self, ctx:mParser.ParamListContext):
        return str(ctx.getText())

    def visitMacroCallParam(self, ctx:mParser.MacroCallParamContext):
        try:
            return ctx.getText()
        except ValueError:
            return '"'+ ctx.getText() +'"'

def extract_original_text(ctx):
    token_source = ctx.start.getTokenSource()
    input_stream = token_source.inputStream
    start, stop  = ctx.start.start, ctx.stop.stop
    return input_stream.getText(start, stop)

def preprocess(code):

    data = InputStream(code)

    # lexer
    lexer = mLexer(data)
    stream = CommonTokenStream(lexer)
    # parser
    parser = mParser(stream)
    tree = parser.main()
    # evaluator
    visitor = MyVisitor()
    #ParseTreeListener()

    printer = preprocessorListener(code)
    walker = ParseTreeWalker()

    walker.walk(printer, tree)

    return printer.NewCode