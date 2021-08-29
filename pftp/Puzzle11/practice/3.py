T = [[1,4,7,11,15],
     [2,5,8,12,19],
     [3,6,9,16,22],
     [10,13,14,17,24],
     [18,21,23,26,30]]
size = len(T)
def recursive(x,t):
    if len(t) == 1 and len(t[0]) == 1:
        return print('False')
    else:
        if t[0][-1] > x:
            for row in t:
                row.pop(-1)
            recursive(x, t[:])
        elif t[0][-1] < x:
            recursive(x,t[1:][:])
        else:
            return print(f'{size - len(t)+1}行{len(t[0])}列')

def findNum(x, t):
    recursive(x,t)
    





findNum(21,T)