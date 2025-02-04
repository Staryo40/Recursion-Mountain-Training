def product(x:int, y:int) -> int:
    if (x < y):
        small = x
        big = y
    else:
        small = y
        big = x

    if (small == 0):
        return 0
    if (small == 1):
        return big
    
    if (small == x):
        return big + product(x-1, y)
    else:
        return big + product(x, y-1)
    
print(f"Product of 7 * 8 = {product(7, 8)}")
    