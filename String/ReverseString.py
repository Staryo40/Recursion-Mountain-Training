def reverseString(s:str) -> str:
    if (len(s) == 1 or len(s) == 0):
        return s
    return reverseString(s[1:]) + s[0]

print(f"Reverse of 'overlord' = {reverseString("overlord")}")