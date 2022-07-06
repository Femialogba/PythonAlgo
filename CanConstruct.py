# Write a function CanConstruct(target, wordBank) that 
# accepts a target string and an array of strings.
# The function should return true if the target can be
# constructed by concatenating elements of the wordBank array
# elements of wordBank can be reused.
def CanConstruct(target, wordBank, memo = {}):
    if target in memo:
        return memo[target]
    if target == "":
        return True
    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word) :]
            if CanConstruct(suffix, wordBank, memo) == True:
                memo[target] = True
                return memo[target]
    memo[target] = False   
    return memo[target]

#Brute Force
# m = target.length
# n = wordBank.length
# Time: O(n*m)
# Space: O(m^2)

#Memoized
# Time: O(n*m^2)
# Space: O(m^2)

print(CanConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]))
print(CanConstruct("eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeef",
                ["e", "ee", "eee", "eeee", 
                "eeeee", "eeeeee", "eeeeeee"]))

    

