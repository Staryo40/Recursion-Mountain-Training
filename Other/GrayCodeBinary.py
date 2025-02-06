def binaryToGrayCode(bin: int) -> int:
    if (bin < 0):
        print("Invalid binary")
        return
    if (bin == 0 or bin == 1):
        return bin
    
    firstbit = bin & 0b1
    secondbit = (bin >> 1) & 0b1
    gray = firstbit ^ secondbit
    
    prev = binaryToGrayCode(bin >> 1)
    return (prev << 1) + gray

print(f"Binary code of 11 is {bin(binaryToGrayCode(0b11))[2:]} which is 3 to {binaryToGrayCode(0b11)}")
print(f"Binary code of 1001 is {bin(binaryToGrayCode(0b1001))[2:]} which is 9 to {binaryToGrayCode(0b1001)}")
print(f"Binary code of 110011 is {bin(binaryToGrayCode(0b110011))[2:]} which is 49 to {binaryToGrayCode(0b110011)}")
print(f"Binary code of 100110 is {bin(binaryToGrayCode(0b100110))[2:]} which is 38 to {binaryToGrayCode(0b100110)}")
