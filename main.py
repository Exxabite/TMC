#from curses.ascii import isdigit
from ast import Assign
from multiprocessing.dummy.connection import Listener
from operator import contains
import string
import sys
from antlr4 import *
from dist.mLexer import mLexer
from dist.mParser import mParser
from dist.mVisitor import mVisitor


def get_username():
    from pwd import getpwuid
    from os import getuid
    return getpwuid(getuid())[ 0 ]

#int : 0
variables = {
    "default" : 0
}


class mListener(ParseTreeListener):
    def enterAssignExpr(self, ctx:mParser.AssignExprContext):
        visitor = MyVisitor()

        name = ctx.getChild(1)
        value = visitor.visit(ctx.value)

        variables[str(name)] = 0 #SAFTEY!

        if value.isdigit():
            out.write("mov " + str(name) + ", " + value + "\n")
        else:
            out.write(value + "mov " + str(name) + ", eax\n")

    def enterAssignVar(self, ctx:mParser.AssignExprContext):
        visitor = MyVisitor()

        name = str(ctx.getChild(0))
        value = visitor.visit(ctx.value)

        if name not in variables.keys():
            raise Exception(name + " is undefined")

        if not " " in value:
            out.write("mov " + name + ", " + value + "\n")
        else:
            out.write(value + "mov " + name + ", eax\n")

    def enterDefineVar(self, ctx:mParser.DefineVarContext):
        #Add saftey!!!
        name = str(ctx.getChild(1))
        variables[name] = 0

class MyVisitor(mVisitor):

    #def visitMainExp(self, ctx):
    #    return 1

    #def visitAssignExpr(self, ctx):
    #    name = ctx.getChild(1)
    #    value = self.visit(ctx.value)
#
    #    if value.isdigit():
    #        return "\nmov " + str(name) + ", " + value
    #    else:
    #        return value + "\nmov " + str(name) + ", eax"

    def visitNumberExpr(self, ctx):
        value = ctx.getText()
        #return "mov TMP, " + value + "\n"
        #return "s_push " + value + "\n"
        return value

    def visitVariableExpr(self, ctx: mParser.VariableExprContext):
        name = ctx.getText()

        if name not in variables.keys():
            raise Exception(name + " is undefined")
        return name

    def visitParenExpr(self, ctx):
        return self.visit(ctx.expr())

    def visitInfixExpr(self, ctx):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)
        
        op = ctx.op.text

        #print(ctx.getChild(2))

        Ltype = str(ctx.getChild(0))[1:-1]
        Rtype = str(ctx.getChild(2))[1:-1]

        #print("R: " + r)
        #print("L: " + l)

        #print(str(Ltype) + ", " + str(Rtype))

        operation =  {
        '+': lambda: l + r,
        '-': lambda: l - r,
        '*': lambda: l * r,
        '/': lambda: l / r,
        }
        

        operationTxt =  {
        '+': "add ",
        '-': "sub ",
        '*': "mul ",
        '/': "div ",
        }

        

        if not " " in l and not " " in r:
            return "mov eax, " + l + "\n" + operationTxt.get(op) + "eax, " + r + "\n"
        elif " " in l and not " " in r:
            return l  + operationTxt.get(op) + "eax, " + r + "\n"
        elif not " " in l and " " in r:
            return r  + operationTxt.get(op) + "eax, " + l + "\n"
        elif " " in l and " " in r:
            return l + "push eax\n" + r + "pop ebx\n" + operationTxt.get(op) + "ebx, eax\nmov eax, ebx\n"

        #return operation.get(op, lambda: None)()

    def visitByeExpr(self, ctx):
        print(f"goodbye {get_username()}")
        sys.exit(0)

    def visitHelloExpr(self, ctx):
        return (f"{ctx.getText()} {get_username()}")


if __name__ == "__main__":
    
    #data =  InputStream(input(">>> "))
    text = open("words.c").read()
    data = InputStream(text)

    # lexer
    lexer = mLexer(data)
    stream = CommonTokenStream(lexer)
    # parser
    parser = mParser(stream)
    tree = parser.main()
    # evaluator
    visitor = MyVisitor()
    #ParseTreeListener()

    printer = mListener()
    walker = ParseTreeWalker()

    out = open("output.txt", "w")

    walker.walk(printer, tree)

    out.close()
    #output = visitor.visit(tree)
    #print(output)