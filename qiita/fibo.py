idx = 3 #30番目のフィボナッチ数を求める

def recursiveFibonacci(idx, memo = {}):
    if idx <= 0: return 0
    if idx == 1: return 1

    if not idx in memo:
        memo[idx] = recursiveFibonacci(idx-1, memo) + recursiveFibonacci(idx-2, memo)
    return memo[idx]

print(recursiveFibonacci(idx-1))