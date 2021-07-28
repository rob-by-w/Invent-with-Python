import shutil
import sys

# Set up the constants for line characters:
UP_DOWN_CHAR = chr(9474)  # Character 9474 is '│'
LEFT_RIGHT_CHAR = chr(9472)  # Character 9472 is '─'
DOWN_RIGHT_CHAR = chr(9484)  # Character 9484 is '┌'
DOWN_LEFT_CHAR = chr(9488)  # Character 9488 is '┐'
UP_RIGHT_CHAR = chr(9492)  # Character 9492 is '└'
UP_LEFT_CHAR = chr(9496)  # Character 9496 is '┘'
UP_DOWN_RIGHT_CHAR = chr(9500)  # Character 9500 is '├'
UP_DOWN_LEFT_CHAR = chr(9508)  # Character 9508 is '┤'
DOWN_LEFT_RIGHT_CHAR = chr(9516)  # Character 9516 is '┬'
UP_LEFT_RIGHT_CHAR = chr(9524)  # Character 9524 is '┴'
CROSS_CHAR = chr(9532)  # Character 9532 is '┼'

CANVAS_WIDTH, CANVAS_HEIGHT = shutil.get_terminal_size()
CANVAS_WIDTH -= 1
CANVAS_HEIGHT -= 5


def print_canvas(canvasData, cx, cy):
    output = ''

    for row in range(CANVAS_HEIGHT):
        for col in range(CANVAS_WIDTH):
            if col == cx and row == cy:
                output += '#'
                continue

            cell = canvasData.get((col, row))
            if cell in (set(['W', 'S']), set(['W']), set(['S'])):
                output += UP_DOWN_CHAR
            elif cell in (set(['A', 'D']), set(['A']), set(['D'])):
                output += LEFT_RIGHT_CHAR
            elif cell == set(['S', 'D']):
                output += DOWN_RIGHT_CHAR
            elif cell == set(['S', 'A']):
                output += DOWN_LEFT_CHAR
            elif cell == set(['W', 'D']):
                output += UP_RIGHT_CHAR
            elif cell == set(['W', 'A']):
                output += UP_LEFT_CHAR
            elif cell == set(['W', 'S', 'D']):
                output += UP_DOWN_RIGHT_CHAR
            elif cell == set(['W', 'S', 'A']):
                output += UP_DOWN_LEFT_CHAR
            elif cell == set(['W', 'A', 'D']):
                output += UP_LEFT_RIGHT_CHAR
            elif cell == set(['S', 'A', 'D']):
                output += DOWN_LEFT_RIGHT_CHAR
            elif cell == set(['W', 'S', 'A', 'D']):
                output += CROSS_CHAR
            elif cell == None:
                output += ' '
        output += '\n'
    return output


canvas = {}
cursorX = 0
cursorY = 0

moves = []
while True:
    print(print_canvas(canvas, cursorX, cursorY))
    print('WASD key to move, H for help, C to clear, F to save, or QUIT.')

    userInput = input('> ').upper()
    if userInput == 'QUIT':
        print('Thanks for playing!')
        sys.exit()
    elif userInput == 'H':
        print('Enter W, A, S, and D characters to move the cursor and draw a line behind it as it moves. For example, ddd draws a line going right and sssdddwwwaaa draws a box.')
        print()
        print('You can save your drawing to a text file by entering F.')
        input('Press Enter to return to the program...')
        continue
    elif userInput == 'C':
        canvas = {}
        moves.append('C')
    elif userInput == 'F':
        try:
            print('Enter filename to save to:')
            filename = input('> ')

            if not filename.endswith('.txt'):
                filename += '.txt'
            with open(filename, 'w', encoding='utf-8') as outputFile:
                outputFile.write(''.join(moves) + '\n')
                outputFile.write(print_canvas(canvas, None, None))
        except:
            print('ERROR: Could not save file.')

    for command in userInput:
        if command not in ('W', 'A', 'S', 'D'):
            continue
        moves.append(command)

        if canvas == {}:
            if command in ('W', 'S'):
                canvas[(cursorX, cursorY)] = set(['W', 'S'])
            elif command in ('A', 'D'):
                canvas[(cursorX, cursorY)] = set(['A', 'D'])

        if command == 'W' and cursorY > 0:
            canvas[(cursorX, cursorY)].add(command)
            cursorY -= 1
        elif command == 'S' and cursorY < CANVAS_HEIGHT - 1:
            canvas[(cursorX, cursorY)].add(command)
            cursorY += 1
        elif command == 'A' and cursorX > 0:
            canvas[(cursorX, cursorY)].add(command)
            cursorX -= 1
        elif command == 'D' and cursorX < CANVAS_WIDTH - 1:
            canvas[(cursorX, cursorY)].add(command)
            cursorX += 1
        else:
            continue

        if (cursorX, cursorY) not in canvas:
            canvas[(cursorX, cursorY)] = set()

        if command == 'W':
            canvas[(cursorX, cursorY)].add('S')
        elif command == 'S':
            canvas[(cursorX, cursorY)].add('W')
        elif command == 'A':
            canvas[(cursorX, cursorY)].add('D')
        elif command == 'D':
            canvas[(cursorX, cursorY)].add('A')
