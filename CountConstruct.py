# Write a function CountConstruct(target, wordBank) that 
# accepts a target string and an array of strings.
# The function should return the number of ways that the target can
# be constructed by concatenating elements of the wordBank array
# elements of wordBank can be reused.
def CountConstruct(target, wordBank, memo = {}):
    if target in memo:
        return memo[target]
    if target == "":
        return 1
    totalWays = 0
    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word) : ]
            numWays = CountConstruct(suffix, wordBank, memo)
            totalWays = totalWays + numWays
            memo[target] = totalWays

    memo[target] = totalWays        
    return memo[target]

#Brute Force
# m = target.length
# n = wordBank.length
# Time: O(n*m)
# Space: O(m^2)

#Memoized
# Time: O(n*m^2)
# Space: O(m^2)

print(CountConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(CountConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"]))
print(CountConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
                ["e", "ee", "eee", "eeee", 
                "eeeee", "eeeeee", "eeeeeee"]))