import random
import sys

WIDTH = 40
HEIGHT = 20

PLAYER = chr(923)
ROBOT = 'R'
EMPTY = ' '
CRASH = chr(9617)
WALL = chr(9608)

NUM_OF_ROBOTS = 10
NUM_OF_TELEPORTS = 2
NUM_OF_DEAD_ROBOTS = 2
NUM_OF_WALLS = 100


def main():
    print(f'''Hungry Robots
You are trapped in a maze with hungry robots! You don't know why robots need to eat,
but you don't want to find out. The robots are badly programmed and will move directly
toward you, even if blocked by walls. You must trick the robots into crashing into each other
(or dead robots) without being caught. You have a personal teleporter device, but it only
has enough battery for {NUM_OF_TELEPORTS} trips. Keep in mind, you and robots can slip
through the corners of two diagonal walls!
''')

    input('Press Enter to begin...')
    board = initialize_board()
    robotPositions = initialize_robots(board)
    playerPosition = initialize_player(board)

    while True:
        print_board(board)
        check_end(playerPosition, board, robotPositions)
        print(f'(T)eleports remaining: {board["teleports"]}')
        playerPosition = player_move(playerPosition, board, robotPositions)
        board[playerPosition] = PLAYER
        robotPositions = robot_move(playerPosition, board, robotPositions)


def initialize_board():
    board = {'teleports': NUM_OF_TELEPORTS}
    for col in range(WIDTH):
        for row in range(HEIGHT):
            if row in [0, HEIGHT-1] or col in [0, WIDTH - 1]:
                board[(col, row)] = WALL
            else:
                board[(col, row)] = EMPTY

    for _ in range(NUM_OF_WALLS):
        while True:
            col, row = random.randint(1, WIDTH-2), random.randint(1, HEIGHT-2)
            if board[(col, row)] == EMPTY:
                board[(col, row)] = WALL
                break

    for _ in range(NUM_OF_DEAD_ROBOTS):
        while True:
            col, row = random.randint(1, WIDTH-2), random.randint(1, HEIGHT-2)
            if board[(col, row)] == EMPTY:
                board[(col, row)] = CRASH
                break

    return board


def initialize_robots(board):
    robots = []
    for _ in range(NUM_OF_ROBOTS):
        while True:
            col, row = random.randint(1, WIDTH-2), random.randint(1, HEIGHT-2)
            if board[(col, row)] == EMPTY:
                board[(col, row)] = ROBOT
                robots.append((col, row))
                break

    return robots


def initialize_player(board):
    while True:
        col, row = random.randint(1, WIDTH-2), random.randint(1, HEIGHT-2)
        if board[(col, row)] == EMPTY:
            board[(col, row)] = PLAYER
            return (col, row)


def print_board(cell):
    for row in range(HEIGHT):
        for col in range(WIDTH):
            print(cell[(col, row)], end='')
        print()


def check_empty(positions, board, robots):
    return board[positions] == EMPTY and positions not in robots


def player_move(player, board, robots):
    board[player] = EMPTY

    playerX, playerY = player
    q = 'Q' if check_empty((playerX - 1, playerY - 1),
                           board, robots) else ' '
    w = 'W' if check_empty((playerX, playerY - 1),
                           board, robots) else ' '
    e = 'E' if check_empty((playerX + 1, playerY - 1),
                           board, robots) else ' '
    a = 'A' if check_empty((playerX - 1, playerY),
                           board, robots) else ' '
    d = 'D' if check_empty((playerX + 1, playerY),
                           board, robots) else ' '
    z = 'Z' if check_empty((playerX - 1, playerY + 1),
                           board, robots) else ' '
    x = 'X' if check_empty((playerX, playerY + 1),
                           board, robots) else ' '
    c = 'C' if check_empty((playerX + 1, playerY + 1),
                           board, robots) else ' '
    t = 'T' if board['teleports'] > 0 else ' '
    moveList = q + w + e + a + d + z + x + c + 'S' + t

    print(' ' * 20 + f'({q})  ({w})  ({e})')
    print(f'Enter Move or QUIT: ({a})  (S)  ({d})')
    print(' ' * 20 + f'({z})  ({x})  ({c})')

    while True:
        playerMove = input('> ').upper()
        if playerMove in moveList:
            break

        if playerMove == 'QUIT':
            sys.exit()

        print('Invalid input.')

    if playerMove == 'T':
        while True:
            playerX, playerY = random.randint(
                1, WIDTH-2), random.randint(1, HEIGHT-2)
            if check_empty((playerX, playerY), board, robots):
                board['teleports'] -= 1
                return (playerX, playerY)

    return {
        'Q': (playerX - 1, playerY - 1),
        'W': (playerX, playerY - 1),
        'E': (playerX + 1, playerY - 1),
        'A': (playerX - 1, playerY),
        'S': (playerX, playerY),
        'D': (playerX + 1, playerY),
        'Z': (playerX - 1, playerY + 1),
        'X': (playerX, playerY + 1),
        'C': (playerX + 1, playerY + 1)
    }[playerMove]


def robot_move(player, board, robots):
    for robot in robots:
        board[robot] = EMPTY

    robotNextPositions = []
    for robotX, robotY in robots:
        # Horizonal move
        robotNextX = robotX
        if robotX < player[0]:
            robotNextX = robotX + 1
        elif robotX > player[0]:
            robotNextX = robotX - 1

        # Vertical move
        robotNextY = robotY
        if robotY < player[1]:
            robotNextY = robotY + 1
        elif robotY > player[1]:
            robotNextY = robotY - 1

        if board[(robotNextX, robotNextY)] != WALL:
            robotX, robotY = robotNextX, robotNextY
        elif board[(robotX, robotNextY)] != WALL:
            robotY = robotNextY
        elif board[(robotNextX, robotY)] != WALL:
            robotX = robotNextX

        if board[(robotX, robotY)] == CRASH:
            continue

        if (robotX, robotY) not in robotNextPositions:
            robotNextPositions.append((robotX, robotY))
        else:
            robotNextPositions.remove((robotX, robotY))
            board[(robotX, robotY)] = CRASH

    for robot in robotNextPositions:
        board[robot] = ROBOT

    return robotNextPositions


def check_end(player, board, robots):
    if player in robots or board[player] == CRASH:
        print('Game over!')
        sys.exit()

    if robots == []:
        print('You win!')
        sys.exit()


if __name__ == "__main__":
    main()
