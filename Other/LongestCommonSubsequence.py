def LCS(s1:str, s2: str) -> int:
    subsequence1 = subsequence(s1)
    subsequence2 = subsequence(s2)

    res = 0
    for sub1 in subsequence1:
        for sub2 in subsequence2:
            if (sub1 == sub2):
                if (len(sub1) > res):
                    res = len(sub1)
                break
    return res

def subsequence(s:str) -> list[str]:
    if (len(s) == 0):
        return []
    
    before = subsequence(s[1:])
    currentChar = s[0]

    if (len(before) == 0):
        return [currentChar]
    
    new = [currentChar]
    for sub in before:
        temp = currentChar + sub
        temp = ''.join(temp)
        new.append(temp)

    return before + new

print(f"LCS of 'ABC' and 'ACD' = {LCS("ABC", 'ACD')}")
print(f"LCS of 'AGGTAB' and 'GXTXAYB' = {LCS("AGGTAB", 'GXTXAYB')}")
print(f"LCS of 'ABC' and 'CBA' = {LCS("ABC", 'CBA')}")
