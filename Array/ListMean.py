def listMean(l:list[int]) -> int:
    if (len(l) == 1):
        return l[0]
    return (l[0] + (listMean(l[1:])*(len(l)-1)))/len(l)

l = [5,6,7,8,9]
print(listMean(l))
