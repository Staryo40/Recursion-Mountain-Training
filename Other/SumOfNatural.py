def sumOfNatural(n:int) -> int:
    if (n <= 0):
        print("Invalid input.")
        return
    if (n == 1):
        return 1
    return n + sumOfNatural(n-1)

print(f"Sum of first 6 natural numbers = {sumOfNatural(6)}")