def triangleLayer(side:int):
    if (side < 0):
        print("Invalid side, please enter a valid side")
        return
    if (side == 0):
        return
    if (side == 1):
        print("*")
        return

    print("*", end="")
    triangleLayer(side-1)
    return

def rightSideTriangle(side: int):
    if (side < 0):
        print("Invalid side, please enter a valid side")
        return
    if (side == 0):
        return
    if (side == 1):
        triangleLayer(1)
        return
    
    rightSideTriangle(side-1)
    triangleLayer(side)

rightSideTriangle(10)