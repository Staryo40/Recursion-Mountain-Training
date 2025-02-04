# Input: sum = 4, coins[] = [1, 2, 3]
# Output: 4
# Explanation: There are four solutions: [1, 1, 1, 1], [1, 1, 2], [2, 2] and [1, 3]
def coinChange(coins:list[int], sum:int) -> list[list[int]]:
    res = []
    for i in range(len(coins)):
        res += subCoinCombination(coins, sum, [coins[i]])
    return res


def subCoinCombination(coins, targetSum, currentSet) -> list[list[int]]:
    if (sumOfList(currentSet) == targetSum):
        return [currentSet]
    elif (sumOfList(currentSet) < targetSum):
        res = []
        lastCoin = currentSet[len(currentSet)-1]
        for i in range(len(coins)):
            if (coins[i] <= lastCoin):
                newList = currentSet.copy()
                newList.append(coins[i])
                res += subCoinCombination(coins, targetSum, newList)
        return res
    else: # currentSet sum is bigger than targetSum
        return []

def sumOfList(l) -> int:
    sum = 0
    for i in range(len(l)):
        sum += l[i]
    return sum
    
res = coinChange([1,2,3], 7)
print(res)