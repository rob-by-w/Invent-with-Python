import sys
import math
import time
import os

PAUSE_TIME = 0.1
WIDTH, HEIGHT = 80, 24
SCALEX = (WIDTH - 4) // 8
SCALEY = (HEIGHT - 4) // 8
SCALEY *= 2
TRANSLATEX = (WIDTH - 4) // 2
TRANSLATEY = (HEIGHT - 4) // 2

LINE_CHAR = chr(9608)

X_ROTATE_SPEED = 0.03
Y_ROTATE_SPEED = 0.08
Z_ROTATE_SPEED = 0.13

X = 0
Y = 1
Z = 2


def rotate_point(x, y, z, ax, ay, az):
    """Returns an (x, y, z) tuple of the x, y, z arguments rotated.
    The rotation happens around the 0, 0, 0 origin by angles
    ax, ay, az (in radians).
        Directions of each axis:
         -y
         |
         +-- +x
        /
        +z
    """

    rotatedX = x
    rotatedY = (y * math.cos(ax)) - (z * math.sin(ax))
    rotatedZ = (y * math.sin(ax)) + (z * math.cos(ax))
    x, y, z = rotatedX, rotatedY, rotatedZ

    rotatedX = (z * math.sin(ay)) + (x * math.cos(ay))
    rotatedY = y
    rotatedZ = (z * math.cos(ay)) - (x * math.sin(ay))
    x, y, z = rotatedX, rotatedY, rotatedZ

    rotatedX = (x * math.cos(az)) - (y * math.sin(az))
    rotatedY = (x * math.sin(az)) + (y * math.cos(az))
    rotatedZ = z

    return (rotatedX, rotatedY, rotatedZ)


def adjust_point(point):
    """Adjusts the 3D XYZ point to a 2D XY point fit for displaying on
        the screen. This resizes this 2D point by a scale of SCALEX and
        SCALEY, then moves the point by TRANSLATEX and TRANSLATEY."""
    return (int(point[X] * SCALEX + TRANSLATEX), int(point[Y] * SCALEY + TRANSLATEY))


def line(x1, y1, x2, y2):
    points = []
    if (x1 == x2 and y1 == y2 + 1) or (y1 == y2 and x1 == x2 + 1):
        return [(x1, y1), (x2, y2)]

    isSteep = abs(y2 - y1) > abs(x2 - x1)
    if isSteep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    isReversed = x1 > x2

    if isReversed:
        x1, x2 = x2, x1
        y1, y2 = y2, y1

        deltaX = x2 - x1
        deltaY = abs(y2 - y1)
        extraY = int(deltaX / 2)
        currentY = y2
        yDirection = 1 if y1 < y2 else -1
        for currentX in range(x2, x1 - 1, -1):
            points.append((currentY, currentX)
                          if isSteep else (currentX, currentY))
            extraY -= deltaY
            if extraY <= 0:
                currentY -= yDirection
                extraY += deltaX
    else:
        deltaX = x2 - x1
        deltaY = abs(y2 - y1)
        extraY = int(deltaX / 2)
        currentY = y1
        yDirection = 1 if y1 < y2 else -1
        for currentX in range(x1, x2 + 1):
            points.append((currentY, currentX)
                          if isSteep else (currentX, currentY))
            extraY -= deltaY
            if extraY < 0:
                currentY += yDirection
                extraY += deltaX

    return points


if __name__ == "__main__":
    """CUBE_CORNERS stores the XYZ coordinates of the corners of a cube.
    The indexes for each corner in CUBE_CORNERS are marked in this diagram:
          0---1
         /|  /|
        2---3 |
        | 4-|-5
        |/  |/
        6---7"""
    CUBE_CORNERS = [[-1, -1, -1],  # Point 0
                    [1, -1, -1],  # Point 1
                    [-1, -1,  1],  # Point 2
                    [1, -1,  1],  # Point 3
                    [-1,  1, -1],  # Point 4
                    [1,  1, -1],  # Point 5
                    [-1,  1,  1],  # Point 6
                    [1,  1,  1]]  # Point 7
    # rotatedCorners stores the XYZ coordinates from CUBE_CORNERS after
    # they've been rotated by rx, ry, and rz amounts:
    rotatedCorners = [None for _ in range(8)]
    xRotation = 0
    yRotation = 0
    zRotation = 0

    try:
        while True:
            xRotation += X_ROTATE_SPEED
            yRotation += Y_ROTATE_SPEED
            zRotation += Z_ROTATE_SPEED
            for i in range(len(CUBE_CORNERS)):
                x = CUBE_CORNERS[i][X]
                y = CUBE_CORNERS[i][Y]
                z = CUBE_CORNERS[i][Z]
                rotatedCorners[i] = rotate_point(
                    x, y, z, xRotation, yRotation, zRotation)

            cubePoints = []
            for fromCornerIndex, toCornerIndex in ((0, 1), (1, 3), (3, 2), (2, 0), (0, 4), (1, 5), (2, 6), (3, 7), (4, 5), (5, 7), (7, 6), (6, 4)):
                fromX, fromY = adjust_point(rotatedCorners[fromCornerIndex])
                toX, toY = adjust_point(rotatedCorners[toCornerIndex])
                pointsOnLine = line(fromX, fromY, toX, toY)
                cubePoints.extend(pointsOnLine)

            cubePoints = tuple(frozenset(cubePoints))
            for y in range(HEIGHT):
                for x in range(WIDTH):
                    print(LINE_CHAR if (x, y) in cubePoints else ' ',
                          end='', flush=False)
                print(flush=False)
            print('Press Ctrl-C to quit.', end='', flush=True)

            time.sleep(PAUSE_TIME)
            os.system('cls' if sys.platform == 'win32' else 'clear')

    except KeyboardInterrupt:
        sys.exit()
