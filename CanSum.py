# Given a target value and an array A of int values.
# return true if the target value can be gotten from
# the sum of any int(s) in the array return false otherwise.

# brute force method

def CanSum(target, A, memo = {}):
    if target in memo:
        return memo[target]

    if target == 0:
        return True

    if target < 0:
        return False

    for num in A:
        remainder = target - num 
        if CanSum(remainder, A, memo) is True:
            memo[target] = True
            return True

    memo[target] = False
    return False

A = [2, 3]
B = [5, 3, 4, 7]
C = [2, 4]
D = [2, 3, 5]
E = [7, 14]

print(CanSum(7, [2, 3]))
print(CanSum(7, [5, 3, 4, 7]))
print(CanSum(7, [2, 4]))
print(CanSum(8, [2, 3, 5]))
print(CanSum(300, [7, 14]))