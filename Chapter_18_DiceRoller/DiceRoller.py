import random

if __name__ == "__main__":
    print('Dice Roller')
    print('''Enter what kind and how many dice to roll. The format is the number of dice, followed by "d", 
followed by the number of sides the dice have. You can also add a plus or minus adjustment.

Examples:
3d6 rolls three 6-sided dice
1d10+2 rolls one 10-sided die, and adds 2
2d38-1 rolls two 38-sided die, and subtracts 1
QUIT quits the program
''')

    while True:
        while True:
            userInput = input('> ').lower()
            if 'd' in userInput or userInput == 'quit':
                break
            print('Invalid input.')

        if userInput == 'quit':
            print('Thanks for playing!')
            break

        numOfRolls, userInput = userInput.split('d')
        numOfRolls = int(numOfRolls)

        try:
            if '+' in userInput:
                numOfSide, bonusPoint = list(map(int, userInput.split('+')))
            elif '-' in userInput:
                numOfSide, bonusPoint = list(map(int, userInput.split('-')))
                bonusPoint *= -1
            else:
                numOfSide = int(userInput)
                bonusPoint = 0
        except ValueError:
            print('Invalid input. Enter something like "3d6" or "1d10+2".')
            continue

        diceRolls = [random.randint(1, numOfSide) for _ in range(numOfRolls)]
        totalValue = sum(diceRolls) + bonusPoint

        print(totalValue, end=' ')
        print('(', end='')
        print(', '.join(map(str, diceRolls)), end='')
        if bonusPoint != 0:
            print(f', +{bonusPoint}' if bonusPoint >
                  0 else f', {bonusPoint}', end='')
        print(')')
