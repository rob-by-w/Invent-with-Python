import sys
import random

BLANK = ''


def main():
    print('Twenty Forty-Eight')
    print("""
Slide all the tiles on the board in one of four directions. Tiles with
like numbers will combine into larger-numbered tiles. A new 2 tile is
added to the board on each move. You win if you can create a 2048 tile.
You lose if the board fills up the tiles before then.
    """)
    input('Press Enter to begin...')

    gameBoard = intialize_board()

    while True:
        print_board(gameBoard)
        playerMove = ask_player_move()
        gameBoard = make_move(gameBoard, playerMove)
        generate_two(gameBoard)

        if is_full(gameBoard):
            print_board(gameBoard)
            print('Game Over - Thanks for playing!')
            sys.exit()


def intialize_board():
    newBoard = {(x, y): BLANK for x in range(4) for y in range(4)}
    startingTwosPlaced = 0
    while startingTwosPlaced < 2:
        randomSpace = (random.randint(0, 3), random.randint(0, 3))
        if newBoard[randomSpace] == BLANK:
            newBoard[randomSpace] = 2
            startingTwosPlaced += 1

    return newBoard


def print_board(board):
    labels = [str(board[(x, y)]).center(5) for x in range(4) for y in range(4)]
    print("""
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|
|     |     |     |     |
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|
|     |     |     |     |
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|
|     |     |     |     |
+-----+-----+-----+-----+
|     |     |     |     |
|{}|{}|{}|{}|
|     |     |     |     |
+-----+-----+-----+-----+""".format(*labels))
    print(f'Score: {get_score(board)}')


def get_score(board):
    return sum([board[(x, y)] if board[(x, y)] != BLANK else 0 for x in range(4) for y in range(4)])


def ask_player_move():
    print('Enter move: (WASD or Q to quit)')
    while True:
        move = input('> ').upper()
        if move == 'Q':
            print('Thanks for playing!')
            sys.exit()

        if move in 'WASD':
            return move
        print('Invalid input.')


def combile_tiles_column(column):
    combinedTiles = []
    for tile in column:
        if tile != BLANK:
            combinedTiles.append(tile)

    while len(combinedTiles) < 4:
        combinedTiles.append(BLANK)

    for i in range(3):
        if combinedTiles[i] == combinedTiles[i+1]:
            combinedTiles[i] *= 2
            for aboveIdx in range(i+1, 3):
                combinedTiles[aboveIdx] = combinedTiles[aboveIdx + 1]
            combinedTiles[3] = BLANK
    return combinedTiles


def make_move(board, move):
    if move == 'W':
        allColumnsSpaces = [[(row, col) for row in range(4)]
                            for col in range(4)]
    elif move == 'S':
        allColumnsSpaces = [[(row, col)
                             for row in range(3, -1, -1)] for col in range(4)]
    elif move == 'A':
        allColumnsSpaces = [[(row, col) for col in range(4)]
                            for row in range(4)]
    elif move == 'D':
        allColumnsSpaces = [[(row, col)
                             for col in range(3, -1, -1)] for row in range(4)]

    boardAfterMove = {}
    for columnSpaces in allColumnsSpaces:
        firstSpace, secondSpace, thirdSpace, fourthSpace = columnSpaces
        firstTile = board[firstSpace]
        secondTile = board[secondSpace]
        thirdTile = board[thirdSpace]
        fourthTile = board[fourthSpace]

        column = [firstTile, secondTile, thirdTile, fourthTile]
        combinedTilesColumn = combile_tiles_column(column)

        for i in range(4):
            boardAfterMove[columnSpaces[i]] = combinedTilesColumn[i]

    return boardAfterMove


def generate_two(board):
    while True:
        randomSpace = (random.randint(0, 3), random.randint(0, 3))
        if board[randomSpace] == BLANK:
            board[randomSpace] = 2
            return


def is_full(board):
    for x in range(4):
        for y in range(4):
            if board[(x, y)] == BLANK:
                return False
    return True


if __name__ == "__main__":
    main()
