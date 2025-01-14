import random

def createRandomArray(length, lowerbound, upperbound):
    array = []
    for i in range(length):
        currentNum = random.randint(lowerbound, upperbound)
        array.append(currentNum)
    return array

def mergeSort(l):
    if (len(l) == 1):
        return l
    
    firsthalf = l[0:(len(l)//2)]
    secondhalf = l[len(l)//2:len(l)]

    sortedfirst = mergeSort(firsthalf)
    sortedsecond = mergeSort(secondhalf)

    res = []
    
    for i in range(len(l)):
        if (len(sortedfirst) == 0):
            res.append(sortedsecond[0])
            sortedsecond = sortedsecond[1:]
        elif (len(sortedsecond) == 0):
            res.append(sortedfirst[0])
            sortedfirst = sortedfirst[1:]
        elif (sortedfirst[0] <= sortedsecond[0]):
            res.append(sortedfirst[0])
            sortedfirst = sortedfirst[1:]
        else:
            res.append(sortedsecond[0])
            sortedsecond = sortedsecond[1:]
    
    return res

generatedArray = createRandomArray(10, 1, 100)
print(f"Generated array = {generatedArray}")
print(f"Sorted array = {mergeSort(generatedArray)}")