from glob import glob
from re import I, T

from numpy import size


globalCode = []

def constantEvaluation():
    constants = []
    occurences  = {}

    values = {}
    new = []
    success = False
    global globalCode

    input = globalCode

    #True for search false for replace
    search = True
    name = ""
    value = 0

    i = 0
    for operation in input:
        opcode = operation[0]
        op1 = operation[1][0]
        op2 = operation[1][1]

        #If operation is (mov var, imm)
        if opcode == 0 and type(op1) == str and type(op2) == int:

            #For all operations after operation
            for index in range(i + 1, len(globalCode)):
                if i == len(globalCode): break

                checkOperation = globalCode[index]

                if checkOperation[1][1] == op1: 
                    globalCode[index][1][1] = op2
                    success = True

                if checkOperation[1][0] == op1: break
        i += 1

    return success


def removeUnusedVar():
    success = False
    global globalCode
    new = []


    i = 0
    for operation in globalCode:
        if operation[0] == 0 and type(operation[1][0]) == str and type(operation[1][1]) == int:
            name = operation[1][0]
            used = False

            #Check to see if the variable is used
            for index in range(i + 1, len(globalCode)):
                op = globalCode[index]
                if op[1][1] == name or (1 <= op[0] <= 4 and op[1][0] == name):
                    used = True
                    #print(name + " is used")
                    break
                
                #Break if var is modified
                if op[1][0] == name: break

            if used:
                new += [operation]
            else:
                success = True
        else:
            new += [operation]

        i += 1
    globalCode = new
    return success
                 
def peephole():
    global globalCode
    success = False

    size = len(globalCode) - 2

    index = 0
    while index < len(globalCode) - 1:

        operation = globalCode[index]

        #Optimizations that start with (mov var, var)
        if operation[0] == 0 and type(operation[1][0]) == str and type(operation[1][1]) == str:

            #Optimizes mov var1, var2
            #          mov var2, var1
            if (globalCode[index+1][0] == 0
            and operation[1][0] == globalCode[index+1][1][1] 
            and operation[1][1] == globalCode[index+1][1][0]):
                del globalCode[index+1]
                size -= 1
                success = True

        #Optimizations that start with (mov var, int)
        if operation[0] == 0 and type(operation[1][0]) == str and type(operation[1][1]) == int:

            #Optimize mov   var, int
            #         arith var, int
            if (1 <= globalCode[index+1][0] <= 4
            and operation[1][0] == globalCode[index+1][1][0] 
            and type(globalCode[index+1][1][1]) == int):
                
                if globalCode[index+1][0] == 1: operation[1][1] = operation[1][1] + globalCode[index+1][1][1]
                if globalCode[index+1][0] == 2: operation[1][1] = operation[1][1] - globalCode[index+1][1][1]

                del globalCode[index+1]
                size -= 1
                success = True

        #if index == len(globalCode): break
        index += 1
    return success


def optimize(code):
    global globalCode
    globalCode = code
    success = True

    while success > 0:
        success = False
        
        success = constantEvaluation()
        #success += removeUnusedVar()
        success += peephole()

    return globalCode