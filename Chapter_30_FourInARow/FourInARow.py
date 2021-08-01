WIDTH = 9
HEIGHT = 8
LEFT_INDENT = 10

PLAYER_1 = 'X'
PLAYER_2 = 'O'


def main():
    print('Four in a Row')

    board = []
    for y in range(HEIGHT):
        if y in [0, HEIGHT-1]:
            board.append(list('+-------+'))
        else:
            board.append(list('|.......|'))
    print_board(board)

    playerTurn = PLAYER_1
    while True:
        playerMove = player_move(board, playerTurn)
        if playerMove == 'QUIT':
            break

        for y in range(HEIGHT-2, 0, -1):
            if board[y][playerMove] == '.':
                board[y][playerMove] = playerTurn
                break

        print_board(board)

        if check_win(board, playerTurn):
            print(f'Player {playerTurn} win!')
            break

        playerTurn = PLAYER_2 if playerTurn == PLAYER_1 else PLAYER_1


def print_board(board):
    print(' '*(LEFT_INDENT+1) + '1234567')
    for line in board:
        print(' '*LEFT_INDENT + ''.join(line))


def player_move(board, player):
    print(f'Player {player}, enter a column or QUIT:')
    while True:
        move = input('> ').upper()
        if move.isdigit() and eval('1<=' + move + '<=7'):
            move = int(move)
            column = [board[row][move] for row in range(HEIGHT - 1)]
            if '.' in column:
                break
            print(f'Column {move} is full. ', end='')
        if move == 'QUIT':
            break

        print('Invalid input.')

    return move


def check_win(board, mark):
    # Four in a column
    for col in range(1, WIDTH):
        for row in range(1, HEIGHT-4):
            markList = [board[row+i][col] for i in range(4)]
            if all([m == mark for m in markList]):
                return True

    # Four in a row
    for row in range(HEIGHT-1, 0, -1):
        for col in range(1, WIDTH-4):
            markList = [board[row][col+i] for i in range(4)]
            if all([m == mark for m in markList]):
                return True

    # Four in a diagonal
    for row in range(1, HEIGHT-4):
        for col in range(1, WIDTH-4):
            # Right
            markList = [board[row+i][col+i] for i in range(4)]
            if all([m == mark for m in markList]):
                return True

            # Left
            markList = [board[row+i][col+3-i] for i in range(4)]
            if all([m == mark for m in markList]):
                return True


if __name__ == "__main__":
    main()
