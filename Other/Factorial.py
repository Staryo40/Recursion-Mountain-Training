def factorial(n:int) -> int:
    if (n == 0):
        return 1
    
    return n * factorial(n-1)

print(f"5! = {factorial(5)}")
print(f"8! = {factorial(8)}")
print(f"10! = {factorial(10)}")