import random
import os
import time
import sys

WIDTH = 80
HEIGHT = 9

ALIVE = 'O'
DEAD = ' '

nextCells = {}
for x in range(WIDTH):
    for y in range(HEIGHT):
        nextCells[(x, y)] = ALIVE if random.randint(0, 1) == 1 else DEAD

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    currentCells = nextCells.copy()

    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(currentCells[(x, y)], end='')
        print()

    if any([status == ALIVE for status in currentCells.values()]):
        print('Press Ctrl-C to quit.')
    else:
        print('All cells are dead. Simulation ends.')
        sys.exit()

    for x in range(WIDTH):
        for y in range(HEIGHT):
            countNeighbors = 0

            left = (x - 1) % WIDTH
            right = (x + 1) % WIDTH
            up = (y - 1) % HEIGHT
            down = (y - 1) % HEIGHT

            if currentCells[(left, y)] == ALIVE:
                countNeighbors += 1
            if currentCells[(left, up)] == ALIVE:
                countNeighbors += 1
            if currentCells[(x, up)] == ALIVE:
                countNeighbors += 1
            if currentCells[(right, up)] == ALIVE:
                countNeighbors += 1
            if currentCells[(right, y)] == ALIVE:
                countNeighbors += 1
            if currentCells[(right, down)] == ALIVE:
                countNeighbors += 1
            if currentCells[(x, down)] == ALIVE:
                countNeighbors += 1
            if currentCells[(left, down)] == ALIVE:
                countNeighbors += 1

            if currentCells[(x, y)] == ALIVE and countNeighbors in [2, 3]:
                nextCells[(x, y)] = ALIVE
            elif currentCells[(x, y)] == DEAD and countNeighbors == 3:
                nextCells[(x, y)] = ALIVE
            else:
                nextCells[(x, y)] = DEAD

    try:
        time.sleep(1)
    except KeyboardInterrupt:
        print('\nSimulation end.')
        sys.exit()
