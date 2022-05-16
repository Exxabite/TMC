namespace = "exxabite:data"
scoreboard = "system"

def mov(in1, in2):
    if type(in2) == str: #From var
        return "scoreboard players operation "+in1+" system = "+in2+" system"
    else: #From imm
        return "scoreboard players set "+in1+" system "+str(in2)

def push(in1):
    if type(in1) == str:
        return ("execute store result storage "+ namespace +" TMP int 1 run scoreboard players get "+ in1 +" "+ scoreboard +"\n"
                "data modify storage "+ namespace +" Stack prepend from storage "+ namespace +" TMP")

    elif type(in1) == int:
        return "data modify storage "+ namespace +" Stack prepend value " + str(in1)

def pop(in1):
    return ("execute store result score "+ in1 +" system run data get storage "+ namespace +" Stack[0] 1\n"
            "data remove storage "+ namespace +" Stack[0]")
    


def arithmatic(op, in1, in2):
    code = { #0, 5 and 6 need to be there, I don't know why since they never seem to be used
        0 : "brick o' beans",
        1 : "+=",
        2 : "-=",
        3 : "*=",
        4 : "/=",
        5 : "waffles",
        6 : "more beans"
    }
    if type(in2) == str:
        return "scoreboard players operation "+in1+" system "+code[op]+" "+in2+" system"
    elif op <= 2:
        return "scoreboard players " + ("add" if op == 1 else "remove") + " "+in1+" system "+str(in2)
    else:
        return "scoreboard players operation "+in1+" system "+code[op]+" "+ str(in2) +" system"

def call(in1):
    return "function " + "exxabite" + ":" + in1

def generateFunctions(input, namespace, scoreboard, varList, functionName):

    output = ""

    #Convert var names to the function namespace
    for op in input:
        if op[0] < 7:
            if type(op[1][0]) != int and varList[op[1][0]] == 0:
                op[1][0] = functionName + "_" + op[1][0]

            if len(op[1]) > 1 and type(op[1][1]) != int and varList[op[1][1]] == 0:
                op[1][1] = functionName + "_" + op[1][1]

    for op in input:

        if op[0] == 0: out = mov(op[1][0], op[1][1])
        if 1 <= op[0] <= 4: out = arithmatic(op[0], op[1][0], op[1][1])
        if op[0] == 5: out = push(op[1][0])
        if op[0] == 6: out = pop(op[1][0])
        if op[0] == 7: out = call(op[1][0])

        output += out + "\n"
    return output