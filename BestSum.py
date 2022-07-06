 # Write a function 'BestSum(target, nums)' that takes
 # in a target value and an array of numbers as args

 # The function should return an array containing the 
 # shortest combination of numbers that add up to exactly the target.

 # if there's a tie for the shortest combination, 
 # you may return any one of the shortest.

 # * is "spread operator"

# brute force method
# def BestSum(target, A):
#     if target == 0:
#         return []
#     if target < 0:
#         return None
#     shortestcombination = None
#     for num in A:
#         remainder = target - num
#         remcombination = BestSum(remainder, A)
#         if remcombination != None:
#             combination = [*remcombination, num]
#             if shortestcombination == None or (len(combination) < len(shortestcombination)):
#                 shortestcombination = combination
    
#     return shortestcombination

# Memoised method
def BestSum(target, A, memo = {}):
    if target in memo:
        return memo[target]
    if target == 0:
        return []
    if target < 0:
        return None
    shortestcombination = None
    for num in A:
        remainder = target - num
        remcombination = BestSum(remainder, A)
        if remcombination != None:
            combination = [*remcombination, num]
            if shortestcombination == None or (len(combination) < len(shortestcombination)):
                shortestcombination = combination
    memo[target] = shortestcombination
    return memo[target]


# m = target
# n = len(nums)

# Brute force
# time: O(n^m * m)
# space: O(m^2)

# memoised
# time: O(m^2 * n)
# space: O(m^2)   

# print(BestSum(7, [2, 3]))
# print(BestSum(7, [5, 3, 4, 7]))
# print(BestSum(8, [2, 3, 5]))
print(BestSum(8, [1, 4, 5]))
print(BestSum(100, [1, 2, 5, 25]))
