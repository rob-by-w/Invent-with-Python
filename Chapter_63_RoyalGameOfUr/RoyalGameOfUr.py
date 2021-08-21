import os
import random
import sys

PLAYER_X = 'X'
PLAYER_O = 'O'
EMPTY = ' '

HOME_X = 'x_home'
HOME_O = 'o_home'
GOAL_X = 'x_goal'
GOAL_O = 'o_goal'

ALL_SPACES = 'hgfetsijklmnopdcbarq'
TRACK_X = 'HefghijklmnopstG'
TRACK_O = 'HabcdijklmnopqrG'

FLOWER_SPACES = ('h', 't', 'd', 'r')

BOARD_TEMPLATE = """
                    {}           {}
                    Home              Goal
                      v                 ^
 +-----+-----+-----+--v--+           +--^--+-----+
 |*****|     |     |     |           |*****|     |
 |* {} *<  {}  <  {}  <  {}  |           |* {} *<  {}  |
 |****h|    g|    f|    e|           |****t|    s|
 +--v--+-----+-----+-----+-----+-----+-----+--^--+
 |     |     |     |*****|     |     |     |     |
 |  {}  >  {}  >  {}  >* {} *>  {}  >  {}  >  {}  >  {}  |
 |    i|    j|    k|****l|    m|    n|    o|    p|
 +--^--+-----+-----+-----+-----+-----+-----+--v--+
 |*****|     |     |     |           |*****|     |
 |* {} *<  {}  <  {}  <  {}  |           |* {} *<  {}  |
 |****d|    c|    b|    a|           |****r|    q|
 +-----+-----+-----+--^--+           +--v--+-----+
                      ^                 v
                    Home              Goal
                    {}           {}
"""


def main():
    print('''The Royal Game of Ur
          
This is a 5,000 year old game. Two players must move their tokens
from their home to their goal. On your turn you flip four coins and can
move one token a number of spaces equal to the heads you got.

Ur is a racing game; the first player to move all seven of their tokens
to their goal wins. To do this, tokens must travel from their home to
their goal:

            X Home      X Goal
              v           ^
+---+---+---+-v-+       +-^-+---+
|v<<<<<<<<<<<<< |       | ^<|<< |
|v  |   |   |   |       |   | ^ |
+v--+---+---+---+---+---+---+-^-+
|>>>>>>>>>>>>>>>>>>>>>>>>>>>>>^ |
|>>>>>>>>>>>>>>>>>>>>>>>>>>>>>v |
+^--+---+---+---+---+---+---+-v-+
|^  |   |   |   |       |   | v |
|^<<<<<<<<<<<<< |       | v<<<< |
+---+---+---+-^-+       +-v-+---+
              ^           v
            O Home      O Goal
            
If you land on an opponent's token in the middle track, it gets sent
back home. The **flower** spaces let you take another turn. Tokens in
the middle flower space are safe and cannot be landed on.''')
    input('Press Enter to begin...')

    board = initialize_board()
    turn = PLAYER_O

    while True:
        if turn == PLAYER_X:
            opponent = PLAYER_O
            home = HOME_X
            goal = GOAL_X
            track = TRACK_X
            opponentHome = HOME_O
        elif turn == PLAYER_O:
            opponent = PLAYER_X
            home = HOME_O
            goal = GOAL_O
            track = TRACK_O
            opponentHome = HOME_X

        display_board(board)
        input(f"It is {turn}'s turn. Press Enter to flip...")

        flipResult = ['H' if random.randint(
            0, 1) == 1 else 'T' for _ in range(4)]
        totalMove = flipResult.count('H')
        print('Flips: ' + '-'.join(flipResult))

        if totalMove == 0:
            input('You lose a turn. Press Enter to continue...')
            turn = opponent
            continue

        validMoves = get_moves(board, turn, totalMove)
        if validMoves == []:
            print('There are no possible moves, so you lose a turn.')
            input('Press Enter to continue...')
            turn = opponent
            continue

        while True:
            print(f'Select move {totalMove} spaces: ', end='')
            print(' '.join(validMoves) + ' quit')
            userMove = input('> ').lower()

            if userMove == 'quit':
                print('Thanks for playing!')
                sys.exit()
            if userMove in validMoves:
                break

            print('Invalid move.')

        if userMove == 'home':
            board[home] -= 1
            nextSpaceIdx = totalMove
        else:
            board[userMove] = EMPTY
            nextSpaceIdx = track.index(userMove) + totalMove

        if nextSpaceIdx == (len(track) - 1):
            board[goal] += 1
            if board[goal] == 7:
                display_board(board)
                print(f'{turn} has won the game!')
                print('Thanks for playing!')
                sys.exit()
        else:
            nextSpace = track[nextSpaceIdx]
            if board[nextSpace] == opponent:
                board[opponentHome] += 1

            board[nextSpace] = turn

        if nextSpace in FLOWER_SPACES:
            print(f'{turn} landed on a flower space and goes again.')
            input('Press Enter to continue...')
        else:
            turn = opponent


def initialize_board():
    board = {HOME_X: 7, GOAL_X: 0, HOME_O: 7, GOAL_O: 0}
    board.update({cell: EMPTY for cell in ALL_SPACES})
    return board


def display_board(board):
    os.system('cls' if os.name == 'nt' else 'clear')
    xHomeTokens = ('X' * board[HOME_X]).ljust(7, '.')
    xGoalTokens = ('X' * board[GOAL_X]).ljust(7, '.')
    oHomeTokens = ('O' * board[HOME_O]).ljust(7, '.')
    oGoalTokens = ('O' * board[GOAL_O]).ljust(7, '.')

    spaces = [xHomeTokens, xGoalTokens]
    for cell in ALL_SPACES:
        spaces.append(board[cell])
    spaces.extend([oHomeTokens, oGoalTokens])

    print(BOARD_TEMPLATE.format(*spaces))


def get_moves(board, player, totalMove):
    availableMoves = []
    if player == PLAYER_X:
        opponent = PLAYER_O
        home = HOME_X
        track = TRACK_X
    elif player == PLAYER_O:
        opponent = PLAYER_X
        home = HOME_O
        track = TRACK_O

    if board[home] > 0 and board[track[totalMove]] == EMPTY:
        availableMoves.append('home')

    for idx, space in enumerate(track):
        if space == 'H' or space == 'G' or board[space] != player:
            continue

        nextSpaceIdx = idx + totalMove
        if nextSpaceIdx >= len(track):
            continue

        nextSpaceKey = track[nextSpaceIdx]
        if nextSpaceKey == 'G':
            availableMoves.append(space)
            continue

        if board[nextSpaceKey] in (EMPTY, opponent):
            if nextSpaceKey == 'l' and board['l'] == opponent:
                continue
            availableMoves.append(space)

    return availableMoves


if __name__ == "__main__":
    main()
