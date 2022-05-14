namespace = "exxabite:data"
scoreboard = "system"

def mov(in1, in2):
    if type(in2) == str: #From var
        return "scoreboard players operation "+in1+" system = "+in2+" system"
    else: #From imm
        return "scoreboard players set "+in1+" system "+str(in2)

def push(in1):
    return ("execute store result storage "+ namespace +" TMP int 1 run scoreboard players get "+ in1 +" "+ scoreboard +"\n"
            "data modify storage "+ namespace +" Stack prepend from storage "+ namespace +" TMP")

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
        return ("scoreboard players operation EAX system *= TMP system")

def generateFunctions(input, namespace, scoreboard):

    output = ""

    for op in input:

        if op[0] == 0: out = mov(op[1][0], op[1][1])
        if 1 <= op[0] <= 4: out = arithmatic(op[0], op[1][0], op[1][1])
        if op[0] == 5: out = push(op[1][0])
        if op[0] == 6: out = pop(op[1][0])

        output += out + "\n"
    return output