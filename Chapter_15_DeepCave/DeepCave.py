import random
import time
import sys

ROCK = '#'
GAP = ' '
WIDTH = 80
PAUSE_TIME = 0.5

print('Deep cave')
print('Press Ctrl-C to stop.')
time.sleep(2)
leftWidth = 35
gapWidth = 10

while True:
    rightWidth = WIDTH - leftWidth - gapWidth
    print(ROCK*leftWidth + GAP*gapWidth + ROCK*rightWidth)

    try:
        time.sleep(PAUSE_TIME)
    except KeyboardInterrupt:
        sys.exit()

    diceRoll = random.randint(1, 6)
    if diceRoll == 1 and leftWidth > 1:
        leftWidth -= 1
    elif diceRoll == 2 and rightWidth > 1:
        leftWidth += 1
    elif diceRoll == 3 and gapWidth > 2:
        gapWidth -= 1
    elif diceRoll == 4 and rightWidth > 1:
        gapWidth += 1
    else:
        pass
