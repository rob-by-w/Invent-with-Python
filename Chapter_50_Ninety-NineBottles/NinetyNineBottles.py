import sys
import time

PAUSE = 1

print('Ninety-Nine Bottles')
print()
print('Press Ctrl-C to quit.')
try:
    for bottle in range(99, 1, -1):
        print(f'{bottle} bottles of milk on the wall,')
        time.sleep(PAUSE)
        print(f'{bottle} bottles of milk,')
        time.sleep(PAUSE)
        print('Take one down, pass it around,')
        time.sleep(PAUSE)
        print(f'{bottle-1} bottles' if bottle >
              2 else f'{bottle-1} bottle', end=' ')
        time.sleep(PAUSE)
        print('of milk on the wall!')
        time.sleep(PAUSE)
        print()

    print('1 bottle of milk on the wall,')
    time.sleep(PAUSE)
    print('1 bottle of milk,')
    time.sleep(PAUSE)
    print('Take one down, pass it around,')
    time.sleep(PAUSE)
    print('No more bottles of milk on the wall!')

except KeyboardInterrupt:
    sys.exit()
