BLANK = ' '
PLAYER_X = 'X'
PLAYER_O = 'O'


def main():
    print('Welcome to Tic-Tac-Toe!')
    print()

    gameBoard = [[BLANK for _ in range(3)] for _ in range(3)]
    turn = PLAYER_X
    print_board(gameBoard)

    while True:
        print(f"What is {turn}'s move? (1-9)")
        while True:
            playerMove = input('> ')
            if playerMove.isdigit() and eval(f'1<={playerMove}<=9'):
                playerMove = int(playerMove) - 1
                row, col = playerMove // 3, playerMove % 3
                if gameBoard[row][col] == BLANK:
                    gameBoard[row][col] = turn
                    break
                else:
                    print('Space has been filled')
            else:
                print('Invalid input')

        print_board(gameBoard)
        if check_winner(gameBoard, turn):
            print(f'Player {turn} has won the game!')
            break
        if check_board_full(gameBoard):
            print('The game is a tie!')
            break

        turn = PLAYER_O if turn == PLAYER_X else PLAYER_X

    print('Thanks for playing!')


def print_board(board):
    for idx, row in enumerate(board):
        possibleNum = [3*idx+i+1 if value ==
                       BLANK else BLANK for i, value in enumerate(row)]
        print(' '*5 + '{}|{}|{}'.format(*row) + ' ' *
              3 + '{} {} {}'.format(*possibleNum))
        if idx != 2:
            print(' '*5 + '-+-+-')


def check_winner(board, player):
    # Horizontal
    for row in board:
        if row.count(player) == 3:
            return True

    # Vertical
    for col in list(map(list, zip(*board))):
        if col.count(player) == 3:
            return True

    # Diagonal
    if (board[0][0] == board[1][1] == board[2][2] == player) or (board[0][2] == board[1][1] == board[2][0] == player):
        return True

    return False


def check_board_full(board):
    return [value for row in board for value in row].count(' ') == 0


if __name__ == "__main__":
    main()
