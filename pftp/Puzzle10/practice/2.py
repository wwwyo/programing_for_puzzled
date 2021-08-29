#Programming for the Puzzled -- Srini Devadas
#A Profusion of Queens
#Given the dimension of a square "chess" board, call it N, find a placement
#of N queens such that no two Queens attack each other using recursive search

#This procedure initializes the board to be empty, calls the recursive N-queens
#procedure and prints the returned solution
location = [-1, -1, 4, -1, -1, -1, -1, 0, -1, 5]
def nQueens(size):
    board = [-1] * size
    rQueens(board, 0, size)


#This procedure checks that the most recently placed queen on column current
#does not conflict with queens in columns to the left.
def noConflicts(board, current):
    for i in range(current):
        if (board[i] == board[current]):
            return False
        if (current - i == abs(board[current] - board[i])):
            return False
    return True 


#This procedure places a queens on the board on a given column so it does
#not conflict with the existing queens, and then calls itself recursively
#to place subsequent queens till the requisite number of queens are placed
def rQueens(board, current, size):
    if (current == size):
        is_correct = True
        for j in range(size):
            if location[j] != -1 and location[j] != board[j]:
                is_correct = False

        if is_correct:
            board_2 = [['.' for _ in range(size)] for _ in range(size)]
            for col_num,i in enumerate(board):
                board_2[i][col_num] = 'Q'
            for row in board_2:
                print(' '.join(row))
            print('-----------------------')
    else:
        for i in range(size):
            board[current] = i
            if (noConflicts(board, current)):
                rQueens(board, current + 1, size)
        return False


nQueens(10)
