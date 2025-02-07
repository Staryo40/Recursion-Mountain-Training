def removeAdjacentDuplicate(s:str) -> str:
    return RAD(s, 0)

def RAD(s:str, cur:int) -> str:
    if (len(s) == 0 or len(s) == 1 or cur == len(s)-1):
        return s
    
    deleted = False
    firstDup = -1
    i = cur
    s_new = s
    while (i < len(s_new)-1):
        if (s_new[i] == s_new[i+1]):
            if (firstDup == -1):
                firstDup = i
                deleted = True
            char = s_new[i]
            while (i < len(s_new) and s_new[i] == char):
                s_new = s_new[:i] + s_new[(i+1):]
        else:
            i += 1

    if (deleted):
        if (firstDup == 0):
            return RAD(s_new, firstDup)
        else:
            return RAD(s_new, firstDup-1)
    else:
        return s_new
    
print(f"Cleansed 'geeksforgeek' = '{removeAdjacentDuplicate("geeksforgeek")}'")
print(f"Cleansed 'abccbccba' = '{removeAdjacentDuplicate("abccbccba")}'")
print(f"Cleansed 'zxxzykk' = '{removeAdjacentDuplicate("zxxzykk")}'")

        