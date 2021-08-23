import random
import sys

BLANK = '  '


def get_new_board():
    return [[BLANK if (i == 4 and j == 3) else str(i+4*j).ljust(2) for i in range(1, 5)] for j in range(4)]


def find_blank_space(board):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if board[row][col] == BLANK:
                return (row, col)


def make_move(board, move):
    bRow, bCol = find_blank_space(board)

    if move == 'W':
        board[bRow][bCol], board[bRow +
                                 1][bCol] = board[bRow+1][bCol], board[bRow][bCol]
    elif move == 'S':
        board[bRow][bCol], board[bRow -
                                 1][bCol] = board[bRow-1][bCol], board[bRow][bCol]
    elif move == 'A':
        board[bRow][bCol], board[bRow][bCol +
                                       1] = board[bRow][bCol+1], board[bRow][bCol]
    elif move == 'D':
        board[bRow][bCol], board[bRow][bCol -
                                       1] = board[bRow][bCol-1], board[bRow][bCol]


def make_random_move(board):
    blankRow, blankCol = find_blank_space(board)
    validMoves = []
    if blankRow != 3:
        validMoves.append('W')
    if blankRow != 0:
        validMoves.append('S')
    if blankCol != 3:
        validMoves.append('A')
    if blankCol != 0:
        validMoves.append('D')

    make_move(board, random.choice(validMoves))


def initialize_puzzle(randomMoves=200):
    board = get_new_board()

    for _ in range(randomMoves):
        make_random_move(board)
    return board


def display_board(board):
    labels = [cell for row in board for cell in row]
    boardTemplate = '''
+------+------+------+------+
|      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |
+------+------+------+------+
|      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |
+------+------+------+------+
|      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |
+------+------+------+------+
|      |      |      |      |
|  {}  |  {}  |  {}  |  {}  |
|      |      |      |      |
+------+------+------+------+
'''.format(*labels)
    print(boardTemplate)


def get_player_move(board):
    blankRow, blankCol = find_blank_space(board)
    w = 'W' if blankRow != 3 else ' '
    s = 'S' if blankRow != 0 else ' '
    a = 'A' if blankCol != 3 else ' '
    d = 'D' if blankCol != 0 else ' '

    while True:
        print(f'                          ({w})')
        print(f'Enter WASD (or QUIT): ({a}) ({s}) ({d})')
        playerMove = input('> ').upper()

        if playerMove == 'QUIT':
            sys.exit()
        if playerMove in (w+s+a+d).replace(' ', ''):
            return playerMove


if __name__ == "__main__":
    print('''Sliding Tile Puzzle
    
    Use the AWSD keys to move the tiles back into their original order:
            1  2  3  4
            5  6  7  8
            9 10 11 12
           13 14 15 ''')
    input('Press Enter to begin....')

    gameBoard = initialize_puzzle()

    while True:
        display_board(gameBoard)
        playerMove = get_player_move(gameBoard)
        make_move(gameBoard, playerMove)

        if gameBoard == get_new_board():
            display_board(gameBoard)
            print('You won!')
            sys.exit()
