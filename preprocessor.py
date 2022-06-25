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

        #For debuging
        #Macros[name] += name + "('text', 1)"
        #print(MacroCode)

    def exitMacroDefinition(self, ctx:mParser.MacroDefinitionContext):
        global NewCode

        token_source = ctx.start.getTokenSource()
        input_stream = token_source.inputStream
        start, stop  = ctx.start.start, ctx.stop.stop
        

        name = str(ctx.getChild(1))
        exec(Macros[name])
        #print(input_stream.getText(start, stop))
        NewCode = NewCode.replace(input_stream.getText(start, stop), "")

    def enterMacroCall(self, ctx:mParser.MacroCallContext):
        global NewCode
        visitor = MyVisitor()

        token_source = ctx.start.getTokenSource()
        input_stream = token_source.inputStream
        start, stop  = ctx.start.start, ctx.stop.stop

        name = str(ctx.getChild(1))
        params = visitor.visit(ctx.getChild(3))

        call = name + "("+ params +")"

        #print(Macros[name])
        #print("Result = " + call)

        #This code is very bad
        global Result
        Result = ""
        exec(Macros[name] + "global Result \nResult = " + call)

        #print("Result: " +Result)

        NewCode = NewCode.replace(input_stream.getText(start, stop), Result)


class MyVisitor(mVisitor):
    def visitMacroParamList(self, ctx:mParser.ParamListContext):
        return str(ctx.getText())

    def visitMacroCallParamList(self, ctx:mParser.ParamListContext):
        return str(ctx.getText())
        visitor = MyVisitor()
        ParamList = ""
        for i in ctx.getChildCount():
            param = visitor.visit(ctx.getChild(i))
            if param != None:
                ParamList += param
        #return ParamList
        #return self.visitChildren(ctx)

    def visitMacroCallParam(self, ctx:mParser.MacroCallParamContext):
        try:
            return ctx.getText()
        except ValueError:
            return '"'+ ctx.getText() +'"'

def extract_original_text(self, ctx):
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


    new = ""
    for line in code.splitlines():

        lineList = line.split()

        if len(lineList) > 1 and lineList[0] == "#include":
            #print(lineList)
            line = open(lineList[1][1:-1]).read()
        new += line + "\n"
    #print(new)
    return NewCode