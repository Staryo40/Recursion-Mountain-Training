def equilateralTriangle(size:int):
    # creates an equilateral triangle with height "size" and base of "size"
    ETProper(size, size-1)

def ETProper(size: int, current:int):
    if (current == 0):
        for i in range(size):
            if (i == size-1):
                print('*')
            else:
                print('*', end=" ")
        return
    
    print(" " * current, end="")

    for i in range(size-current):
        if (i == (size-current)-1):
            print('*')
        else:
            print('*', end=" ")

    ETProper(size, current-1)
        

equilateralTriangle(2)
equilateralTriangle(4)
equilateralTriangle(8)
equilateralTriangle(16)
