
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
 
        if len(self.__path) == depth:
            #print("Path "+instr.modify+":" + str(varList))
            place.append(Instruction(instr.opcode, self.getVarPath(instr.modify, varList), self.getVarPath(instr.read, varList)))
        else:
            #Place is main code and tail is Codeblock
            if len(self.code) > 0 and type(place) != Codeblock and type(place[-1]) == Codeblock:
                varList.append(place[-1].variableList)
                #print(varPath)
                self.__appendCode(instr, place[-1], depth+1, varList)

            #Place is Codeblock and tail is Codeblock
            elif type(place) == Codeblock and len(place.code) > 0 and type(place.code[-1]) == Codeblock:
                varList.append(place.code[-1].variableList)
                self.__appendCode(instr, place.code[-1], depth+1, varList)

            #tail is instr
            else:
                place.append(self.getVarPath(instr, varList)) #sus

    def enterBlock(self, name, place=code):
        self.__enterBlock(name, place, 0)
        self.__path.append(name)

    def __enterBlock(self, name, place, depth):

        if len(self.__path) == depth:
            place.append(Codeblock(name, []))

        #Place is main code and tail is Codeblock
        elif len(self.code) > 0 and type(place) != Codeblock and type(place[-1]) == Codeblock:
            self.__enterBlock(name, place[-1], depth+1)
        #Place is Codeblock and tail is Codeblock
        elif type(place) == Codeblock and len(place.code) > 0 and type(place.code[-1]) == Codeblock:
            self.__enterBlock(name, place.code[-1], depth+1)

        else:
            place.append(Codeblock(name, []))

            
        #self.path.append(name)

    def exitBlock(self, place=code):
        self.__path.pop()
        self.__exitBlock(place)

    def __exitBlock(self, place):
        
        #Place is main code
        if len(self.code) > 0 and type(place) != Codeblock and type(place[-1]) == Codeblock and type(place[-1].code[-1]) == Codeblock:
            self.__exitBlock(place[-1])

        elif len(self.code) > 0 and type(place) == Codeblock and type(place.code[-1]) == Codeblock and type(place.code[-1].code[-1]) == Codeblock:
            self.__exitBlock(place.code[-1])
        else:
            #Tail is Null instruction
            #if type(place) == Codeblock and len(place.code) > 0 and type(place.code[-1]) != Codeblock and place.code[-1].opcode == None:
            #    del place.code[-1]

            #place.append(Instruction(None, None, None))
            pass

        #self.block.exit()


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
                #print(str(var) + " varList[index]" + str(varList[index]))
                if var in varList[index]:
                    return self.name + "_" + '.'.join(map(str, self.__path[:(index+1)])) +"."+ var

            #Not in any of the codeblocks
            if var in self.variables:
                return self.name + "_" + var
            else:
                return var



    def clean(self, list=code): #Unused
        self.code = self.__clean(list)

    def __clean(self, list): #Unused
        new = []
        for instr in list:
            if type(instr) == Instruction :
                if instr.opcode != None:
                    new.append(instr)
            elif type(instr) == Codeblock:
                new.append(instr)
                new[-1].code = self.clean(instr.code)
            #else:
            #   self.clean(instr)
        
        return new
    
    def newVariable(self, name, VarType, place=code, depth=0):
        if len(self.__path) == 0:
            self.variables[name] = VarType 
        else:
            if type(place) == Codeblock:
                if place.name == self.__path[-1]:
                    #instr.variables[name] = VarType
                    print(place.name)
                    place.addVariable(name, VarType)
                    #place.append(Instruction(0, "newVar", 16))
                    return
                else:
                    self.newVariable(name, VarType, place.code[-1], depth+1)
            else:
                self.newVariable(name, VarType, place[-1], depth+1)

class Instruction:
    def __init__(self, opcode, modify, read):
        self.opcode = opcode
        #self.modify = test.getVarPath(modify) #This is temporary!!! replace when variables get added.
        self.modify = modify
        self.read = read

class Codeblock:
    #name = ""
    #variables = {}
    #code = []

    def __init__(self, name, code=[], variableList={}):
        self.name = name
        self.code = code
        self.variableList = {}

    def append(self, instr):
        self.code.append(instr)

    def addVariable(self, name, VarType):
        self.variableList[name] = VarType

    #def exit(self):
    #    self.name = ""
    #    self.variables = {}
    #    self.code = []

test = Function("test")


test.appendCode(Instruction(0, "eax", 17))
test.newVariable("lol", 0)
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

#test.clean()

#test.append(Instruction(1, "eax", 17))
#test.append(Instruction(2, "eax", 3))
#test.append(Codeblock("Block", [Instruction(2, "eax", 7), [Instruction(0, "i", "eax"), Instruction(1, "i", 7)], Instruction(0, "eax", "i")]))
#test.append(Codeblock("Beans", [Instruction(0, "eax", 17)]))

#print(test.getVarPath("lol"))
#print(test.name)

def printInstr(list, indent):
    for instr in list:
        if type(instr) == Instruction:
            print(" "*indent + str(instr.opcode) + " " + str(instr.modify) + ", " + str(instr.read))
        elif type(instr) == Codeblock:
            #print(" "*indent + "{ " + instr.name + ":")
            print(" "*indent + instr.name + ": " + str(instr.variableList))
            printInstr(instr.code, indent + 4)
            #print(" "*indent + "}")
        else:
            #indent += 3
            printInstr(instr, indent)
            #indent -= 3

printInstr(test.code, 0)