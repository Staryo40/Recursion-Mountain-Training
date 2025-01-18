def GCD(a:int, b:int) -> int:
    if (b > a):
        bucket = b
        b = a
        a = bucket
    if (b == 0):
        return a
    
    return GCD(b, a % b)

print(f"GCD of 56 and 98 is {GCD(98, 56)}")