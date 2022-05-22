
class Function:
    def __init__(self, name):
        self.name = name
    code = []
    path = []

    def appendCode(self, instr, place=code):
        if len(self.path) == 0:
            self.code.append(instr)
        else:
            #Place is main code and tail is Codeblock
            if len(self.code) > 0 and type(place) != Codeblock and type(place[-1]) == Codeblock:
                self.appendCode(instr, place[-1])

            #Place is Codeblock and tail is Codeblock
            elif type(place) == Codeblock and len(place.code) > 0 and type(place.code[-1]) == Codeblock:
                self.appendCode(instr, place.code[-1])

            #tail is instr
            else:
                #Tail is Null instruction
                if type(place) == Codeblock and len(place.code) > 0 and place.code[-1].opcode == None:
                    place.code[-1] = instr
                else:
                    place.append(instr)

    def enterBlock(self, name, place=code):
        self.__enterBlock(name, place)
        self.path.append(name)

    def __enterBlock(self, name, place):

        #Place is main code and tail is Codeblock
        if len(self.code) > 0 and type(place) != Codeblock and type(place[-1]) == Codeblock:
            self.__enterBlock(name, place[-1])
        #Place is Codeblock and tail is Codeblock
        elif type(place) == Codeblock and len(place.code) > 0 and type(place.code[-1]) == Codeblock:
            self.__enterBlock(name, place.code[-1])

        else:
            place.append(Codeblock(name, []))

            
        #self.path.append(name)

    def exitBlock(self, place=code):
        self.path.pop()
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
            place.append(Instruction(None, None, None))

        #self.block.exit()

    def getVarPath(self, var):
        return '.'.join(map(str, self.path)) + "." + str(var) 

    def clean(self, list=code):
        new = []
        for instr in list:
            if type(instr) == Instruction :
                if instr.opcode == None:
                    break
                    continue
                else:
                    new.append(instr)
            elif type(instr) == Codeblock:
                self.clean(instr.code)
                new.append(instr)
            #else:
            #   self.clean(instr)
        
        self.code = new

class Instruction:
    def __init__(self, opcode, modify, read):
        self.opcode = opcode
        self.modify = test.getVarPath(modify) #This is temporary!!! replace when variables get added.
        #self.modify = modify
        self.read = read

class Codeblock:
    name = ""
    variables = {}
    code = []

    def __init__(self, name, code=[]):
        self.name = name
        self.code = code

    def append(self, instr):
        self.code.append(instr)

    def addVariable(self, name, type):
        self.variables[name] = type

    def exit(self):
        self.name = ""
        self.variables = {}
        self.code = []

test = Function("Test")


test.appendCode(Instruction(0, "eax", 17))
test.enterBlock("some_block")
test.appendCode(Instruction(0, "lol", 17))
test.appendCode(Instruction(1, "lol", 9))
test.enterBlock("brick")
test.appendCode(Instruction(0, "this_is_in_brick", 12))
test.enterBlock("another")
test.appendCode(Instruction(0, "beans", 42))
test.exitBlock()
test.appendCode(Instruction(1, "lol", 6))
test.exitBlock()
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
            print(" "*indent + instr.name + ":")
            printInstr(instr.code, indent + 4)
            #print(" "*indent + "}")
        else:
            #indent += 3
            printInstr(instr, indent)
            #indent -= 3

printInstr(test.code, 0)