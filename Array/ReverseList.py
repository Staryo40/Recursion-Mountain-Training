from ArrayCommon import *

def reverseList(l:list[int]) -> list[int]:
    if (len(l) == 0):
        return []
    
    currentEl = l[0]
    reversed = reverseList(l[1:])
    return reversed + [currentEl]

generatedArray = createRandomArray(10, 1, 100)
print(f"Generated array = {generatedArray}")
print(f"Reversed array = {reverseList(generatedArray)}")
