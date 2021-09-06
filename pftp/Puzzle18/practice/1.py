


def rFibMemorize(x,memo):
    if x == 0:
        return 0
    elif x == 1:
        return 1
    elif x in memo:
        return memo[x]
    else:
        result = rFibMemorize(x-1,memo) + rFibMemorize(x-2,memo)
        memo[x] = result
        return result


def iFib(x):
    if x < 2:
        return x
    else:
        f, g = 0, 1
        for i in range(x-1):
            f, g = g, f + g
        return g
# print(iFib(30))
print(rFibMemorize(30, {}))