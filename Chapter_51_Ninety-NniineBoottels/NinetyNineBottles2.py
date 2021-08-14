import random
import time
import sys

PAUSE_TIME = 1

print('niNety-nniinE BoOttels')
print()
print('Press Ctrl-C to quit.')
time.sleep(PAUSE_TIME)

lines = ['bottles of milk on the wall,', 'bottles of milk,',
         'Take one down, pass it around,', 'bottles of milk on the wall!']
try:
    for bottle in range(99, 0, -1):
        for idx, line in enumerate(lines):
            if idx in [0, 1]:
                print(f'{bottle}', end=' ')
            if idx == 3 and bottle - 1 > 0:
                print(f'{bottle-1}', end=' ')

            if bottle == 1 and idx == 3:
                print('No more bottles of milk on the wall!')
            else:
                print(line)
            time.sleep(PAUSE_TIME)
        print()

        lineIdxToEdit = random.randint(0, len(lines)-1)
        lineToEdit = list(lines[lineIdxToEdit])
        mutationsType = random.randint(1, 4)
        if mutationsType == 1:
            charIdx = random.randint(0, len(lineToEdit)-1)
            lineToEdit[charIdx] = ' '
        elif mutationsType == 2:
            charIdx = random.randint(0, len(lineToEdit)-1)
            lineToEdit[charIdx] = lineToEdit[charIdx].lower(
            ) if lineToEdit[charIdx].isupper() else lineToEdit[charIdx].upper()
        elif mutationsType == 3:
            charIdx = random.randint(0, len(lineToEdit)-2)
            lineToEdit[charIdx], lineToEdit[charIdx +
                                            1] = lineToEdit[charIdx+1], lineToEdit[charIdx]
        elif mutationsType == 4:
            charIdx = random.randint(0, len(lineToEdit)-2)
            lineToEdit.insert(charIdx, lineToEdit[charIdx])

        lines[lineIdxToEdit] = ''.join(lineToEdit)

except KeyboardInterrupt:
    sys.exit()
