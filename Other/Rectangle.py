def rectangle(kar:str, l:int, w:int):
    if (w == 1):
        print(kar * l)
        return 
    
    print(kar * l)
    rectangle(kar, l, w-1)

print("Rectangle * with dimension 8x3:")
rectangle("*", 8, 3)
print("\nRectangle x with dimension 5x10:")
rectangle("x", 5, 10)
