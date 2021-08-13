import sys
import random

DOOR = [['+------+',
        '|      |',
         '|   1  |',
         '|      |',
         '|      |',
         '|      |',
         '+------+'],
        ['+------+',
        '|      |',
         '|   2  |',
         '|      |',
         '|      |',
         '|      |',
         '+------+'],
        ['+------+',
        '|      |',
         '|   3  |',
         '|      |',
         '|      |',
         '|      |',
         '+------+']]
GOAT = ['+------+',
        '|  ((  |',
        '|  oo  |',
        '| /_/|_|',
        '|    | |',
        '|GOAT|||',
        '+------+']
CAR = ['+------+',
       '| CAR! |',
       '|    __|',
       '|  _/  |',
       '| /_ __|',
       '|   O  |',
       '+------+']


def print_door(doorList):
    for line in zip(*doorList):
        print('  '.join(line))


if __name__ == "__main__":
    print('The Monty Hall Problem')
    print()
    print('In the Monty Hall game show, you can pick one of three doors. One door has a new car for a prize. The other two doors have worthless goats:')

    print_door(DOOR)
    print('Say you pick Door #1. Before the door you choose is opened, another door with a goat is opened')
    print_door([DOOR[0], DOOR[1], GOAT])
    print('You can choose to either open the door you originally picked or swap to the other unopened door.')
    print()
    print("It may seem like it doesn't matter if you swap or not, but your odds do improve if you swap doors! This program demonstrates the Monty Hall problem by letting you do repeated experiments.")
    print()
    input('Press Enter to start...')

    swapped = {'win': 0, 'lose': 0}
    noSwapping = {'win': 0, 'lose': 0}

    while True:

        openedDoor = []
        carDoor = random.randint(0, 2)
        goatDoor = list(range(3))
        goatDoor.remove(carDoor)
        doors = [GOAT if i != carDoor else CAR for i in range(3)]

        print_door(DOOR)
        print('Pick a door 1, 2, or 3 (or "QUIT" to stop):')
        while True:
            userPick = input('> ').upper()
            if userPick == 'QUIT':
                sys.exit()
            if userPick.isdigit() and eval(f'1<={userPick}<=3'):
                userPick = int(userPick) - 1
                break
            print('Invalid input.')

        try:
            goatDoor.remove(userPick)
        except ValueError:
            pass

        randomGoatDoor = random.choice(goatDoor)
        openedDoor.append(randomGoatDoor)
        print_door([DOOR[i] if i not in openedDoor else doors[i]
                   for i in range(3)])
        print(f'Door {randomGoatDoor+1} contains a goat!')

        print('Do you want to swap doors? Y/N')
        while True:
            swapOrNot = input('> ').upper()
            if swapOrNot in ['Y', 'YES']:
                userPick = [i for i in range(3) if i not in (
                    userPick, randomGoatDoor)][0]
                break
            if swapOrNot in ['N', 'NO']:
                break
            if swapOrNot == 'QUIT':
                sys.exit()
            print('Invalid input. Please enter Y or N.')

        print_door(doors)
        print(f'Door {carDoor+1} has the car!')

        if userPick == carDoor:
            print('You won!')
            if swapOrNot in ['Y', 'YES']:
                swapped['win'] += 1
            elif swapOrNot in ['N', 'NO']:
                noSwapping['win'] += 1
        else:
            print('You lost!')
            if swapOrNot in ['Y', 'YES']:
                swapped['lose'] += 1
            elif swapOrNot in ['N', 'NO']:
                noSwapping['lose'] += 1

        swapSuccessRate = round(100 * swapped['win']/(
            swapped['win'] + swapped['lose']) if swapped['win'] + swapped['lose'] > 0 else 0.0, 1)
        noSwapSuccessRate = round(100 * noSwapping['win']/(
            noSwapping['win'] + noSwapping['lose']) if noSwapping['win'] + noSwapping['lose'] > 0 else 0.0, 1)
        print()
        print(
            f"Swapping:      {swapped['win']} wins, {swapped['lose']} loses, success rate {swapSuccessRate}%")
        print(
            f"Not swapping:  {noSwapping['win']} wins, {noSwapping['lose']} loses, success rate {noSwapSuccessRate}%")
        print()
        input('Press Enter to repeat the experiment...')
