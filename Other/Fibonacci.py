def fibElement(id: int) -> int:
    if (id == 0):
        return 0
    if (id == 1):
        return 1
    
    return fibElement(id-1) + fibElement(id-2)

def printFibSequence(id: int):
    for i in range(id+1):
        if (i == id):
            print(fibElement(i))
        else:
            print(fibElement(i), end=" ")

print(f"The 8-th element of fibonacci = {fibElement(8)}")
print("The fibonacci sequence up to the 8-th element = ", end="")
printFibSequence(8)