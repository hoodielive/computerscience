# There's a staircase with N steps, and you can climb 1 or 2 steps at a time. Given N, write a 
# function that returns the number of unique ways you can climb the staircase. 
# The order of the steps matters.
# For example, if N is 4, then there are 5 unique ways:
# 1, 1, 1, 1
# 2, 1, 1
# 1, 2, 1
# 1, 1, 2
# 2, 2
# What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a 
# set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time. 
# Generalize your function to take in X.

# slow way
def staircase(n):
    if n <= 1:
        return 1
    return staircase(n-1) + staircase(n-2)

print(staircase(4))

# faster 
def staircase(n):
    a, b = 1, 2
    for _ in range(n - 1):
        a, b = b, a + b
    return a
print(staircase(4))

# very slow
def staircase(n, X):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else: 
        return sum(staircase(n - x, X) for x in X)

staircase(4, 3)

# speed it up with dynamic programming
def staircase(n, X):
    cache = [0 for _ in range(n + 1)]
    cache[0] = 1 
    for i in range(1, n + 1):
        cache[i] += sum(cache[i - x] for x in X if i - x >= 0)
    return cache[n]
staircase(4, 3)
