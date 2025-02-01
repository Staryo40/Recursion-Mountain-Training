def printNto1(n:int):
    if (n == 1):
        print(n)
        return
    print(n)
    printNto1(n-1)

printNto1(7)