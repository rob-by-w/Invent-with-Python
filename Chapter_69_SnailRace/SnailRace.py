import os
import time
import random
import sys

MAX_SNAILS_NUM = 8
MAX_NAME_LENGTH = 20
COURSE_LENGTH = 40


def print_race(snailProgress):
    os.system('cls' if os.name == 'nt' else 'clear')
    print('START' + ' ' * (COURSE_LENGTH - len('START')) + 'FINISH')
    print('|' + ' ' * (COURSE_LENGTH - len('|')) + '|')
    for snail, progress in snailProgress.items():
        print(' ' * progress + snail[:MAX_NAME_LENGTH])
        print('.' * progress + '@v')


print('Snail Race')
print('''
    @v  <--  snail
''')

print(f'How main snails will race? Max: {MAX_SNAILS_NUM}')
while True:
    numOfSnails = input('> ')
    if numOfSnails.isdigit() and eval(f'1 < {numOfSnails} <= {MAX_SNAILS_NUM}'):
        numOfSnails = int(numOfSnails)
        break
    print(f'Invalid input. Enter a number between 2 and {MAX_SNAILS_NUM}')

snailNames = []
for i in range(numOfSnails):
    print(f"Enter snail #{i+1}'s name:")
    while True:
        name = input('> ')
        if name not in snailNames and len(name) < MAX_NAME_LENGTH:
            snailNames.append(name)
            break
        print('Inputted name is already used')

input('Press enter to start the race')
os.system('cls' if os.name == 'nt' else 'clear')

snailProgress = {snailName: 0 for snailName in snailNames}
print_race(snailProgress)
time.sleep(1.5)

while True:
    for _ in range(random.randint(1, numOfSnails // 2)):
        randomSnail = random.choice(snailNames)
        snailProgress[randomSnail] += 1

        if snailProgress[randomSnail] == COURSE_LENGTH:
            print_race(snailProgress)
            print(f'{randomSnail} has won the race!')
            sys.exit()

    time.sleep(0.5)
    print_race(snailProgress)
