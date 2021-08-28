#Programming for the Puzzled -- Srini Devadas
#Hip To Be a Square Root
#Given a list, find an element in the list using sequential, iterative search
#Given a sorted list, find an element in the list using binary search

NOTFOUND = -1
Ls = [2, 3, 5, 7, 11, 13, 17, 19, 23, 26, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, \
     71, 73, 79, 83, 89, 97]

def lsearch(L, value):
    for i in range(len(L)):
        if L[i] == value:
            print ("Found at location", i)
            return i
    print ("Could not find the value", value)
    return NOTFOUND



def bsearch(L, value, min_len):
    lo, hi = 0, len(L)-1
    while hi - lo > min_len:
        mid = (lo + hi) // 2
##        #To trace execution
##        print ("LOW = ", lo, "HIGH = ", hi, "MID = ", mid)
        if L[mid] < value:
            lo = mid + 1
        elif value < L[mid]:
            hi = mid - 1
        else:
            print ("Found at location", mid)
            return mid
    else:
        while lo <= hi:
            if L[lo] < value:
                lo += 1
            elif L[lo] > value:
                break
            else:
                print ("Found at location", lo)
                return mid
    print ("Could not find the value", value)
    return NOTFOUND


# lsearch(Ls, 26, 10)
bsearch(Ls, 26, 6)
# bsearch(Ls, 29)
