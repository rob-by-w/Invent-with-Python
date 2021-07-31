import bext
import random
import time
import sys

WIDTH, HEIGHT = bext.size()
WIDTH -= 1

GROW_CHANCE = 0.01
LIGHTNING_CHANCE = 0.01

EMPTY = ' '
TREE = 'A'
FIRE = 'W'
COLOR = {EMPTY: 'white', TREE: 'green', FIRE: 'red'}

LEFT_EDGE = 0
RIGHT_EDGE = WIDTH
TOP_EDGE = 0
BOTTOM_EDGE = HEIGHT - 2

PAUSE_TIME = 1


def main():
    forest = create_forest()
    nextForest = {}

    while True:
        bext.clear()
        draw_forest(forest)

        for x in range(WIDTH):
            for y in range(HEIGHT):
                if forest[(x, y)] == EMPTY and random.random() <= GROW_CHANCE:
                    nextForest[(x, y)] = TREE
                elif forest[(x, y)] == TREE and random.random() <= LIGHTNING_CHANCE:
                    nextForest[(x, y)] = FIRE
                elif forest[(x, y)] == FIRE:
                    for ix in range(-1, 2):
                        for iy in range(-1, 2):
                            if forest.get((x+ix, y+iy)) == TREE:
                                nextForest[(x+ix, y+iy)] = FIRE
                    nextForest[(x, y)] = EMPTY
                else:
                    nextForest[(x, y)] = forest[(x, y)]

        forest = nextForest
        time.sleep(PAUSE_TIME)


def create_forest():
    cell = {}
    for x in range(WIDTH):
        for y in range(HEIGHT):
            cell[(x, y)] = TREE if random.random() <= GROW_CHANCE else EMPTY

    return cell


def draw_forest(cell):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            bext.fg(COLOR[cell[(x, y)]])
            print(cell[(x, y)], end='')
        print()
    bext.fg('reset')
    print(f'Grow chance: {GROW_CHANCE*100}%   ', end='')
    print(f'Lightning chance: {LIGHTNING_CHANCE*100}%   ', end='')
    print('Press Ctrl-C to quit.')


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
