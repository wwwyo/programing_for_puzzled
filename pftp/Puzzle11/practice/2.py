
def recursive(x,low_i, high_i,low_j, high_j,t):
    i = (low_i + high_i)//2
    j = (low_j + high_j)//2
    if (high_i <= low_i or high_j <= low_j):
        if t[i][j] == x:
            return print(f"{i+1}行{j+1}列")
    else:
        n = (t[i][j])
        if n > x:
            recursive(x,low_i,i-1,low_j,j-1,t)
            recursive(x,low_i,i-1,j+1,high_j,t)
            recursive(x,i+1,high_i,low_j,j-1,t)
        elif n < x:
            recursive(x,i+1,high_i,j+1,high_j,t)
            recursive(x,low_i,i-1,j+1,high_j,t)
            recursive(x,i+1,high_i,low_j,j-1,t)
        else:
            return print(f"{i}行{j}列")

def findNum(x, t):
    i = len(t)-1
    j = len(t[0])-1
    recursive(x,0,i,0,j,t)
    


T = [[1,4,7,11,15],
     [2,5,8,12,19],
     [3,6,9,16,22],
     [10,13,14,17,24],
     [18,21,23,26,30]]


findNum(21,T)

