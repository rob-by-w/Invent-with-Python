import shutil
import sys
import math
import time

WIDTH, HEIGHT = shutil.get_terminal_size()
WIDTH -= 1

print('Sine Message')
print('(Press Ctrl-C to quit.)')
print()
try:
    print(f"What message do you want to display? (Max {WIDTH//2} chars.)")
    while True:
        userMessage = input('> ')
        if 1 <= len(userMessage) <= WIDTH//2:
            break
        print(f'Message must be 1 to {WIDTH//2} characters long.')

    step = 0
    multiplier = (WIDTH - len(userMessage)) / 2
    while True:
        sinOfStep = math.sin(step)
        print(' ' * int((sinOfStep + 1) * multiplier) + userMessage)
        time.sleep(0.1)
        step += 0.25
except KeyboardInterrupt:
    sys.exit()
