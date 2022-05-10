#from curses.ascii import isdigit
from ast import Assign
from multiprocessing.dummy.connection import Listener
from operator import contains
import string
import sys
import pickle
from antlr4 import *
from dist.mLexer import mLexer
from dist.mParser import mParser
from dist.mVisitor import mVisitor



variable = {
    "int" : 0
}

variables = {
    "eax" : 0,
    "ebx" : 0,
    "ecx" : 0,
    "edx" : 0
}

operation = {
    "mov" : 0,
    "add" : 1,
    "sub" : 2,
    "mul" : 3,
    "div" : 4,
    "push": 5,
    "pop" : 6
}

output = []

class instr:
    def mov(operand1, operand2):
        return [[0, [operand1, operand2]]]
    def add(operand1, operand2):
        return [[1, [operand1, operand2]]]
    def sub(operand1, operand2):
        return [[2, [operand1, operand2]]]
    def mul(operand1, operand2):
        return [[3, [operand1, operand2]]]
    def div(operand1, operand2):
        return [[4, [operand1, operand2]]]
    def push(operand1):
        return [[5, operand1]]
    def pop(operand1):
        return [[6, operand1]]

def append(input):
    global output
    output += input

def newOp(op, operands):
    global output
    output += [[operation[op], operands]]



class mListener(ParseTreeListener):
    def enterAssignExpr(self, ctx:mParser.AssignExprContext):
        visitor = MyVisitor()

        name = ctx.getChild(1)
        value = visitor.visit(ctx.value)
        
        variables[str(name)] = 0 #SAFTEY!

        if value.isdigit():
            out.write("mov " + str(name) + ", " + value + "\n")
            append(instr.mov(str(name), int(value)))
        else:
            out.write(value + "mov " + str(name) + ", eax\n")
            append(instr.mov(str(name), "eax"))

    def enterAssignVar(self, ctx:mParser.AssignExprContext):
        visitor = MyVisitor()

        name = str(ctx.getChild(0))
        value = visitor.visit(ctx.value)


        if name not in variables.keys():
            raise Exception(name + " is undefined")

        if type(value) != list:
            #out.write("mov " + name + ", " + value + "\n")
            #newOp("mov", [str(name), int(value)])
            append(instr.mov(name, int(value)))
        else:
            #out.write(value + "mov " + name + ", eax\n")
            #newOp("mov", [str(name), "eax"])
            append(value)
            append(instr.mov(name, "eax"))

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

        

        operationFunc =  {
        '+': instr.add,
        '-': instr.sub,
        '*': instr.mul,
        '/': instr.div,
        }

        expression = []



        if type(l) != list and type(r) != list:
            #expression += [[operation["mov"], ["eax", l]]]
            expression += instr.mov("eax", l)
            #expression += [[operationTxt[op], ["eax", r]]]
            expression += operationFunc[op]("eax", r)

        elif type(l) == list and type(r) != list:
            expression += l
            #expression += [[operationTxt[op], ["eax", r]]]
            expression += operationFunc[op]("eax", r)
            
        elif type(l) != list and type(r) == list:
            expression += r
            #expression += [[operationTxt[op], ["eax", l]]]
            expression += operationFunc[op]("eax", l)

        elif type(l) == list and type(r) == list:
            expression += l
            expression += instr.push("eax")
            expression += r
            expression += instr.pop("ebx")
            expression += operationFunc[op]("ebx", "eax")
            expression += instr.mov("eax", "ebx")
        return expression


if __name__ == "__main__":
    
    #data =  InputStream(input(">>> "))
    text = open(sys.argv[1]).read()
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

    out = open(sys.argv[2], "w")
    
    with open(sys.argv[1] + ".pickle", 'wb') as fp:
        pickle.dump(output, fp)

    walker.walk(printer, tree)

    out.close()
    #output = visitor.visit(tree)
    for line in output:
        print(line)