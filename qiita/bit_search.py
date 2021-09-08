# https://atcoder.jp/contests/abc045/tasks/arc061_a


s = '125'

answer = 0
# bitに変換して探索
for i in range(2 ** (len(s)-1)):
    formula = [''] * len(s)
    for j in range(len(s)):
        if i >> j & 1:
            formula[len(s)-j-2] = '+'
        else:
            formula[len(s)-j-2] = ''

    calc = ''
    for i, j in zip(s, formula):
        calc += i + j
    answer += eval(calc)

print(answer)
