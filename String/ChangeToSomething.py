def isPalindrome(x:str) -> bool:
    if (len(x) <= 1):
        return True
    if (len(x) == 2):
        return x[0] == x[1]
    
    compare = x[0] == x[len(x)-1]
    return compare and isPalindrome(x[1:(len(x)-1)])

# add comment
# more comments