#Programming for the Puzzled -- Srini Devadas
#The Towers of Brahma with a Twist
#Given n rings arranged from bigger at the bottom to smaller at the top on
#a peg, move the rings to another peg, utilizing a 3rd peg. ALl 3 pegs
#are assumed be on a line.
#The standard problem has no other constraints
#The variant problem disallows the move of a ring between non-adjacent pegs

#This procedure solves the Towers of Hanoi problem
def hanoi(numRings, startPeg, endPeg):
    numMoves = 0
    if numRings > 0:
        numMoves += hanoi(numRings-1, startPeg, endPeg)
        numMoves += hanoi(numRings -1, endPeg, 6 - startPeg-endPeg)
        print ('Move ring', numRings, 'from peg', startPeg, 'to peg', endPeg)
        numMoves += 1
        numMoves += hanoi(numRings -1 , 6-startPeg-endPeg, startPeg)
        numMoves += hanoi(numRings-1, startPeg, endPeg)
        # if numRings == 3:
        #     numMoves += hanoi(numRings-1, startPeg, endPeg)
        # else:
        #     print ('Move ring', numRings, 'from peg', endPeg, 'to peg', 6-startPeg-endPeg)
        #     numMoves += hanoi(numRings-1, startPeg, endPeg)
        #     numMoves += hanoi(numRings-1, endPeg, 6-startPeg-endPeg)
    return numMoves

#hanoi(3, 1, 3)

print(hanoi(3, 1, 2))
