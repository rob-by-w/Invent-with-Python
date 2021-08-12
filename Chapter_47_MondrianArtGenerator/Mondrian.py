import bext
import random
import sys

WIDTH, HEIGHT = bext.size()
WIDTH -= 1
HEIGHT -= 3

MIN_X_INCREASE = 6
MAX_X_INCREASE = 16
MIN_Y_INCREASE = 3
MAX_Y_INCREASE = 6
WHITE = 'white'
BLACK = 'black'
RED = 'red'
YELLOW = 'yellow'
BLUE = 'blue'
GREEN = 'green'

while True:
    canvas = {}
    for x in range(WIDTH):
        for y in range(HEIGHT):
            canvas[(x, y)] = WHITE

    numOfSegmentsToDelete = 0
    x = random.randint(MIN_X_INCREASE, MAX_X_INCREASE)
    while x < WIDTH - MIN_X_INCREASE:
        numOfSegmentsToDelete += 1
        for y in range(HEIGHT):
            canvas[(x, y)] = BLACK
        x += random.randint(MIN_X_INCREASE, MAX_X_INCREASE)

    y = random.randint(MIN_Y_INCREASE, MAX_Y_INCREASE)
    while y < HEIGHT - MIN_Y_INCREASE:
        numOfSegmentsToDelete += 1
        for x in range(WIDTH):
            canvas[(x, y)] = BLACK
        y += random.randint(MIN_Y_INCREASE, MAX_Y_INCREASE)

    numOfRectanglesToPaint = numOfSegmentsToDelete - 3
    numOfSegmentsToDelete = int(numOfSegmentsToDelete * 1.5)

    for i in range(numOfSegmentsToDelete):
        while True:
            startX = random.randint(1, WIDTH - 2)
            startY = random.randint(1, HEIGHT - 2)
            if canvas[(startX, startY)] == WHITE:
                continue

            if canvas[(startX - 1, startY)] == WHITE and canvas[(startX + 1, startY)] == WHITE:
                orientation = 'vertical'
            elif canvas[(startX, startY - 1)] == WHITE and canvas[(startX, startY + 1)] == WHITE:
                orientation = 'horizontal'
            else:
                continue

            pointsToDelete = [(startX, startY)]
            canDeleteSegment = True
            if orientation == 'vertical':
                for changeY in (-1, 1):
                    y = startY
                    while 0 < y < HEIGHT - 1:
                        y += changeY
                        if canvas[(startX - 1, y)] == BLACK and canvas[(startX + 1, y)] == BLACK:
                            break
                        elif (canvas[(startX - 1, y)] == WHITE and canvas[(startX + 1, y)] == BLACK) or (canvas[(startX - 1, y)] == BLACK and canvas[(startX + 1, y)] == WHITE):
                            canDeleteSegment = False
                            break

                        pointsToDelete.append((startX, y))

            elif orientation == 'horizontal':
                for changeX in (-1, 1):
                    x = startX
                    while 0 < x < WIDTH - 1:
                        x += changeX
                        if canvas[(x, startY - 1)] == BLACK and canvas[(x, startY + 1)] == BLACK:
                            break
                        elif (canvas[(x, startY - 1)] == WHITE and canvas[(x, startY + 1)] == BLACK) or (canvas[(x, startY - 1)] == BLACK and canvas[(x, startY + 1)] == WHITE):
                            canDeleteSegment = False
                            break

                        pointsToDelete.append((x, startY))

            if not canDeleteSegment:
                continue
            break

        for x, y in pointsToDelete:
            canvas[(x, y)] = WHITE

    for x in range(WIDTH):
        canvas[(x, 0)] = BLACK
        canvas[(x, HEIGHT - 1)] = BLACK
    for y in range(HEIGHT):
        canvas[(0, y)] = BLACK
        canvas[(WIDTH - 1, y)] = BLACK

    for i in range(numOfRectanglesToPaint):
        while True:
            startX = random.randint(1, WIDTH - 2)
            startY = random.randint(1, HEIGHT - 2)
            if canvas[(startX, startY)] != WHITE:
                continue
            else:
                break

        colorToPaint = random.choice([RED, YELLOW, BLUE, GREEN])
        pointsToPaint = set([(startX, startY)])
        while len(pointsToPaint) > 0:
            x, y = pointsToPaint.pop()
            canvas[(x, y)] = colorToPaint
            if canvas[(x - 1, y)] == WHITE:
                pointsToPaint.add((x - 1, y))
            if canvas[(x + 1, y)] == WHITE:
                pointsToPaint.add((x + 1, y))
            if canvas[(x, y - 1)] == WHITE:
                pointsToPaint.add((x, y - 1))
            if canvas[(x, y + 1)] == WHITE:
                pointsToPaint.add((x, y + 1))

    for y in range(HEIGHT):
        for x in range(WIDTH):
            bext.bg(canvas[(x, y)])
            print(' ', end='')
        print()

    try:
        bext.fg(WHITE)
        input('Press Enter for another work of art, or Ctrl-C to quit.')
    except KeyboardInterrupt:
        sys.exit()
