import random

def createRandomArray(length, lowerbound, upperbound):
    array = []
    for i in range(length):
        currentNum = random.randint(lowerbound, upperbound)
        array.append(currentNum)
    return array