# naive approach:
#def fib (n):
#    if n <= 2:
#        return 1
#    return fib(n-1) + fib(n-2)

#memoisation
# HashMap - keys will be arg to function, values will be returned
def fib (n, memo = {}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    memo[n] =  fib(n-1, memo) + fib(n-2, memo) 
    return memo[n]


# Bottom-up solution
# memo is a list
def fibBU (n):
    memo = {}
    for i in range(1, n+1):
        if i <= 2:
            f = 1
        else:
            f =  memo[i-1] + memo[i-2]
        memo[i] = f
    return memo[n]

print(fib(50))
print(fibBU(50))
print(fib(20))
print(fibBU(20))
print(fib(10))
print(fibBU(10)) 