import shutil

WIDTH, HEIGHT = shutil.get_terminal_size()
WIDTH -= 1
HEXGRID = r"/ \_"

if __name__ == "__main__":
    patternRecursion = WIDTH // len(HEXGRID)
    reminderLength = WIDTH % len(HEXGRID)
    for row in range(HEIGHT):
        currentCell = HEXGRID[2:] + HEXGRID[:2] if row % 2 else HEXGRID
        print(currentCell * (patternRecursion) + currentCell[:reminderLength])
