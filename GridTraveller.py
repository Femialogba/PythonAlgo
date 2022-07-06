# Say that you are a traveler on a 2D grid.
# You begin in the top-left corner and 
# your goal is to travel to the bottom-right corner. 
# You may only move down or right. 


# In how many ways can you travel to the goal
# on a grid with dimensions m * n?

#def gridTraveller(m, n):
#    if (m == 1) and (n == 1):
#        return 1
#    if (m == 0) or (n == 0):
#        return 0
#    return gridTraveller(m - 1, n) + gridTraveller(m, n - 1)

def gridTraveller(m, n, memo = {}):
    #are the args in the memo
    key = m,n

    if key in memo:
        return memo[key]
    if (m == 1) and (n == 1):
        return 1
    if (m == 0) or (n == 0):
        return 0
    memo[key] = gridTraveller(m - 1, n, memo) + gridTraveller(m, n - 1 , memo)
    return memo[key]

# Bottom-up solution
def gridTraveller(m, n):
    memo = {}
    for i in range(1, n+1 and m+1):
        if i == 0:
            return 0
        if i == 1:
            return 1
        f = memo[i - 1] + memo[i]
        memo[i] = f


print(gridTraveller(1, 1))
print(gridTraveller(2, 3))
print(gridTraveller(3, 2))
print(gridTraveller(18, 18))