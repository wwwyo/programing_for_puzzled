#Programming for the Puzzled -- Srini Devadas
#Hip To Be a Square Root
#Given a number, find the square root to within a given error
#Use bisection search.

def calcX(x):
    return x ** 3 + x ** 2 -11

def bisectionSearchForSquareRoot(epsilon):
    numGuesses = 0
    low = -10.0
    high = 10.0
    x = (high + low)/2.0

    ans = calcX(x)
    while abs(ans) >= epsilon:
        if ans >= epsilon:
            high = x
        else:
            low = x
        x = (high + low) / 2.0
        ans = calcX(x)
        numGuesses += 1
        #print('low = ', low, 'high = ', high, 'guess = ', ans)
    print ('numGuesses =', numGuesses)
    print (x, 'is close to square root of x ** 3 + x ** 2 - 11')

    return

bisectionSearchForSquareRoot(.01)
# bisectionSearchForSquareRoot(0.25, .01)

