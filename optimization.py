from glob import glob


globalCode = []

def constantEvaluation(input):
    constants = []
    occurences  = {}

    values = {}
    new = []
    success = False
    global globalCode

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

    for operation in input:
        #Check to see if operation follows assigment format
        if search and operation[0] == 0 and type(operation[1][0]) == str and type(operation[1][1]) == int:
                search = False
                name = operation[1][0]
                value = operation[1][1]
                new += [[-10, [name, value]]]
                #new += [operation]
        elif operation[1][0] == name:
            search = True
            new += [operation]
        elif len(operation[1]) > 1 and operation[1][1] == name and not search:
            success = True
            new += [[operation[0], [operation[1][0], value]]]
        else:
            new += [operation]

    globalCode = new


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
                 


def optimize(code):
    global globalCode
    globalCode = code
    success = True

    while success == True:
        success = False
        
        success = constantEvaluation(globalCode) #Weird param usage, fix later
        success += removeUnusedVar()

    return globalCode