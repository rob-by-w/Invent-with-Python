import random
import shutil
import sys
import time

MIN_STREAM_LENGTH = 4
MAX_STREAM_LENGTH = 9
PAUSE_TIME = 0.1
STREAM_CHARS = ['0', '1']
DENSITY = 0.1
WIDTH = shutil.get_terminal_size()[0] - 1

print('Digital Stream Screensaver')
print('Press Ctrl-C to quit.')
time.sleep(2)

try:
    columns = [0] * WIDTH
    while True:
        for idx in range(WIDTH):
            if columns[idx] == 0:
                if random.random() <= DENSITY:
                    columns[idx] = random.randint(
                        MIN_STREAM_LENGTH, MAX_STREAM_LENGTH)

            if columns[idx] > 0:
                print(random.choice(STREAM_CHARS), end='')
                columns[idx] -= 1
            else:
                print(' ', end='')
        print()
        sys.stdout.flush()
        time.sleep(PAUSE_TIME)
except KeyboardInterrupt:
    sys.exit()
