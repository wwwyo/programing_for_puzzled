def hanoi(offset, numRings, startPeg, middlePeg, endPeg):
    
    numMoves = 0
    if numRings > 0:
        numMoves += hanoi(offset, numRings - 1, startPeg, endPeg, middlePeg)
        print ('Move ring', numRings + offset, 'from peg', startPeg, 'to peg', endPeg)
        numMoves += 1
        numMoves += hanoi(offset, numRings - 1, middlePeg, startPeg, endPeg)
    return numMoves

def hanoi4pegs(numRings, startPeg, middlePeg, endPeg, fourthPeg):

    numMoves = 0
    numMoves += hanoi(0, numRings // 2 , startPeg, middlePeg, fourthPeg)
    numMoves += hanoi(numRings // 2, numRings // 2, startPeg, middlePeg, endPeg)
    numMoves += hanoi(0, numRings //2, fourthPeg, middlePeg, endPeg)

hanoi4pegs(8, 1, 2, 3, 4)