class Function:
    __path = []
    __varList = []
    def __init__(self, name, code=None, variables=None, parameters=None):
        self.name = name
        if code is None:
            self.code = []
        else:
            self.code = code

        if variables is None:
            self.variables = {}
        else:
            self.variables = variables

        if parameters is None:
            self.parameters = []
        else:
            self.parameters = parameters

        self.__place = self
        self.breadcrumb = []

    def appendCode(self, instr, depth=0, var_list=None):

        if var_list == None:
            var_list = []

        if type(instr) == list:
                for item in instr:
                    self.__place.append(Instruction(item.opcode, self.getVarPath(item.modify), self.getVarPath(item.read), item.codeblock)) #Implement recurion for infinate depth
        else:
            self.__place.append(Instruction(instr.opcode, self.getVarPath(instr.modify), self.getVarPath(instr.read), instr.codeblock))

    def append(self, instr):
        self.code.append(instr)

    def enterBlock(self, name):
        self.__place.append(Codeblock(name, []))

        self.breadcrumb.append(self.__place)
        self.__place = self.__place.code[-1]
        print("Enter: " + self.getPath() + self.__place.name)
        self.__path.append(name)


    def exitBlock(self):
        print("Exit: " + self.getPath() + self.__place.name)
        #place = self.code
        self.__place = self.breadcrumb[-1]
        self.breadcrumb.pop()
        self.__path.pop()


    def getPath(self):
        if len(self.__path) == 0:
            return self.name + "_"
        else:
            return self.name + "_" + '.'.join(map(str, self.__path)) + "."


    def getVarPath(self, var):
        if type(var) == int:
            return var

        if len(self.breadcrumb) == 0:
            if var in self.variables:
                return self.name + "_" + var
            else:
                return var
        else:
            for depth in reversed(range(0, len(self.breadcrumb))):
                if var in self.__place.variables:
                    return self.name + "_" + '.'.join(map(str, self.__path[:(depth+1)])) +"."+ var

                elif var in self.breadcrumb[depth].variables:
                    if depth == 0:
                        return self.name + "_" + var
                    else:
                        return self.name + "_" + '.'.join(map(str, self.__path[:(depth+1)])) +"."+ var
            
            return var  #Not in any of the codeblocks

    def newVariable(self, name, VarType, depth=0):
        #self.__newVariable(name, VarType, self.code, depth)
        if len(self.__path) == 0:
            self.variables[name] = VarType
        else:
            self.__place.addVariable(name, VarType)

    def getVarType(self, var):
        if type(var) == int:
            return -1
        if len(self.__path) == 0:
            if var in self.variables: 
                return self.variables[var]
            else:
                return -1
        else:
            for index in reversed(range(0, len(self.__varList))):
                if var in self.__varList[index]:
                    return self.__varList[var]

class Instruction:
    def __init__(self, opcode, modify, read, codeblock=None):
        self.opcode = opcode
        self.modify = modify
        self.read = read
        self.codeblock = codeblock          

class Codeblock:
    def __init__(self, name, code=None, variables=None):
        self.name = name

        #This is a temprorary fix.
        self.code = []
        self.variables = []

        if code is None:
            self.code = []
        if variables is None:
            self.variables = {}

    def append(self, instr):
        self.code.append(instr)

    def addVariable(self, name, VarType):
        self.variables[name] = VarType

#Example of gneration code

#test = Function("test")
#
#test.newVariable("lol", 0)
#test.appendCode(Instruction(6, "lol", None))
#test.newVariable("lel", 0)
#test.appendCode(Instruction(0, "lol", "eax"))
#test.enterBlock("someBlock")
#test.appendCode(Instruction(0, "lol", 17))
#test.appendCode(Instruction(1, "lol", 9))
#test.enterBlock("brick")
#test.appendCode(Instruction(0, "brick", 12))
#test.newVariable("beans", 0)
#test.enterBlock("another")
#test.appendCode(Instruction(0, "beans", 42))
#test.exitBlock()
#test.appendCode(Instruction(1, "lol", 6))
#test.exitBlock()
#test.appendCode(Instruction(0, "lel", 7))
#test.exitBlock()
#test.appendCode(Instruction(1, "eax", 18))


operation = {
    0 : "mov",
    1 : "add",
    2 : "sub",
    3 : "mul",
    4 : "div",
    5 : "push",
    6 : "pop",
    7 : "call",
    8 : "je",
    9 : "jg",
    10: "jge",
    11: "jl",
    12: "jle",
    13: "jne"
}

def printCode(code_list, indent=0):
    for instr in code_list:
        if type(instr) == Instruction:
            if 8 <= instr.opcode <= 13:
                print(" "*indent + operation[instr.opcode] + " " + str(instr.modify) + ", " + str(instr.read) + ", " + str(instr.codeblock))
            elif type(instr.modify) == type(None) and type(instr.read) != type(None):
                print(" "*indent + operation[instr.opcode] + " " + str(instr.read))

            elif type(instr.modify) != type(None) and type(instr.read) == type(None):
                print(" "*indent + operation[instr.opcode] + " " + str(instr.modify))

            elif type(instr.modify) != type(None) and type(instr.read) != type(None):
                print(" "*indent + operation[instr.opcode] + " " + str(instr.modify) + ", " + str(instr.read))
            
            else:
                print(" "*indent + operation[instr.opcode] + " " + str(instr.codeReference)) #Should never be reached

        elif type(instr) == Codeblock:
            print(" "*indent + instr.name + ": " + ', '.join(map(str, instr.variables)))
            printCode(instr.code, indent + 4)
        else:
            print(instr)

def printFunction(fun): #indent=0 might be used later
    print("Name: " + fun.name)
    print("Variables: " + ', '.join(map(str, fun.variables)))
    print("Code:")
    printCode(fun.code, 4)
    print("\n")
#printFunction(test)