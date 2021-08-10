import os
import sys

WALL = '#'
EMPTY = ' '
START = 'S'
EXIT = 'E'

PLAYER = '@'
BLOCK = chr(9617)


def display_maze(maze):
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x, y) == (playerX, playerY):
                print(PLAYER, end='')
            elif (x, y) == (exitX, exitY):
                print('X', end='')
            elif maze[(x, y)] == WALL:
                print(BLOCK, end='')
            else:
                print(maze[(x, y)], end='')
        print()


if __name__ == "__main__":
    print('Maze Runner 2D')

    while True:
        print('Enter the filename of the maze (or LIST or QUIT):')
        filename = input('> ')

        if filename.upper() == 'LIST':
            print('Maze files found in' + os.getcwd() + '/mazes')
            for file in os.listdir('./mazes'):
                if file.startswith('maze') and file.endswith('.txt'):
                    print(f'    {file}')
            continue

        if filename.upper() == 'QUIT':
            sys.exit()

        if os.path.exists('./mazes/' + filename):
            break
        print(f'There is no file named {filename}')

    mazeFile = open('./mazes/' + filename)
    maze = {}
    lines = mazeFile.readlines()
    playerX = None
    playerY = None
    exitX = None
    exitY = None
    y = 0

    for line in lines:
        WIDTH = len(line.rstrip())
        for x, char in enumerate(line.rstrip()):
            assert char in (
                WALL, EMPTY, START, EXIT), f'Invalid character at column {x+1}, line {y+1}'
            if char in (WALL, EMPTY):
                maze[(x, y)] = char
            elif char == START:
                playerX, playerY = x, y
                maze[(x, y)] = EMPTY
            elif char == EXIT:
                exitX, exitY = x, y
                maze[(x, y)] = EMPTY
        y += 1
    HEIGHT = y

    assert playerX != None and playerY != None, 'No start in maze file.'
    assert exitX != None and exitY != None, 'No exit in maze file.'

    while True:
        display_maze(maze)

        while True:
            print('                          W')
            print('Enter direction or QUIT: ASD')
            move = input('> ').upper()

            if move == 'QUIT':
                print('Thanks for playing!')
                sys.exit()

            if move not in ['A', 'S', 'W', 'D']:
                print('Invalid direction. enter one of W, A, S, or D.')

            if move == 'W' and maze[(playerX, playerY - 1)] == EMPTY:
                break
            elif move == 'S' and maze[(playerX, playerY + 1)] == EMPTY:
                break
            elif move == 'A' and maze[(playerX - 1, playerY)] == EMPTY:
                break
            elif move == 'D' and maze[(playerX + 1, playerY)] == EMPTY:
                break

            print('You cannot move in that direction.')

        if move == 'W':
            while True:
                playerY -= 1
                if (playerX, playerY) == (exitX, exitY):
                    break
                if maze[(playerX, playerY - 1)] == WALL:
                    break
                if maze[(playerX - 1, playerY)] == EMPTY or maze[(playerX + 1, playerY)] == EMPTY:
                    break
        elif move == 'S':
            while True:
                playerY += 1
                if (playerX, playerY) == (exitX, exitY):
                    break
                if maze[(playerX, playerY + 1)] == WALL:
                    break
                if maze[(playerX - 1, playerY)] == EMPTY or maze[(playerX + 1, playerY)] == EMPTY:
                    break
        elif move == 'A':
            while True:
                playerX -= 1
                if (playerX, playerY) == (exitX, exitY):
                    break
                if maze[(playerX - 1, playerY)] == WALL:
                    break
                if maze[(playerX, playerY - 1)] == EMPTY or maze[(playerX, playerY + 1)] == EMPTY:
                    break
        elif move == 'D':
            while True:
                playerX += 1
                if (playerX, playerY) == (exitX, exitY):
                    break
                if maze[(playerX + 1, playerY)] == WALL:
                    break
                if maze[(playerX, playerY - 1)] == EMPTY or maze[(playerX, playerY + 1)] == EMPTY:
                    break

        if (playerX, playerY) == (exitX, exitY):
            display_maze(maze)
            print('You have reached the exit! Good job!')
            print('Thanks for playing!')
            sys.exit()
