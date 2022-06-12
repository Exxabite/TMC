#Instruction types
def mov(in1, in2):
    if type(in2) == str: #From variable
        return "scoreboard players operation "+in1+" system = "+in2+" system"
    else: #From immediate number 
        return "scoreboard players set "+in1+" system "+str(in2)

def push(in1):
    if type(in1) == str: #From variable
        return ("execute store result storage "+ NAMESPACE +":data TMP int 1 run scoreboard players get "+ in1 +" "+ SCOREBOARD +"\n"
                "data modify storage "+ NAMESPACE +":data Stack prepend from storage "+ NAMESPACE +":data TMP")

    elif type(in1) == int: #From immediate number 
        return "data modify storage "+ NAMESPACE +":data Stack prepend value " + str(in1)

def pop(in1): #To variable
    return ("execute store result score "+ in1 +" system run data get storage "+ NAMESPACE +":data Stack[0] 1\n"
            "data remove storage "+ NAMESPACE +":data Stack[0]") 

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
    return "function " + NAMESPACE + ":" + in1

def jmpCnd(opcode, in1, in2, codeblock):
    code = {
        8 : "=",
        9 : ">",
        10: ">=",
        11: "<",
        12: "<=",
        13: "!="
    }

    if opcode == 13:
        if type(in2) != int:
            return "execute unless score "+ in1 +" system "+ code[opcode] +" "+ in2 + " system run function "+ NAMESPACE +":" + codeblock
        else:
            return "execute unless score "+ in1 +" system matches "+ in2 +" run function "+ NAMESPACE +":" + codeblock

    else:
        if type(in2) != int:
           return "execute if score "+ in1 +" system "+ code[opcode] +" "+ in2 + " system run function "+ NAMESPACE +":" + codeblock
        else:
            return "execute if score "+ in1 +" system "+ getMatchcode(opcode, in2) + " system run function "+ NAMESPACE +":" + codeblock

def getMatchcode(opcode, number):
    if opcode == 8: return str(number)
    if opcode == 9: str(number + 1) + ".."
    if opcode == 10:str(number) + ".."
    if opcode == 11:".." + str(number - 1)
    if opcode == 12:".." + str(number)

def generateFunctions(code, namespace, scoreboard):
    global NAMESPACE
    global SCOREBOARD
    NAMESPACE = namespace
    SCOREBOARD = scoreboard
    #input is function code

    output = ""

    for op in code:

        if op.opcode == 0: out = mov(op.modify, op.read)
        if 1 <= op.opcode <= 4: out = arithmatic(op.opcode, op.modify, op.read)
        if op.opcode == 5: out = push(op.read)
        if op.opcode == 6: out = pop(op.modify)
        if op.opcode == 7: out = call(op.read)
        if 8 <= op.opcode <= 13: out = jmpCnd(op.opcode, op.modify, op.read, op.codeblock)

        output += out + "\n"
    return output