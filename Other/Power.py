def power(base:int, exp:int) -> int:
    if (exp == 0):
        return 1
    
    sign = False
    if (exp < 0):
        exp = -exp
        sign = True
    
    result = base * power(base, exp-1)

    if sign:
        return round(1/result, 10)
    else:
        return result

print(f"5^3 = {power(5,3)}")
print(f"-5^(3) = {power(-5,3)}")
print(f"5^(-3) = {power(5,-3)}")
print(f"-5^(-3) = {power(-5,-3)}")