def LCSLen(s1:str, s2: str) -> int:
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

def LCS(s1:str, s2: str) -> list[str]:
    n = LCSLen(s1, s2)

    subsequence1 = subsequence(s1)
    subsequence2 = subsequence(s2)

    res = []
    for sub1 in subsequence1:
        if (len(sub1) == n and sub1 not in res):
            if sub1 in subsequence2:
                res.append(sub1)
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

print(f"LCS of 'ABC' and 'ACD' has the length {LCSLen("ABC", 'ACD')} which are {LCS("ABC", 'ACD')}")
print(f"LCS of 'AGGTAB' and 'GXTXAYB' has the length {LCSLen("AGGTAB", 'GXTXAYB')} which are {LCS("AGGTAB", 'GXTXAYB')}")
print(f"LCS of 'ABC' and 'CBA' has the length {LCSLen("ABC", 'CBA')} which are {LCS("ABC", 'CBA')}")
