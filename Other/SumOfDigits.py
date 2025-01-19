def sumOfDigits(n:int) -> int:
    nStr = str(n)
    if (len(nStr) == 1):
        return n
    
    currentNum = int(nStr[0])
    m = 10 ** (len(nStr) - 1)
    return currentNum + sumOfDigits(n % m)

print(f"Sum of digits 12345 is {sumOfDigits(12345)}")