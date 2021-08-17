import time
import sys
import bext

print('Rainbow')
print('Press Ctrl-C to stop.')
time.sleep(1)

indent = 0
indentIncreasing = True

try:
    while True:
        print(' ' * indent, end='')
        bext.fg('red')
        print('##', end='')
        bext.fg('yellow')
        print('##', end='')
        bext.fg('green')
        print('##', end='')
        bext.fg('blue')
        print('##', end='')
        bext.fg('cyan')
        print('##', end='')
        bext.fg('purple')
        print('##')

        if indentIncreasing:
            indent += 1
            indentIncreasing = False if indent == 60 else indentIncreasing
        else:
            indent -= 1
            indentIncreasing = True if indent == 0 else indentIncreasing

        time.sleep(0.1)

except KeyboardInterrupt:
    sys.exit()
