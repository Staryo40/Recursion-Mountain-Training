def createSetList(el:int) -> list[int]:
    res = []
    for i in range (el):
        res.append(i+1)
    return res

def getSubsetList(l:list[int]) -> list[list[int]]:
    if (len(l) == 0):
        return [[]]
    
    current = [l[0]]
    beforeList = getSubsetList(l[1:])
    currentList = []

    for i in range(len(beforeList)):
        newelement = beforeList[i] + current
        currentList.append(newelement)
    
    return beforeList + currentList

l = createSetList(3)
print(l)
print(getSubsetList(l))