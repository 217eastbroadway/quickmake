def fixPath(path):
    if not path.endswith("/") and not path.endswith("\\"):
        return path + '/'
    
    return path

def getObjectFiles(compileQueue):
    objectQueue = ""

    for file in compileQueue:
        temp = file.split("/")[-1];
        temp = temp[slice(0, len(temp)-4)]
        temp += ".o"
        objectQueue += temp + ' '

    return objectQueue