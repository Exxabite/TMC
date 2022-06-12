import sys
from codeGeneration import generateFunctions
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
je = 8
jg = 9
jge = 10
jl = 11
jle = 12
jne = 13

OUTPUT = []

ifStatementCount = 0

codeblockName = None

mainCode = []

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

        mainCode.append(
            Function(currentFunction.name, currentFunction.code,
                    currentFunction.variables, currentFunction.parameters
            )
        )

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

    def exitParamList(self, ctx:mParser.ParamListContext):
        
        if currentFunction.name in functions:
            if currentFunction.parameters in functions[currentFunction.name]:
                raise Exception("Cannot have two functions with identical name and parameters")
            else:
                functions[currentFunction.name] += [currentFunction.parameters]
        else:
            functions[currentFunction.name] = [currentFunction.parameters]

        currentFunction.name = currentFunction.name + ''.join(map(str, currentFunction.parameters))

    def enterReturnStatement(self, ctx:mParser.ReturnStatementContext):
        value = visitor.visit(ctx.value)

        if type(value) != list: #Some type handling impovements could be made
            currentFunction.appendCode(Instruction(mov, "eax", value))
        else:
            currentFunction.appendCode(value)


    def enterFunctionCall(self, ctx:mParser.FunctionCallContext):
        global parameterStack
        name = str(ctx.getChild(0))

        if not name in functions:
            raise Exception("No such function: " + name)


    def enterCallParam(self, ctx:mParser.CallParamListContext):

        try:
            name = int(str(ctx.getChild(0)))
        except ValueError:
            name = str(ctx.getChild(0))

        parameterStack.append(name)

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

    def enterSelectionStatement(self, ctx:mParser.SelectionStatementContext):
        global ifStatementCount
        global codeblockName

        codeblockName = "if" + str(ifStatementCount)
        comparison = visitor.visit(ctx.comparison)
        op = str(ctx.comparison.getChild(1))
        
        for operation in comparison:
            currentFunction.appendCode(operation)

        

        ifStatementCount += 1

        inverseCode = {
            8 : 13,  # ==  -->  !=
            9 : 10,  # <   -->  >=
            10 : 9,  # <=  -->  >
            11 : 10, # >   -->  <=
            12 : 9,  # >=  -->  <
            13 : 8   # !=  -->  ==
        }
        
        if ctx.getChildCount() == 5: #Normal if statement
            pass
        else: #If else statement
            currentFunction.appendCode(
                [Instruction(inverseCode[comparison[-1].opcode], 
                            comparison[-1].modify, 
                            comparison[-1].read, 
                            currentFunction.getPath() + codeblockName + "else")
                ]
            )

    def exitSelectionStatement(self, ctx:mParser.SelectionStatementContext):
        global codeblockName
        global ifStatementCount

    def enterElseString(self, ctx:mParser.ElseStringContext):
        global codeblockName
        codeblockName = "if" + str(ifStatementCount) + "else"

    # Enter a parse tree produced by mParser#compoundStatement.
    def enterCompoundStatement(self, ctx:mParser.CompoundStatementContext):
        if codeblockName != None:
            currentFunction.enterBlock(codeblockName)

    # Exit a parse tree produced by mParser#compoundStatement.
    def exitCompoundStatement(self, ctx:mParser.CompoundStatementContext):
        global codeblockName
        global ifStatementCount
        if ifStatementCount > 0:
            codeblockName = None
            ifStatementCount -= 1
            currentFunction.exitBlock()
    
    
    def enterCondition(self, ctx:mParser.ConditionContext):
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
        
        variable_type = str(ctx.getChild(0))

        return types[variable_type]

    def visitInfixExpr(self, ctx):
        global exprDepth

        exprDepth += 1
        l = self.visit(ctx.left)
        r = self.visit(ctx.right)
        exprDepth -= 1

        op = ctx.op.text
        

        opcode = {
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

    def visitCondition(self, ctx:mParser.ConditionContext):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        op = str(ctx.getChild(1))

        expression = []

        code = {
            "==": 8,
            ">": 9,
            ">=": 10,
            "<": 11,
            "<=": 12,
            "!=": 13
        }

        if type(left) == list and type(right) != list:
            expression += left
            expression += [Instruction(code[op], "eax", right, currentFunction.getPath() + codeblockName)]
        elif type(left) != list and type(right) == list:
            expression += right
            expression += [Instruction(code[op], left, "eax", currentFunction.getPath() + codeblockName)]
        elif type(left) == list and type(right) == list:
            expression += right
            expression += [Instruction(mov, "ebx", "eax")]
            expression += left
            expression += [Instruction(code[op], "eax", "ebx", currentFunction.getPath() + codeblockName)]
        else:
            expression += [Instruction(code[op], left, right, currentFunction.getPath() + codeblockName)]
        return expression

if __name__ == "__main__":
    
    #text = open(sys.argv[1]).read() !only for debuging!
    text = open("words.c", encoding="utf-8").read()
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

    for line in OUTPUT:
        print(line)

    optimizedOutput = optimize(OUTPUT)

    def denest(code, functionName, path=None):
        
        output = []

        if type(code) == Function:
            path = ""
            tmpBlock = Codeblock(functionName)
        elif type(code) == Codeblock:
            tmpBlock = Codeblock(functionName + "_" + path)
        
        for instr in code.code:
            if type(instr) == Instruction:
                tmpBlock.append(instr)
            elif type(instr) == Codeblock:
                if len(path) > 0 and path[-1] != "_":
                    output += denest(instr, functionName, path + "." +instr.name )
                else:
                    output += denest(instr, functionName, path + instr.name )

        output += [tmpBlock]
        return output

    denestedCode = []
    for func in mainCode:
        denestedCode += denest(func, func.name)

    for block in denestedCode:
            print(block.name)

    for func in denestedCode:
        file = open(sys.argv[2] + func.name + ".mcfunction", "w", encoding="utf-8")
        file.write(
            generateFunctions(func.code,"exxabite", "system")
        )


    print("\nOptimized:\n" )

    for line in optimizedOutput:
        print(line)
