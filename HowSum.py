# Given a target value and an array A of int values.
# return an array of the number combination if the target value can be gotten from
# the sum of any int(s) in the array return null otherwise.
# * is "spread operator"
# brute force method

def HowSum(target, A, memo = {}):
    if target in memo:
        return memo[target]

    if target == 0:
        return []

    if target < 0:
        return None

    for num in A:
        remainder = target - num 
        result = HowSum(remainder, A, memo)
        if result != None:
            memo[target] =  [*result, num]
            return memo[target]
    memo[target] = None
    return None

#print(HowSum(7, [2, 3]))

#print(HowSum(7, [5, 3, 4, 7]))

print(HowSum(7, [2, 4]))

#print(HowSum(8, [2, 3, 5]))

#print(HowSum(300, [7, 14]))