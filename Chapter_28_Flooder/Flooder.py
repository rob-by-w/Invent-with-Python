import bext
import random
import sys

BOARD_WIDTH = 16
BOARD_HEIGHT = 14
MOVES_PER_GAME = 20

HEART = chr(9829)  # Character 9829 is '♥'.
DIAMOND = chr(9830)  # Character 9830 is '♦'.
SPADE = chr(9824)  # Character 9824 is '♠'.
CLUB = chr(9827)  # Character 9827 is '♣'.
BALL = chr(9679)  # Character 9679 is '•'.
TRIANGLE = chr(9650)  # Character 9650 is '▲'.

BLOCK = chr(9608)  # Character 9608 is '█'
LEFTRIGHT = chr(9472)  # Character 9472 is '─'
UPDOWN = chr(9474)  # Character 9474 is '│'
DOWNRIGHT = chr(9484)  # Character 9484 is '┌'
DOWNLEFT = chr(9488)  # Character 9488 is '┐'
UPRIGHT = chr(9492)  # Character 9492 is '└'
UPLEFT = chr(9496)  # Character 9496 is '┘'

TILE_TYPES = (0, 1, 2, 3, 4, 5)
COLORS_MAP = {0: 'red', 1: 'green', 2: 'blue',
              3: 'yellow', 4: 'cyan', 5: 'purple'}
COLOR_MODE = 'color mode'
SHAPES_MAP = {0: HEART, 1: TRIANGLE, 2: DIAMOND, 3: BALL, 4: CLUB, 5: SPADE}
SHAPE_MODE = 'shape mode'

COLOR_CMD = list('RGBYCP')
SHAPE_CMD = list('HTDBCS')


def main():
    bext.bg('black')
    bext.fg('white')
    bext.clear()

    print('Flooder')
    print()
    print('Set the upper left color/shape, which fills in all the adjacent squares of that color/shape.')
    print('Try to make the entire board the same color/shape.')

    print('Do you want to play in colorblind mode? Y/N')
    inputDisplayMode = input('> ')
    displayMode = SHAPE_MODE if inputDisplayMode.upper().startswith('Y') else COLOR_MODE

    gameBoard = get_new_board()
    movesLeft = MOVES_PER_GAME

    while True:
        display_board(gameBoard, displayMode)
        print(f'Moves left: {movesLeft}')
        playerMove = ask_for_move(displayMode)
        change_tile(playerMove, gameBoard, 0, 0)
        movesLeft -= 1

        if check_board_complete(gameBoard):
            display_board(gameBoard, displayMode)
            print('You have won!')
            break
        elif movesLeft == 0:
            display_board(gameBoard, displayMode)
            print('You have run out of moves!')
            break


def get_new_board():
    board = {}

    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            board[(x, y)] = random.choice(TILE_TYPES)

    for _ in range(BOARD_WIDTH * BOARD_HEIGHT):
        x = random.randint(0, BOARD_WIDTH - 2)
        y = random.randint(0, BOARD_HEIGHT - 1)
        board[(x + 1, y)] = board[(x, y)]

    return board


def display_board(board, mode):
    bext.fg('white')
    print(DOWNRIGHT + LEFTRIGHT * BOARD_WIDTH + DOWNLEFT)

    for y in range(BOARD_HEIGHT):
        bext.fg('white')
        print('>' if y == 0 else UPDOWN, end='')

        for x in range(BOARD_WIDTH):
            bext.fg(COLORS_MAP[board[(x, y)]])
            if mode == COLOR_MODE:
                print(BLOCK, end='')
            elif mode == SHAPE_MODE:
                print(SHAPES_MAP[board[(x, y)]], end='')

        bext.fg('white')
        print(UPDOWN)

    print(UPRIGHT + LEFTRIGHT * BOARD_WIDTH + UPLEFT)


def ask_for_move(mode):
    while True:
        bext.fg('white')
        print('Choose one of ', end='')

        if mode == COLOR_MODE:
            bext.fg('red')
            print('(R)ed ', end='')
            bext.fg('green')
            print('(G)reen ', end='')
            bext.fg('blue')
            print('(B)lue ', end='')
            bext.fg('yellow')
            print('(Y)ellow ', end='')
            bext.fg('cyan')
            print('(C)yan ', end='')
            bext.fg('purple')
            print('(P)urple ', end='')
        elif mode == SHAPE_MODE:
            bext.fg('red')
            print('(H)eart, ', end='')
            bext.fg('green')
            print('(T)riangle, ', end='')
            bext.fg('blue')
            print('(D)iamond, ', end='')
            bext.fg('yellow')
            print('(B)all, ', end='')
            bext.fg('cyan')
            print('(C)lub, ', end='')
            bext.fg('purple')
            print('(S)pade, ', end='')
        bext.fg('white')
        print('or QUIT:')

        userInput = input('> ').upper()
        if userInput == 'QUIT':
            print('Thanks for playing')
            sys.exit()
        if mode == COLOR_MODE and userInput in COLOR_CMD:
            return COLOR_CMD.index(userInput)
        if mode == SHAPE_MODE and userInput in SHAPE_CMD:
            return SHAPE_CMD.index(userInput)


def change_tile(tileType, board, x, y, charToChange=None):
    if x == 0 and y == 0:
        charToChange = board[(x, y)]
        if tileType == charToChange:
            return

    board[(x, y)] = tileType

    if x > 0 and board[(x - 1, y)] == charToChange:
        change_tile(tileType, board, x-1, y, charToChange)
    if y > 0 and board[(x, y-1)] == charToChange:
        change_tile(tileType, board, x, y-1, charToChange)
    if x < BOARD_WIDTH - 1 and board[(x + 1, y)] == charToChange:
        change_tile(tileType, board, x+1, y, charToChange)
    if y < BOARD_HEIGHT - 1 and board[(x, y + 1)] == charToChange:
        change_tile(tileType, board, x, y+1, charToChange)


def check_board_complete(board):
    tile = board[(0, 0)]

    for x in range(BOARD_WIDTH):
        for y in range(BOARD_HEIGHT):
            if board[(x, y)] != tile:
                return False
    return True


if __name__ == "__main__":
    main()
