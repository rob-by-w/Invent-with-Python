import random
import os

GOLD = 'GOLD'
SILVER = 'SILVER'
BRONZE = 'BRONZE'

QUESTION_FACE = ['+-----------+',
                 '|           |',
                 '|           |',
                 '|     ?     |',
                 '|           |',
                 '|           |',
                 '+-----------+']
STAR_FACE = ['+-----------+',
             '|     .     |',
             '|    ,O,    |',
             "| 'ooOOOoo' |",
             '|   `OOO`   |',
             "|   O' 'O   |",
             '+-----------+']
SKULL_FACE = ['+-----------+',
              '|    ___    |',
              '|   /   \   |',
              '|  |() ()|  |',
              '|   \ ^ /   |',
              '|    VVV    |',
              '+-----------+']


class Player():
    def __init__(self, name):
        self.name = name
        self.score = 0


if __name__ == "__main__":
    print('Lucky Stars')
    print('''
A "press your luck" game where you roll dice with Stars, Skulls, and Question Marks.

On your turn, you pull three random dice from the dice cup and roll them. You can roll
Stars, Skulls, and Question Marks. You can end your turn and get one point per Star.
If you choose to roll again, you keep the Question Marks and pull new dice to replace
the Stars and Skulls. If you collect three Skulls, you lose all your Stars and end your turn.

When a player gets 13 points, everyone else gets one more turn before the game ends.
Whoever has the most points wins.

There are 6 Gold dice, 4 Silver dice, and 3 Bronze dice in the cup.
Gold dice have more Stars, Bronze dice have more Skulls, and Silver is even.
''')

    print('How many players will join the game?')
    while True:
        playerNum = input('> ')
        if playerNum.isdigit() and eval(playerNum + '>0'):
            playerNum = int(playerNum)
            break
        print('Invalid input. Please enter a number larger than 0.')

    playerList = []
    print("Enter the players' name:")
    for idx in range(playerNum):
        playerList.append(Player(input(f'Player {idx+1}: ')))

    turn = 0
    lastPlayer = None
    while True:
        print('Scores: ', end='')
        print(
            ', '.join([f'{player.name}={player.score}' for player in playerList]))

        input('Press Enter to continue...')
        os.system('cls' if os.name == 'nt' else 'clear')

        player = playerList[turn]
        starCount = 0
        skullCount = 0
        diceOnHands = []
        dice = [GOLD] * 6 + [SILVER] * 4 + [BRONZE] * 3
        random.shuffle(dice)
        print(f"It is {player.name}'s turn.")

        while True:
            if len(dice) < (3 - len(diceOnHands)):
                player.score += starCount
                print(
                    f"There aren't enought dice left in the cup to continue {player.name}'s turn.")
                break

            diceFace = []
            for _ in range(3 - len(diceOnHands)):
                diceOnHands.append(dice.pop(0))

            for rollDice in diceOnHands:
                roll = random.randint(1, 6)
                if rollDice == GOLD:
                    if 1 <= roll <= 3:
                        diceFace.append(STAR_FACE)
                        starCount += 1
                    elif 4 <= roll <= 5:
                        diceFace.append(QUESTION_FACE)
                    else:
                        diceFace.append(SKULL_FACE)
                        skullCount += 1
                elif rollDice == SILVER:
                    if 1 <= roll <= 2:
                        diceFace.append(STAR_FACE)
                        starCount += 1
                    elif 3 <= roll <= 4:
                        diceFace.append(QUESTION_FACE)
                    else:
                        diceFace.append(SKULL_FACE)
                        skullCount += 1
                elif rollDice == BRONZE:
                    if 1 <= roll <= 3:
                        diceFace.append(SKULL_FACE)
                        skullCount += 1
                    elif 4 <= roll <= 5:
                        diceFace.append(QUESTION_FACE)
                    else:
                        diceFace.append(STAR_FACE)
                        starCount += 1

            for line in list(zip(*diceFace)):
                print('  '.join(line))
            print(' ' * (9-len(diceOnHands[0])) + diceOnHands[0] + ' ' * (15 - len(
                diceOnHands[1])) + diceOnHands[1] + ' ' * (15-len(diceOnHands[2])) + diceOnHands[2])
            print(
                f'Stars collected: {starCount}    Skulls collected: {skullCount}')

            if skullCount >= 3:
                player.score = 0
                print('You have collected 3 Skulls. You lost all you Stars.')
                break

            keepDiceIdx = [idx for idx, face in enumerate(
                diceFace) if face == QUESTION_FACE]
            diceOnHands = [die for idx, die in enumerate(
                diceOnHands) if idx in keepDiceIdx]
            print('Do you want to roll again? Y/N')
            while True:
                rollAgain = input('> ').upper()
                if rollAgain in ['YES', 'Y', 'NO', 'N']:
                    break
                print('Invalid input. Please enter Y or N.')
            if rollAgain in ['N', 'NO']:
                player.score += starCount

                if player.score >= 13 and lastPlayer == None:
                    lastPlayer = player.name
                    print('\n' + '#' * 60)
                    print(f'{player.name} has reached 13 points!!!')
                    print('Everyone else will get one more turn!')
                    print('#' * 60 + '\n')

                break

        turn = (turn + 1) % playerNum
        if lastPlayer == playerList[turn].name:
            break

    input('Press Enter to continue...')
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Game has ended.')
    print('Scores: ', end='')
    print(
        ', '.join([f'{player.name}={player.score}' for player in playerList]))

    maxScore = max([player.score for player in playerList])
    winner = [player.name for player in playerList if player.score == maxScore]

    print('The winner is ' if len(winner) == 1 else 'The winners are ', end='')
    print(', '.join(winner) + f' with the score of {maxScore}.')
