class Function:
    def __init__(self, name):
        self.name = name
    code = []
    __path = []
    variables = {}

    def appendCode(self, instr, place=code, depth=0):
        varList=[]
        self.__appendCode(instr, place, depth, varList)

    def __appendCode(self, instr, place, depth, varList):
        
        #Decent has reached the correct depth - Append instruction
        if len(self.__path) == depth:
            place.append(Instruction(instr.opcode, self.getVarPath(instr.modify, varList), self.getVarPath(instr.read, varList)))
        else:
            #Place is main code and tail is Codeblock - Enter block
            if len(self.code) > 0 and type(place) != Codeblock and type(place[-1]) == Codeblock:
                varList.append(place[-1].variableList)
                self.__appendCode(instr, place[-1], depth+1, varList)

            #Place is Codeblock and tail is Codeblock - Enter block
            elif type(place) == Codeblock and len(place.code) > 0 and type(place.code[-1]) == Codeblock:
                varList.append(place.code[-1].variableList)
                self.__appendCode(instr, place.code[-1], depth+1, varList)


    def enterBlock(self, name, place=code):
        self.__enterBlock(name, place, 0)
        self.__path.append(name)

    def __enterBlock(self, name, place, depth):

        #Decent has reached the correct depth - Append new block
        if len(self.__path) == depth:
            place.append(Codeblock(name, []))

        #Place is main code and tail is Codeblock - Enter block
        elif len(self.code) > 0 and type(place) != Codeblock and type(place[-1]) == Codeblock:
            self.__enterBlock(name, place[-1], depth+1)
        #Place is Codeblock and tail is Codeblock - Enter block
        elif type(place) == Codeblock and len(place.code) > 0 and type(place.code[-1]) == Codeblock:
            self.__enterBlock(name, place.code[-1], depth+1)


    def exitBlock(self, place=code):
        self.__path.pop()
        self.__exitBlock(place)

    def __exitBlock(self, place):
        
        #Place is main code
        if len(self.code) > 0 and type(place) != Codeblock and type(place[-1]) == Codeblock and type(place[-1].code[-1]) == Codeblock:
            self.__exitBlock(place[-1])

        elif len(self.code) > 0 and type(place) == Codeblock and type(place.code[-1]) == Codeblock and type(place.code[-1].code[-1]) == Codeblock:
            self.__exitBlock(place.code[-1])


    def getVarPath(self, var, varList):
        if type(var) == int:
            return var
        if len(self.__path) == 0:
            if var in self.variables:
                return self.name + "_" + var
            else:
                return var

        else:
            for index in reversed(range(0, len(varList))):
                if var in varList[index]:
                    return self.name + "_" + '.'.join(map(str, self.__path[:(index+1)])) +"."+ var

            #Not in any of the codeblocks
            if var in self.variables:
                return self.name + "_" + var
            else:
                return var

    
    def newVariable(self, name, VarType, place=code, depth=0):
        if len(self.__path) == 0:
            self.variables[name] = VarType 
        else:
            if type(place) == Codeblock:
                if place.name == self.__path[-1]:
                    print(place.name)
                    place.addVariable(name, VarType)
                    return
                else:
                    self.newVariable(name, VarType, place.code[-1], depth+1)
            else:
                self.newVariable(name, VarType, place[-1], depth+1)

class Instruction:
    def __init__(self, opcode, modify, read):
        self.opcode = opcode
        self.modify = modify
        self.read = read

class Codeblock:
    def __init__(self, name, code=[], variableList={}):
        self.name = name
        self.code = code
        self.variableList = {}

    def append(self, instr):
        self.code.append(instr)

    def addVariable(self, name, VarType):
        self.variableList[name] = VarType

#Example of gneration code
test = Function("test")

test.appendCode(Instruction(0, "eax", 17))
test.newVariable("lol", 0)
test.newVariable("lel", 0)
test.appendCode(Instruction(0, "lol", "eax"))
test.enterBlock("someBlock")
test.appendCode(Instruction(0, "lol", 17))
test.appendCode(Instruction(1, "lol", 9))
test.enterBlock("brick")
test.appendCode(Instruction(0, "brick", 12))
test.newVariable("beans", 0)
test.enterBlock("another")
test.appendCode(Instruction(0, "beans", 42))
test.exitBlock()
test.appendCode(Instruction(1, "lol", 6))
test.exitBlock()
test.appendCode(Instruction(0, "lel", 7))
test.exitBlock()
test.appendCode(Instruction(1, "eax", 18))


def printCode(list, indent=0):
    for instr in list:
        if type(instr) == Instruction:
            print(" "*indent + str(instr.opcode) + " " + str(instr.modify) + ", " + str(instr.read))
        elif type(instr) == Codeblock:
            print(" "*indent + instr.name + ": " + ', '.join(map(str, instr.variableList)))
            printCode(instr.code, indent + 4)

def printFunction(fun, indent=0):
    print("Name: " + fun.name)
    print("Variables: " + ', '.join(map(str, fun.variables)))
    print("Code:")
    printCode(fun.code, 4)

printFunction(test)