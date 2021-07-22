import bext, random

width, height = bext.size()

try:
    while True:
        bext.fg('random')
        bext.bg('random')
        x = random.randint(0, width - 1)
        y = random.randint(0, height - 1)

        if x == width -1 and y == height - 1:
            continue # Windows has weird behavior where a character at the end of the row always moves the cursor to the next row.
        bext.goto(x, y)
        print('*', end='')
except KeyboardInterrupt:
    pass