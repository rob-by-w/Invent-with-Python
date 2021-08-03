import random
import bext
import sys
import time

PAUSE_TIME = 0.2
WIDE_FALL_CHANCE = 50

WIDTH = 79
HEIGHT = 25

X = 0
Y = 1
SAND = chr(9617)
GLASS = chr(9608)

HOURGLASS = set()
for i in range(18, 37):
    HOURGLASS.add((i, 1))    # Add walls for the top cap
    HOURGLASS.add((i, 23))   # Add walls for the bottom cap
for i in range(1, 5):
    # Add walls for the top left straight wall
    HOURGLASS.add((18, i))
    # Add walls for the top right straight wall
    HOURGLASS.add((36, i))
    # Add walls for the bottom left straight wall
    HOURGLASS.add((18, i+19))
    # Add walls for the bottom right straight wall
    HOURGLASS.add((36, i+19))
for i in range(8):
    # Add walls for the top left slanted wall
    HOURGLASS.add((19+i, 5+i))
    # Add walls for the top right slanted wall
    HOURGLASS.add((35-i, 5+i))
    # Add walls for the bottom left slanted wall
    HOURGLASS.add((25-i, 13+i))
    # Add walls for the bottom right slanted wall
    HOURGLASS.add((29+i, 13+i))

INITIAL_SAND = set()
for y in range(8):
    for x in range(19 + y, 36 - y):
        INITIAL_SAND.add((x, y + 4))


def main():
    bext.fg('black')
    bext.clear()

    bext.goto(0, 0)
    print('Ctrl-c to quit.', end='')

    for glass in HOURGLASS:
        bext.goto(glass[X], glass[Y])
        print(GLASS, end='')

    bext.fg('yellow')

    while True:
        allSand = list(INITIAL_SAND)
        for sand in allSand:
            bext.goto(sand[X], sand[Y])
            print(SAND, end='')

        hourglass_simulation(allSand)


def hourglass_simulation(sandList):
    while True:
        random.shuffle(sandList)

        sandMovedOnThisStep = False
        for i, sand in enumerate(sandList):
            if sand[Y] == HEIGHT - 1:
                continue

            noSandBelow = (sand[X], sand[Y] + 1) not in sandList
            noGlassBelow = (sand[X], sand[Y] + 1) not in HOURGLASS
            canFallDown = noSandBelow and noGlassBelow

            if canFallDown:
                bext.goto(sand[X], sand[Y])
                print(' ', end='')
                bext.goto(sand[X], sand[Y] + 1)
                print(SAND)

                sandList[i] = (sand[X], sand[Y]+1)
                sandMovedOnThisStep = True
            else:
                belowLeft = (sand[X] - 1, sand[Y] + 1)
                noSandBelowLeft = belowLeft not in sandList
                noGlassBelowLeft = belowLeft not in HOURGLASS
                left = (sand[X] - 1, sand[Y])
                noGlassLeft = left not in HOURGLASS
                notOnLeftEdge = sand[X] > 0
                canFallLeft = noSandBelowLeft and noGlassBelowLeft and noGlassLeft and notOnLeftEdge

                belowRight = (sand[X] + 1, sand[Y] + 1)
                noSandBelowRight = belowRight not in sandList
                noGlassBelowRight = belowRight not in HOURGLASS
                right = (sand[X] + 1, sand[Y])
                noGlassRight = right not in HOURGLASS
                notOnRightEdge = sand[X] > 0
                canFallRight = noSandBelowRight and noGlassBelowRight and noGlassRight and notOnRightEdge

                fallingDirection = None
                if canFallLeft and not canFallRight:
                    fallingDirection = -1
                elif not canFallLeft and canFallRight:
                    fallingDirection = 1
                elif canFallLeft and canFallRight:
                    fallingDirection = random.choice((-1, 1))

                if random.random() * 100 < WIDE_FALL_CHANCE:
                    belowTwoLeft = (sand[X] - 2, sand[Y] + 1)
                    noSandBelowTwoLeft = belowTwoLeft not in sandList
                    noGlassBelowTwoLeft = belowTwoLeft not in HOURGLASS
                    notOnSecondToLeftEdge = sand[X] > 1
                    canFallTwoLeft = canFallLeft and noSandBelowTwoLeft and noGlassBelowTwoLeft and notOnSecondToLeftEdge

                    belowTwoRight = (sand[X] + 2, sand[Y] + 1)
                    noSandBelowTwoRight = belowTwoRight not in sandList
                    noGlassBelowTwoRight = belowTwoRight not in HOURGLASS
                    notOnSecondToRightEdge = sand[X] > 1
                    canFallTwoRight = canFallRight and noSandBelowTwoRight and noGlassBelowTwoRight and notOnSecondToRightEdge

                    if canFallTwoLeft and not canFallTwoRight:
                        fallingDirection = -2
                    elif not canFallTwoLeft and canFallTwoRight:
                        fallingDirection = 2
                    elif canFallTwoLeft and canFallTwoRight:
                        fallingDirection = random.choice((-2, 2))

                if fallingDirection == None:
                    continue

                bext.goto(sand[X], sand[Y])
                print(' ', end='')
                bext.goto(sand[X] + fallingDirection, sand[Y] + 1)
                print(SAND, end='')

                sandList[i] = (sand[X] + fallingDirection, sand[Y] + 1)
                sandMovedOnThisStep = True

        sys.stdout.flush()
        time.sleep(PAUSE_TIME)

        if not sandMovedOnThisStep:
            time.sleep(2)
            for sand in sandList:
                bext.goto(sand[X], sand[Y])
                print(' ', end='')
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
