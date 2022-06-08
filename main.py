import sys
from codeGeneration import arithmatic, generateFunctions
from optimization import optimize
from antlr4 import *
from dist.mLexer import mLexer
from dist.mParser import mParser
from dist.mVisitor import mVisitor
from function import *

types = {
    "int" : 0
}

functions = {}

intermediateVarIndex = 0

currentFunction = Function("main")


operation = {
    "mov" : 0,
    "add" : 1,
    "sub" : 2,
    "mul" : 3,
    "div" : 4,
    "push": 5,
    "pop" : 6
}

mov = 0
add = 1
sub = 2
mul = 3
div = 4
push = 5
pop = 6
call = 7

output = []

mainCode = []

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
        value = int(visitor.visit(ctx.value))
        
        currentFunction.newVariable(name, datatype)

        if type(value) == int:
            currentFunction.appendCode(Instruction(mov, name, value))
        else:
            currentFunction.appendCode(Instruction(mov, name, "eax"))

    def enterAssignVar(self, ctx:mParser.AssignExprContext):
        visitor = MyVisitor()

        name = str(ctx.getChild(0))
        value = visitor.visit(ctx.value)


        if currentFunction.getVarType(name) == -1:
            raise Exception(name + " is undefined")

        if type(value) != list:
            currentFunction.appendCode(Instruction(mov, name, value))
        else:
            currentFunction.appendCode(value)
            currentFunction.appendCode(Instruction(mov, name, "eax"))

    def exitAssignFunction(self, ctx:mParser.AssignFunctionContext):
        name = str(ctx.getChild(0))

        currentFunction.appendCode(Instruction(mov, name, "eax"))

    def enterDefineVar(self, ctx:mParser.DefineVarContext):

        datatype = visitor.visit(ctx.type)
        name = str(ctx.getChild(1))

        currentFunction.newVariable(name, datatype)

    def enterFunctionDefinition(self, ctx:mParser.FunctionDefinitionContext):
        currentFunction.name = str(ctx.getChild(1))


    def exitFunctionDefinition(self, ctx:mParser.FunctionDefinitionContext):
        global mainCode

        if currentFunction.name in functions:
            if currentFunction.parameters in functions[currentFunction.name]:
                raise Exception("Cannot have two functions with identical name and parameters")
            else:
                functions[currentFunction.name] += [currentFunction.parameters]
        else:
            functions[currentFunction.name] = [currentFunction.parameters]

        currentFunction.name = currentFunction.name + ''.join(map(str, currentFunction.parameters))
        mainCode.append(Function(currentFunction.name, currentFunction.code, currentFunction.variables, currentFunction.parameters))
        
        currentFunction.name = ""
        currentFunction.parameters = []
        currentFunction.variables = {}
        currentFunction.code = []


    def enterParam(self, ctx:mParser.ParamContext):

        datatype = visitor.visit(ctx.type)
        name = str(ctx.getChild(1))

        currentFunction.parameters.append(datatype)

        currentFunction.newVariable(name, datatype)
        currentFunction.appendCode(Instruction(pop, name, None))



    def enterReturnStatement(self, ctx:mParser.ReturnStatementContext):
        value = visitor.visit(ctx.value)

        if type(value) != list: #Some type handling impovements could be made
            currentFunction.appendCode(Instruction(mov, "eax", value))
        else:
            currentFunction.appendCode(value)
        pass


    def enterFunctionCall(self, ctx:mParser.FunctionCallContext):
        global parameterStack
        name = str(ctx.getChild(0))

        if not name in functions:
            raise Exception("No such function: " + name)


    def enterCallParam(self, ctx:mParser.CallParamListContext):
        global parameterStack

        try:
            name = int(str(ctx.getChild(0)))
        except:
            name = str(ctx.getChild(0))

        parameterStack.append(name)
        #currentFunction.newVariable(name, 0)
        pass

    def exitFunctionCall(self, ctx:mParser.FunctionCallContext):
        global parameterStack
        name = str(ctx.getChild(0))

        #Change the name to accomodate function overloading
        paramHash = []
        for parameter in parameterStack:
            if type(parameter) == int: paramHash.append(0)
            else: paramHash.append(currentFunction.getVarType(parameter))

        if paramHash not in functions[name]:
            raise Exception ("Invalid parameter types/amount in functon call: " + name)

        for param in reversed(parameterStack):
            currentFunction.appendCode(Instruction(push, None, param))

        currentFunction.appendCode(Instruction(call, None, name + ''.join(map(str, paramHash)))) #This is temporary, call instuctions should be formated differently
        parameterStack = []
        pass

exprDepth = 0

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
        global exprDepth

        exprDepth += 1
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)
        exprDepth -= 1

        op = ctx.op.text



        Ltype = str(ctx.getChild(0))[1:-1]
        Rtype = str(ctx.getChild(2))[1:-1]
        

        opcode =  {
        '+': 1,
        '-': 2,
        '*': 3,
        '/': 4,
        }

        expression = []



        if type(l) != list and type(r) != list:

            if type(l) == int and type(r) == int:
                if op == '+': expression = l + r
                if op == '-': expression = l - r
                if op == '*': expression = l * r
                if op == '/': expression = int(l / r)
                
            else:
                expression += [Instruction(mov, "eax", l)]
                expression += [Instruction(opcode[op], "eax", r)]
        

        elif type(l) == list and type(r) != list:
            expression += l
            expression += [Instruction(opcode[op], "eax", r)]
            
        elif type(l) != list and type(r) == list:
            expression += r
            expression += [Instruction(opcode[op], "eax", l)]

        elif type(l) == list and type(r) == list:
            expression += l
            expression += [Instruction(mov, "__tmp"+str(exprDepth), "eax")]
            expression += r
            expression += [Instruction(opcode[op], "__tmp"+str(exprDepth), "eax")]
            expression += [Instruction(mov, "eax", "__tmp"+str(exprDepth))]
        return expression


if __name__ == "__main__":
    
    #text = open(sys.argv[1]).read() !only for debuging!
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
    

    walker.walk(printer, tree)

    for function in mainCode:
        printFunction(function)

    for line in output:
        print(line)

    optimizedOutput = optimize(output)

    print(mainCode)


    for func in mainCode:
        file = open(sys.argv[2] + func.name + ".mcfunction", "w")
        file.write(generateFunctions(func.code, "exxabite:data", "system", func.variables, func.name))


    print("\nOptimized:\n" )

    for line in optimizedOutput:
        print(line)