from antlr4 import *
from dist.mLexer import mLexer
from dist.mParser import mParser
from dist.mVisitor import mVisitor

NewCode = ""

Macros = {}

class preprocessorListener(ParseTreeListener):
   
    def enterMacroDefinition(self, ctx:mParser.MacroDefinitionContext):
        visitor = MyVisitor()
        global MacroCode
        global Macros
        name = str(ctx.getChild(1))
        params = visitor.visit(ctx.getChild(3))

        Macros[name] = "def " + name + "(" + params + ")" + ":\n"
        Macros[name] += str(ctx.getChild(5))[2:-2]

    def exitMacroDefinition(self, ctx:mParser.MacroDefinitionContext):
        global NewCode

        name = str(ctx.getChild(1))
        exec(Macros[name])
        #print(input_stream.getText(start, stop))
        NewCode = NewCode.replace(extract_original_text(ctx), "")

    def enterMacroCall(self, ctx:mParser.MacroCallContext):
        global NewCode
        visitor = MyVisitor()

        name = str(ctx.getChild(1))
        params = visitor.visit(ctx.getChild(3))

        call = name + "("+ params +")"

        #This code is very bad
        exec(Macros[name] + "global Result \nResult = " + call)

        NewCode = NewCode.replace(extract_original_text(ctx), Result)

    def enterInclude(self, ctx:mParser.IncludeContext):
        global NewCode
        name = str(ctx.getChild(1))
        text = open(name[1:-1]).read()
        #Bad code
        temp = str(NewCode)
        NewCode = ""
        text = preprocess(text)
        NewCode = str(temp)

        NewCode = NewCode.replace(extract_original_text(ctx), text)

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

    global NewCode
    NewCode = code
    
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

    printer = preprocessorListener()
    walker = ParseTreeWalker()


    walker.walk(printer, tree)

    print(NewCode)

    return NewCode