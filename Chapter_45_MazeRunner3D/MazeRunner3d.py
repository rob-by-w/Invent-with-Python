import sys
import os

WALL = '#'
EMPTY = ' '
START = 'S'
EXIT = 'E'
BLOCK = chr(9617)
NORTH = 'NORTH'
SOUTH = 'SOUTH'
EAST = 'EAST'
WEST = 'WEST'


def wall_str_to_dict(wallStr):
    wallDict = {}
    height = 0
    width = 0
    for y, line in enumerate(wallStr.splitlines()):
        height = y if y > height else height
        for x, char in enumerate(line):
            width = x if x > width else width
            wallDict[(x, y)] = char
    wallDict['height'] = height + 1
    wallDict['width'] = width + 1
    return wallDict


EXIT_DICT = {(0, 0): 'E', (1, 0): 'X', (2, 0): 'I',
             (3, 0): 'T', 'height': 1, 'width': 4}
ALL_OPEN = wall_str_to_dict(r'''                      
.................
____.........____
...|\......./|...
...||.......||...
...||__...__||...
...||.|\./|.||...
...||.|.X.|.||...
...||.|/.\|.||...
...||_/...\_||...
...||.......||...
___|/.......\|___
.................
.................'''.strip())

CLOSED = {}
CLOSED['A'] = wall_str_to_dict(r'''
_____
.....
.....
.....
_____'''.strip())
CLOSED['B'] = wall_str_to_dict(r'''
.\.
..\
...
...
...
../
./.'''.strip())
CLOSED['C'] = wall_str_to_dict(r'''
___________
...........
...........
...........
...........
...........
...........
...........
...........
___________'''.strip())
CLOSED['D'] = wall_str_to_dict(r'''
./.
/..
...
...
...
\..
.\.'''.strip())
CLOSED['E'] = wall_str_to_dict(r'''
..\..
...\_
....|
....|
....|
....|
....|
....|
....|
....|
....|
.../.
../..'''.strip())
CLOSED['F'] = wall_str_to_dict(r'''
../..
_/...
|....
|....
|....
|....
|....
|....
|....
|....
|....
.\...
..\..'''.strip())


def display_wall_dict(wallDict):
    print(BLOCK * (wallDict['width'] + 2))
    for y in range(wallDict['height']):
        print(BLOCK, end='')
        for x in range(wallDict['width']):
            print(' ' if wallDict[(x, y)] == '.' else wallDict[(x, y)], end='')
        print(BLOCK)
    print(BLOCK * (wallDict['width'] + 2))


def paste_wall_dict(srcWallDict, targetWallDict, left, top):
    dstWallDict = targetWallDict.copy()
    for x in range(srcWallDict['width']):
        for y in range(srcWallDict['height']):
            dstWallDict[(x + left, y + top)] = srcWallDict[(x, y)]
    return dstWallDict


def make_wall_dict(maze, playerX, playerY, playerDirection, exitX, exitY):
    if playerDirection == NORTH:
        offsets = (('A', 0, -2), ('B', -1, -1), ('C', 0, -1),
                   ('D', 1, -1), ('E', -1, 0), ('F', 1, 0))
    if playerDirection == SOUTH:
        offsets = (('A', 0, 2), ('B', 1, 1), ('C', 0, 1),
                   ('D', -1, 1), ('E', 1, 0), ('F', -1, 0))
    if playerDirection == EAST:
        offsets = (('A', 2, 0), ('B', 1, -1), ('C', 1, 0),
                   ('D', 1, 1), ('E', 0, -1), ('F', 0, 1))
    if playerDirection == WEST:
        offsets = (('A', -2, 0), ('B', -1, 1), ('C', -1, 0),
                   ('D', -1, -1), ('E', 0, 1), ('F', 0, -1))

    section = {}
    for sec, xOff, yOff in offsets:
        section[sec] = maze.get((playerX + xOff, playerY + yOff), WALL)
        if (playerX + xOff, playerY + yOff) == (exitX, exitY):
            section[sec] = EXIT

    wallDict = ALL_OPEN.copy()
    PASTE_CLOSED_TO = {'A': (6, 4), 'B': (4, 3), 'C': (
        3, 1), 'D': (10, 3), 'E': (0, 0), 'F': (12, 0)}
    for sec in 'ABDCEF':
        if section[sec] == WALL:
            wallDict = paste_wall_dict(
                CLOSED[sec], wallDict, PASTE_CLOSED_TO[sec][0], PASTE_CLOSED_TO[sec][1])

    if section['C'] == EXIT:
        wallDict = paste_wall_dict(EXIT_DICT, wallDict, 7, 9)
    if section['E'] == EXIT:
        wallDict = paste_wall_dict(EXIT_DICT, wallDict, 0, 11)
    if section['F'] == EXIT:
        wallDict = paste_wall_dict(EXIT_DICT, wallDict, 13, 11)

    return wallDict


if __name__ == "__main__":
    print('Maze Runner 3D')

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
    playerDirection = NORTH

    while True:
        display_wall_dict(make_wall_dict(
            maze, playerX, playerY, playerDirection, exitX, exitY))

        while True:
            print(
                f'Location ({playerX}, {playerY})   Direction: {playerDirection}')
            print('                           (W)')
            print('Enter direction or QUIT: (A) (D)')
            move = input('> ').upper()

            if move == 'QUIT':
                print('Thanks for playing!')
                sys.exit()

            if move not in ['F', 'L', 'R', 'W', 'A', 'D'] and not move.startswith('T'):
                print('Please enter one of W, A, or D (or F, L, or R).')

            if move == 'F' or move == 'W':
                if playerDirection == NORTH and maze[(playerX, playerY - 1)] == EMPTY:
                    playerY -= 1
                    break
                if playerDirection == SOUTH and maze[(playerX, playerY + 1)] == EMPTY:
                    playerY += 1
                    break
                if playerDirection == EAST and maze[(playerX + 1, playerY)] == EMPTY:
                    playerX += 1
                    break
                if playerDirection == WEST and maze[(playerX - 1, playerY)] == EMPTY:
                    playerX -= 1
                    break
            elif move == 'L' or move == 'A':
                playerDirection = {NORTH: WEST, WEST: SOUTH,
                                   SOUTH: EAST, EAST: NORTH}[playerDirection]
                break
            elif move == 'R' or move == 'D':
                playerDirection = {NORTH: EAST, WEST: NORTH,
                                   SOUTH: WEST, EAST: SOUTH}[playerDirection]
                break
            elif move.startswith('T'):
                playerX, playerY = map(int, move.split()[1].split(','))
                break
            else:
                print('You cannot move in that direction.')

        if (playerX, playerY) == (exitX, exitY):
            print('You have reached the exit! Good job!')
            print('Thanks for playing!')
            sys.exit()
