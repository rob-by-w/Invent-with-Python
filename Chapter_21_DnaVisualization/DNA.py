import random
import time
import sys

WIDTH_PATTERN = [0, 1, 3, 5, 6]
MOLECULES = [['G', 'C'], ['A', 'T']]
BORDER = '#'
OFFSET = (9, 8, 7, 6, 5, 4, 4, 5, 5, 6, 5, 5, 4, 4, 5, 6, 7, 8)
PAUSE_TIME = 0.2

print('DNA Animation')
print('Press Ctrl-C to quit...')
time.sleep(2)
idxOffset = -1

try:
    while True:
        for width in WIDTH_PATTERN + WIDTH_PATTERN[:0:-1]:
            idxOffset = (idxOffset + 1) % len(OFFSET)

            if width == 0:
                print(' ' * OFFSET[idxOffset] + BORDER * 2)
            else:
                moleculesPair = random.choice(MOLECULES)
                if random.randint(0, 1) == 1:
                    moleculesPair[0], moleculesPair[1] = moleculesPair[1], moleculesPair[0]

                print(' ' * (OFFSET[idxOffset]) + BORDER +
                      moleculesPair[0] + '-' * width + moleculesPair[1] + BORDER)

            time.sleep(PAUSE_TIME)
except KeyboardInterrupt:
    sys.exit()
