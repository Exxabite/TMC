#from curses.ascii import isdigit
from ast import Assign
from multiprocessing.dummy.connection import Listener
from operator import contains
import string
import sys
import json
from codeGeneration import arithmatic, generateFunctions
from optimization import optimize
from antlr4 import *
from dist.mLexer import mLexer
from dist.mParser import mParser
from dist.mVisitor import mVisitor



types = {
    "int" : 0
}

functions = {}

class Function:
    name = ""
    parameters = []
    code = []
    variables = {
        "eax" : 100,
        "ebx" : 100,
        "ecx" : 100,
        "edx" : 100
    }

    def addParameter(self, param):
        self.parameters.append(param) 

    def addInstruction(self, instr):
        self.code.append(instr)

    def addVariable(self, name, type):
        self.variables[name] = type

    def reset(self):
        self.name = ""
        self.parameters = []
        self.code = []
        self.variables = {
            "eax" : 100,
            "ebx" : 100,
            "ecx" : 100,
            "edx" : 100
        }
    
currentFunction = Function()

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

mainCode = {}

class instr:
    def mov(operand1, operand2):
        return [0, [operand1, operand2]]
    def add(operand1, operand2):
        return [1, [operand1, operand2]]
    def sub(operand1, operand2):
        return [2, [operand1, operand2]]
    def mul(operand1, operand2):
        return [3, [operand1, operand2]]
    def div(operand1, operand2):
        return [4, [operand1, operand2]]
    def push(operand1):
        return [5, [operand1]]
    def pop(operand1):
        return [6, [operand1]]
    def call(operand1):
        return [7, [operand1]]

def append(input):
    global output
    output += input

def newOp(op, operands):
    global output
    output += [[operation[op], operands]]

parameterStack = []

class mListener(ParseTreeListener):
    def enterAssignExpr(self, ctx:mParser.AssignExprContext):
        visitor = MyVisitor()

        datatype = visitor.visit(ctx.type)
        name = str(ctx.getChild(1))
        value = visitor.visit(ctx.value)
        
        currentFunction.addVariable(name, datatype)

        if type(value) == int:
            currentFunction.addInstruction(instr.mov(str(name), int(value)))
        else:
            currentFunction.addInstruction(instr.mov(str(name), "eax"))

    def enterAssignVar(self, ctx:mParser.AssignExprContext):
        visitor = MyVisitor()

        name = str(ctx.getChild(0))
        value = visitor.visit(ctx.value)


        if name not in currentFunction.variables.keys():
            raise Exception(name + " is undefined")


        if type(value) != list:
            currentFunction.addInstruction(instr.mov(name, value))
        else:
            currentFunction.addInstruction(value)
            currentFunction.addInstruction(instr.mov(name, "eax"))

    def exitAssignFunction(self, ctx:mParser.AssignFunctionContext):
        name = str(ctx.getChild(0))

        currentFunction.addInstruction(instr.mov(name, 'eax'))

        pass

    def enterDefineVar(self, ctx:mParser.DefineVarContext):

        datatype = visitor.visit(ctx.type)
        name = str(ctx.getChild(1))

        currentFunction.addVariable(name, datatype)

    def enterFunctionDefinition(self, ctx:mParser.FunctionDefinitionContext):
        currentFunction.name = str(ctx.getChild(1))

        pass

    def exitFunctionDefinition(self, ctx:mParser.FunctionDefinitionContext):
        global mainCode

        mainCode[currentFunction.name] = {"variables" : currentFunction.variables, "code" : currentFunction.code}
        functions[currentFunction.name] = currentFunction.parameters
        
        currentFunction.reset()


    def enterParam(self, ctx:mParser.ParamContext):

        datatype = visitor.visit(ctx.type)
        name = str(ctx.getChild(1))

        currentFunction.addParameter(type)

        currentFunction.addInstruction(instr.pop(name))

        currentFunction.addVariable(name, datatype)


    def enterReturnStatement(self, ctx:mParser.ReturnStatementContext):
        value = visitor.visit(ctx.value)

        if type(value) != list:
            currentFunction.addInstruction(instr.mov("eax", value))
        else:
            currentFunction.addInstruction(value)
        pass


    def enterFunctionCall(self, ctx:mParser.FunctionCallContext):
        global parameterStack
        name = str(ctx.getChild(0))

        if not name in functions:
            raise Exception("No such function: " + name)


    def enterCallParam(self, ctx:mParser.CallParamListContext):
        global parameterStack

        print(ctx.getChild(0))

        try:
            name = int(str(ctx.getChild(0)))
        except:
            name = str(ctx.getChild(0))

        parameterStack.append(name)
        pass

    def exitFunctionCall(self, ctx:mParser.FunctionCallContext):
        global parameterStack
        name = str(ctx.getChild(0))

        for param in reversed(parameterStack):
            currentFunction.addInstruction(instr.push(param))
        currentFunction.addInstruction(instr.call(name))
        parameterStack = []
        pass

class MyVisitor(mVisitor):

    def visitNumberExpr(self, ctx):
        value = ctx.getText()
        return int(value)

    def visitVariableExpr(self, ctx: mParser.VariableExprContext):
        name = ctx.getText()

        if name not in currentFunction.variables.keys():
            raise Exception(name + " is undefined")
        return name

    def visitParenExpr(self, ctx):
        return self.visit(ctx.expr())

    def visitTypeSpecifier(self, ctx: mParser.TypeSpecifierContext):
        
        type = str(ctx.getChild(0))

        return types[type]

    def visitInfixExpr(self, ctx):
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)
        
        op = ctx.op.text



        Ltype = str(ctx.getChild(0))[1:-1]
        Rtype = str(ctx.getChild(2))[1:-1]
        

        operationFunc =  {
        '+': instr.add,
        '-': instr.sub,
        '*': instr.mul,
        '/': instr.div,
        }

        expression = []



        if type(l) != list and type(r) != list:

            if type(l) == int and type(r) == int:
                if op == '+': expression = l + r
                if op == '-': expression = l - r
                if op == '*': expression = l * r
                if op == '/': expression = int(l / r)
                
            else:
                expression += instr.mov("eax", l)
                expression += operationFunc[op]("eax", r)
        

        elif type(l) == list and type(r) != list:
            expression += l
            expression += operationFunc[op]("eax", r)
            
        elif type(l) != list and type(r) == list:
            expression += r
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
    

    walker.walk(printer, tree)

    for line in output:
        print(line)

    optimizedOutput = optimize(output)

    with open(sys.argv[1] + ".json", 'w') as fp:
        json.dump(mainCode, fp)

    print(mainCode)
    print(functions)


    for func in mainCode:
        file = open(sys.argv[2] + func + ".mcfunction", "w")
        file.write(generateFunctions(mainCode[func]["code"], "exxabite:data", "system", mainCode[func]["variables"], func))



    print("\nOptimized:\n" )

    for line in optimizedOutput:
        print(line)