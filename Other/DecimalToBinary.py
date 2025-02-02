def decimalToBinary(n:int) -> int:
    if (n < 0):
        print("Invalid input.")
        return
    if (n == 0 or n == 1):
        return n
    x = 1
    counter = 0
    while (x < n):
        if (x*2 > n):
            break
        else:
            x *= 2
            counter += 1

    return 10 ** counter + decimalToBinary(n % x)

print(f"Binary of 4 = {decimalToBinary(4)}")
print(f"Binary of 7 = {decimalToBinary(7)}")
print(f"Binary of 36 = {decimalToBinary(36)}")
print(f"Binary of 69 = {decimalToBinary(69)}")