def maxOfArray(l:list[int]) -> int:
    if (len(l) == 0):
        print("Array is empty, no minimum.")
        return
    if (len(l) == 1):
        return l[0]
    
    tailMin = maxOfArray(l[1:])
    if (l[0] > tailMin):
        return l[0]
    else:
        return tailMin

arr = [3,5,10,2,7]
print(f"Maximum of arr is = {maxOfArray(arr)}")