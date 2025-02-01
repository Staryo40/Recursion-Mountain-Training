def print1toNPure(n:int):
    print1toN(n, n-1)

def print1toN(n:int, counter:int):
    if (counter == 0):
        print(n)
        return
    print(n-counter)
    print1toN(n, counter-1)

print1toNPure(7)