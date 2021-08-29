import random
import sys

EMPTY_SPACE = '.'
GRID_LENGTH = 9
BOX_LENGTH = 3
FULL_GRID_SIZE = GRID_LENGTH * GRID_LENGTH


class SudokuGrid:
    def __init__(self, originalSetup):
        self.originalSetup = originalSetup
        self.grid = {}
        self.resetGrid()
        self.moves = []

    def resetGrid(self):
        for row in range(1, GRID_LENGTH + 1):
            for col in range(1, GRID_LENGTH + 1):
                self.grid[(row, col)] = EMPTY_SPACE

        assert len(self.originalSetup) == FULL_GRID_SIZE
        idx = 0
        while idx < FULL_GRID_SIZE:
            for row in range(GRID_LENGTH):
                for col in range(GRID_LENGTH):
                    self.grid[(row, col)] = self.originalSetup[idx]
                    idx += 1

    def display(self):
        print('   A B C   D E F   G H I')
        for row in range(GRID_LENGTH):
            for col in range(GRID_LENGTH):
                if col == 0:
                    print(f'{row+1}  ', end='')

                print(self.grid[(row, col)], end=' ')
                if col in [2, 5]:
                    print('|', end=' ')
            print()

            if row in [2, 5]:
                print('   ------+-------+------')

    def _is_complete_set(self, numbers):
        return sorted(numbers) == list('123456789')

    def is_solved(self):
        for col in range(GRID_LENGTH):
            colNumbers = [self.grid[(x, col)] for x in range(GRID_LENGTH)]
            if not self._is_complete_set(colNumbers):
                return False

        for row in range(GRID_LENGTH):
            rowNumbers = [self.grid[(row, y)] for y in range(GRID_LENGTH)]
            if not self._is_complete_set(rowNumbers):
                return False

        for boxX in (0, 3, 6):
            for boxY in (0, 3, 6):
                boxNumbers = []
                for x in range(BOX_LENGTH):
                    for y in range(BOX_LENGTH):
                        boxNumbers.append(self.grid[(boxX + x, boxY + y)])
                if not self._is_complete_set(boxNumbers):
                    return False

        return True

    def undo(self):
        if self.moves == []:
            return

        self.moves.pop()
        if self.moves == []:
            self.resetGrid()
        else:
            self.grid = self.moves[-1].copy()

    def make_move(self, row, column, number):
        col = 'ABCDEFGHI'.index(column)
        row = int(row) - 1

        if self.originalSetup[row * GRID_LENGTH + col] != EMPTY_SPACE:
            return False

        self.grid[(row, col)] = number
        self.moves.append(self.grid.copy())
        return True


if __name__ == "__main__":
    print("""Sudoku Puzzle, by Al Sweigart al@inventwithpython.com

    Sudoku is a number placement logic puzzle game. A Sudoku grid is a 9x9
    grid of numbers. Try to place numbers in the grid such that every row,
    column, and 3x3 box has the numbers 1 through 9 once and only once.

    For example, here is a starting Sudoku grid and its solved form:

        5 3 . | . 7 . | . . .     5 3 4 | 6 7 8 | 9 1 2
        6 . . | 1 9 5 | . . .     6 7 2 | 1 9 5 | 3 4 8
        . 9 8 | . . . | . 6 .     1 9 8 | 3 4 2 | 5 6 7
        ------+-------+------     ------+-------+------
        8 . . | . 6 . | . . 3     8 5 9 | 7 6 1 | 4 2 3
        4 . . | 8 . 3 | . . 1 --> 4 2 6 | 8 5 3 | 7 9 1
        7 . . | . 2 . | . . 6     7 1 3 | 9 2 4 | 8 5 6
        ------+-------+------     ------+-------+------
        . 6 . | . . . | 2 8 .     9 6 1 | 5 3 7 | 2 8 4
        . . . | 4 1 9 | . . 5     2 8 7 | 4 1 9 | 6 3 5
        . . . | . 8 . | . 7 9     3 4 5 | 2 8 6 | 1 7 9
    """)
    input('Press Enter to begin...')

    with open('sudokupuzzles.txt') as puzzleSource:
        puzzles = puzzleSource.readlines()

    for i, puzzle in enumerate(puzzles):
        puzzles[i] = puzzle.strip()

    grid = SudokuGrid(random.choice(puzzles))

    while True:
        grid.display()
        if grid.is_solved():
            print('Congratulations! You solved the puzzle!')
            print('Thanks for playing!')
            sys.exit()

        while True:
            print()
            print('Enter a move, or RESET, NEW, UNDO, ORIGINAL, or QUIT:')
            print('(For example, a move looks like "B4 9".)')
            userMove = input('> ').upper()

            if userMove == 'QUIT':
                print('Thanks for playing!')
                sys.exit()
            if userMove in ['RESET', 'NEW', 'UNDO', 'ORIGINAL']:
                break
            if len(userMove.split()) == 2:
                space, number = userMove.split()
                if len(space) != 2:
                    print('Invalid input.')
                    continue

                column, row = space
                if column in list('ABCDEFGHI') and (row.isdecimal() and eval(f'1<={row}<=9')) and number.isdecimal():
                    break

            print('Invalid input.')

        print()

        if userMove == 'RESET':
            grid.resetGrid()
            continue
        if userMove == 'NEW':
            grid = SudokuGrid(random.choice(puzzles))
            continue
        if userMove == 'UNDO':
            grid.undo()
            continue
        if userMove == 'ORIGINAL':
            originalGrid = SudokuGrid(grid.originalSetup)
            print('The original grid looked like this:')
            originalGrid.display()
            input('Press Enter to continue...')
            continue

        if grid.make_move(row, column, number) == False:
            print("You cannot overwrite the original grid's numbers.")
            print('Enter ORIGINAL to view the original grid.')
            input('Press Enter to continue...')
