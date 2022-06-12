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
        self.__breadcrumb = []

    def appendCode(self, instr, depth=0, var_list=None):
        place = self.code

        if var_list == None:
            var_list = []

        if type(instr) == list:
                for item in instr:
                    place.append(Instruction(item.opcode, self.getVarPath(item.modify, var_list), self.getVarPath(item.read, var_list), item.codeblock)) #Implement recurion for infinate depth
        else:
            place.append(Instruction(instr.opcode, self.getVarPath(instr.modify, var_list), self.getVarPath(instr.read, var_list), instr.codeblock))


    def __appendCode(self, instr, place, depth, var_list):
        
        


        #Decent has reached the correct depth - Append instruction
        """"
        if len(self.__path) == depth:
            self.__varList = var_list
            if type(instr) == list:
                for item in instr:
                    place.append(Instruction(item.opcode, self.getVarPath(item.modify, var_list), self.getVarPath(item.read, var_list), item.codeblock)) #Implement recurion for infinate depth
            else:
                place.append(Instruction(instr.opcode, self.getVarPath(instr.modify, var_list), self.getVarPath(instr.read, var_list), instr.codeblock))
        else:
            #Place is main code and tail is Codeblock - Enter block
            if len(self.code) > 0 and type(place) != Codeblock and type(place[-1]) == Codeblock:
                var_list.append(place[-1].variableList)
                self.__appendCode(instr, place[-1], depth+1, var_list)

            #Place is Codeblock and tail is Codeblock - Enter block
            elif type(place) == Codeblock and len(place.code) > 0 and type(place.code[-1]) == Codeblock:
                var_list.append(place.code[-1].variableList)
                self.__appendCode(instr, place.code[-1], depth+1, var_list)
        """


    def enterBlock(self, name):
        if type(self.__place) == Function:
            self.__place.code.append(Codeblock(name, []))
        else:
            self.__place.append(Codeblock(name, []))

        self.__breadcrumb.append(self.__place)
        self.__place = self.__place.code[-1]
        print("Enter: " + self.__place.name)
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


    def exitBlock(self):
        print("Exit: " + self.__place.name)
        #place = self.code
        self.__place = self.__breadcrumb[-1]
        self.__breadcrumb.pop()
        self.__path.pop()
        #self.__exitBlock(place)

    def __exitBlock(self, place):
        
        #Place is main code
        if len(self.code) > 0 and type(place) != Codeblock and type(place[-1]) == Codeblock and type(place[-1].code[-1]) == Codeblock:
            self.__exitBlock(place[-1])

        elif len(self.code) > 0 and type(place) == Codeblock and type(place.code[-1]) == Codeblock and type(place.code[-1].code[-1]) == Codeblock:
            self.__exitBlock(place.code[-1])


    def getPath(self):
        if len(self.__path) == 0:
            return self.name + "_"
        else:
            return self.name + "_" + '.'.join(map(str, self.__path)) + "."

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

    def newVariable(self, name, VarType, depth=0):
        #self.__newVariable(name, VarType, self.code, depth)
        if len(self.__path) == 0:
            self.variables[name] = VarType
        else:
            self.__place.addVariable(name, VarType)

    def __newVariable(self, name, VarType, place, depth=0):
        """
        #place=self.code
        if len(self.__path) == 0:
            self.variables[name] = VarType 
        else:
            if type(place) == Codeblock:
                if place.name == self.__path[-1]:
                    print(place.name)
                    place.addVariable(name, VarType)
                    return
                else:
                    self.__newVariable(name, VarType, place.code[-1], depth+1)
            else:
                self.__newVariable(name, VarType, place[-1], depth+1)
        """

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
    def __init__(self, name, code=None, variableList=None):
        self.name = name

        #This is a temprorary fix.
        self.code = []
        self.variableList = []

        if code is None:
            self.code = []
        if variableList is None:
            self.variableList = {}

    def append(self, instr):
        self.code.append(instr)

    def addVariable(self, name, VarType):
        self.variableList[name] = VarType

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
                print(" "*indent + operation[instr.opcode] + " " + str(instr.codeReference))

        elif type(instr) == Codeblock:
            print(" "*indent + instr.name + ": " + ', '.join(map(str, instr.variableList)))
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