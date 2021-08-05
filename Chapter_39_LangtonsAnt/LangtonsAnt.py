import bext
import random
import sys
import time

WIDTH, HEIGHT = bext.size()
WIDTH -= 1
HEIGHT -= 2

PAUSE_TIME = 0.2
NUM_OF_ANTS = 10

ANT_COLOR = 'red'
WHITE_CELL = 'white'
BLACK_CELL = 'black'

NORTH = 'north'
SOUTH = 'south'
EAST = 'east'
WEST = 'west'

ANT_UP = '^'
ANT_DOWN = 'v'
ANT_LEFT = '<'
ANT_RIGHT = '>'


def main():
    board = {'width': WIDTH, 'height': HEIGHT}
    changedTiles = []
    antList = []
    for _ in range(NUM_OF_ANTS):
        antList.append({
            'x': random.randint(0, WIDTH),
            'y': random.randint(0, HEIGHT),
            'direction': random.choice([NORTH, SOUTH, EAST, WEST])
        })

    bext.fg(ANT_COLOR)
    bext.bg(WHITE_CELL)
    bext.clear()

    while True:
        display_board(board, antList, changedTiles)
        changedTiles = []

        nextBoard = board.copy()

        for ant in antList:
            if board.get((ant['x'], ant['y']), False):
                nextBoard[(ant['x'], ant['y'])] = False
                if ant['direction'] == NORTH:
                    ant['direction'] = EAST
                elif ant['direction'] == SOUTH:
                    ant['direction'] = WEST
                elif ant['direction'] == EAST:
                    ant['direction'] = SOUTH
                elif ant['direction'] == WEST:
                    ant['direction'] = NORTH
            else:
                nextBoard[(ant['x'], ant['y'])] = True
                if ant['direction'] == NORTH:
                    ant['direction'] = WEST
                elif ant['direction'] == SOUTH:
                    ant['direction'] = EAST
                elif ant['direction'] == EAST:
                    ant['direction'] = NORTH
                elif ant['direction'] == WEST:
                    ant['direction'] = SOUTH

            changedTiles.append((ant['x'], ant['y']))

            if ant['direction'] == NORTH:
                ant['y'] -= 1
            elif ant['direction'] == SOUTH:
                ant['y'] += 1
            elif ant['direction'] == EAST:
                ant['x'] += 1
            elif ant['direction'] == WEST:
                ant['x'] -= 1

            ant['x'] = ant['x'] % WIDTH
            ant['y'] = ant['y'] % HEIGHT

            changedTiles.append((ant['x'], ant['y']))

        board = nextBoard


def display_board(board, ants, changedTiles):
    for x, y in changedTiles:
        bext.goto(x, y)
        bext.bg(BLACK_CELL if board.get((x, y), False) else WHITE_CELL)

        antHere = False
        for ant in ants:
            if (x, y) == (ant['x'], ant['y']):
                antHere = True
                if ant['direction'] == NORTH:
                    print(ANT_UP, end='')
                elif ant['direction'] == SOUTH:
                    print(ANT_DOWN, end='')
                elif ant['direction'] == WEST:
                    print(ANT_LEFT, end='')
                elif ant['direction'] == EAST:
                    print(ANT_RIGHT, end='')
                break

        if not antHere:
            print(' ', end='')

    bext.goto(0, HEIGHT+1)
    bext.bg(WHITE_CELL)
    print('Press Ctrl-C to quit.', end='')

    sys.stdout.flush()
    time.sleep(PAUSE_TIME)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
