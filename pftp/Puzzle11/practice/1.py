

#This procedure prints a given tiled yard using letters for tiles
def printYard(yard):
    for i in range(len(yard)):
        row = ''
        for j in range(len(yard[0])):
            if yard[i][j] != EMPTYPIECE:
                row += chr((yard[i][j] % 26) + ord('A'))
            else:
                row += ' '
        print (row)


def tileFourMissingYard(n, missList):
    missYardQuads = {}
    size = 2 ** n
    for pos in missList:
        missYardQuads[2*(pos[0] >= size//2) + (pos[1] >= size//2)] = 1
    if len(missYardQuads) == 4:
        return print('Yes')
    for miss in missList:
        trominoes3 = missList[:]
        trominoes3.remove(miss)
        if (isPutTrominoes(trominoes3)):
            return print('Yes')
    return print('No')

def isPutTrominoes(missList):
    for i in range(len(missList)):
        center = missList[i]
        other1 = missList[(i + 1) % 3]
        other2 = missList[(i + 2) % 3]

        create1 = (center[0] + 1, center[1])
        create2 = (center[0] + 1, center[1] + 1)
        if (create1 == other1 and create2 == other2) or\
            (create1 == other2 and create2 == other1):
                return True
        
        create1 = (center[0], center[1] + 1)
        create2 = (center[0] + 1, center[1] + 1)
        if (create1 == other1 and create2 == other2) or\
            (create1 == other2 and create2 == other1):
                return True
            
        create1 = (center[0]+1, center[1])
        create2 = (center[0] + 1, center[1] - 1)
        if (create1 == other1 and create2 == other2) or\
            (create1 == other2 and create2 == other1):
                return True
            
        create1 = (center[0] + 1, center[1]+0)
        create2 = (center[0], center[1] + 1)
        if (create1 == other1 and create2 == other2) or\
            (create1 == other2 and create2 == other1):
                return True
    return False
    
    
tileFourMissingYard(3, [(4, 4), (1, 1), (2, 1), (1, 2)])
tileFourMissingYard(3, [(4, 4), (3, 1), (2, 1), (1, 2)])
tileFourMissingYard(3, [(3, 7), (4, 4), (4, 6), (4, 7)])