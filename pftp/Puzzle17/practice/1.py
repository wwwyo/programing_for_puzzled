corpus = ['abed', 'abet', 'abets', 'abut', 'acme', 'acre',
          'acres', 'actors', 'actress', 'airmen', 'alert',
          'alerted', 'ales', 'aligned', 'allergy', 'alter',
          'altered', 'amen', 'anew', 'angel', 'angle',
          'antler', 'apt', 'bade', 'baste', 'bead',
          'beast', 'beat', 'beats', 'beta', 'betas',
          'came', 'care', 'cares', 'casters', 'castor',
          'costar', 'dealing', 'gallery', 'glean',
          'largely', 'later', 'leading', 'learnt', 'leas',
          'mace', 'mane', 'marine', 'mean', 'name', 'pat',
          'race', 'races', 'recasts', 'regally', 'related',
          'remain', 'rental', 'sale', 'scare', 'seal',
          'tabu', 'tap', 'treadle', 'tuba', 'wane', 'wean']

chToprime = {'a': 2, 'b': 3, 'c': 5, 'd': 7, 'e': 11, 'f': 13,
    'g': 17, 'h': 19, 'i': 23, 'j': 29, 'k': 31, 'l': 37, 'm': 41, 'n': 43, 
    'o': 47, 'p': 53, 'q': 59, 'r': 61, 's': 67, 't': 71, 'u': 73, 'v': 79, 
    'w': 83, 'x': 89, 'y': 97, 'z': 101 }

#This procedure computes the hash of a string recursively
def primeHash(str):
    if len(str) == 0:
        return 1
    else:
        return chToprime[str[0]] * primeHash(str[1:])

def pivotPartitionClever(lst, start, end, primeHash):
    pivot = lst[end]
    bottom = start -1
    top = end
    done = False
    while not done:
        while not done:
            bottom += 1
            if top == bottom:
                done = True
                break

            if primeHash(pivot) < primeHash(lst[bottom]):
                lst[top] = lst[bottom]
                break

        while not done:
            top -= 1
            if top == bottom:
                done = True
                break
            if primeHash(pivot) > primeHash(lst[top]):
                lst[bottom] = lst[top]
                break
    lst[top] = pivot
    return top
    

            

            

def quicksort(lst, start, end, primeHash):
    if start < end:
        split = pivotPartitionClever(lst,start,end, primeHash)
        quicksort(lst, start, split-1, primeHash)
        quicksort(lst, split+1, end, primeHash)
    return lst
    

print (corpus)
print(quicksort(corpus, 0, len(corpus) - 1, primeHash))
print (corpus)
