import random
import time
import os

HEIGHT = 9
WIDTH = 80

QUIZ_DURATION = 30
REWARD = 4
PENALTY = 1

MIN_DICE = 2
MAX_DICE = 5

DICE = {
    1: ['+-------+',
        '|       |',
        '|   O   |',
        '|       |',
        '+-------+'],
    2: ['+-------+',
        '| O     |',
        '|       |',
        '|     O |',
        '+-------+'],
    3: ['+-------+',
        '| O     |',
        '|   O   |',
        '|     O |',
        '+-------+'],
    4: ['+-------+',
        '| O   O |',
        '|       |',
        '| O   O |',
        '+-------+'],
    5: ['+-------+',
        '| O   O |',
        '|   O   |',
        '| O   O |',
        '+-------+'],
    6: ['+-------+',
        '| O   O |',
        '| O   O |',
        '| O   O |',
        '+-------+']}


if __name__ == "__main__":
    print('Dice Math')
    print('Add up the sides of all the dice displayed on the screen.')
    print(f'You have {QUIZ_DURATION} seconds to answer as many as possible.')
    print(
        f'You get {REWARD} points for each correct answer and lose {PENALTY} point for each incorrect answer.')
    print()
    input('Press Enter to begin...')

    correctAnswer = 0
    incorrectAnswer = 0
    startTime = time.time()

    while time.time() < startTime + QUIZ_DURATION:
        os.system('cls' if os.name == 'nt' else 'clear')
        displayCells = {}
        for x in range(WIDTH):
            for y in range(HEIGHT):
                displayCells[(x, y)] = ' '

        numOfDice = random.randint(MIN_DICE, MAX_DICE)
        dicePositions = [(random.randint(0, WIDTH-len(DICE[1][0])), random.randint(0, HEIGHT-len(DICE[1])))
                         for _ in range(numOfDice)]
        diceValue = 0

        for position in dicePositions:
            while True:
                flagOccupied = False
                for x in range(position[0], position[0]+len(DICE[1][0])):
                    for y in range(position[1], position[1]+len(DICE[1])):
                        if displayCells[(x, y)] != ' ':
                            flagOccupied = True
                            break

                    if flagOccupied:
                        break

                if not flagOccupied:
                    break

                position = [random.randint(
                    0, WIDTH-len(DICE[1][0])), random.randint(0, HEIGHT-len(DICE[1]))]

            value = random.randint(1, 6)
            diceValue += value

            currentDice = DICE[value].copy()
            if random.randint(0, 1) == 1:
                currentDice[1], currentDice[3] = currentDice[3], currentDice[1]
            for y in range(len(DICE[value])):
                for x in range(len(DICE[value][0])):
                    displayCells[(position[0]+x, position[1]+y)
                                 ] = currentDice[y][x]

        for y in range(HEIGHT):
            for x in range(WIDTH):
                print(displayCells[(x, y)], end='')
            print()

        userAnswer = input('Enter the sum: ')

        if userAnswer.isdigit():
            userAnswer = int(userAnswer)
            if userAnswer == diceValue:
                correctAnswer += 1
            else:
                incorrectAnswer += 1
        else:
            incorrectAnswer += 1

    os.system('cls' if os.name == 'nt' else 'clear')
    score = correctAnswer * REWARD - incorrectAnswer * PENALTY
    print(f'Answered: {correctAnswer + incorrectAnswer}')
    print(f'Correct: {correctAnswer}')
    print(f'Incorrect: {incorrectAnswer}')
    print(f'Your score is {score}')
