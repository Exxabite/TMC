def preprocess(code):
    new = ""
    for line in code.splitlines():

        lineList = line.split()

        if len(lineList) > 1 and lineList[0] == "#include":
            print(lineList)
            line = open(lineList[1][1:-1]).read()
        new += line + "\n"
    print(new)
    return new