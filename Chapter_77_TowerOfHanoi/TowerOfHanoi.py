import sys

TOTAL_DISK = 5
COMPLETE_TOWER = list(range(TOTAL_DISK, 0, -1))


def main():
    print('The Tower of Hanoi')
    print("""
Move the tower of disks, one disk at a time, to another tower.
Larger disks cannot rest on top of a smaller disk.

More info at https://en.wikipedia.org/wiki/Tower_of_Hanoi""")

    towers = {'A': COMPLETE_TOWER.copy(), 'B': [], 'C': []}

    while True:
        display_tower(towers)
        sourceTower, destTower = ask_player_move(towers)

        disk = towers[sourceTower].pop()
        towers[destTower].append(disk)

        if COMPLETE_TOWER in (towers['B'], towers['C']):
            display_tower(towers)
            print('You have solved the puzzle! Well done!')
            sys.exit()


def display_disk(width):
    emptySpace = ' ' * (TOTAL_DISK - width)

    if width == 0:
        print(emptySpace + '||' + emptySpace, end='')
    else:
        disk = '@' * width
        numLabel = str(width).rjust(2, '_')
        print(emptySpace + disk + numLabel + disk + emptySpace, end='')


def display_tower(towers):
    print()
    for level in range(TOTAL_DISK, -1, -1):
        for tower in (towers['A'], towers['B'], towers['C']):
            if level >= len(tower):
                display_disk(0)
            else:
                display_disk(tower[level])
        print()

    emptySpace = ' ' * TOTAL_DISK
    print('{0} A{0}{0} B{0}{0} C\n'.format(emptySpace))


def ask_player_move(towers):
    while True:
        print('Enter the letters of "from" and "to" towers, or QUIT.')
        print('(e.g. AB to move a disk from tower A to tower B)')
        userMove = input('> ').upper().rstrip()

        if userMove == 'QUIT':
            print('Thanks for playing!')
            sys.exit()

        if userMove not in ('AB', 'AC', 'BA', 'BC', 'CA', 'CB'):
            print('Enter one of AB, AC, BA, BC, CA, or CB.')
            continue

        sourceTower, destTower = userMove[0], userMove[1]
        if len(towers[sourceTower]) == 0:
            print('You selected an empty tower.')
            continue
        elif len(towers[destTower]) == 0:
            return sourceTower, destTower
        elif towers[destTower][-1] < towers[sourceTower][-1]:
            print("Can't put larger disks on top of smaller ones.")
            continue
        else:
            return sourceTower, destTower


if __name__ == "__main__":
    main()
