import time
import random
import itertools

PAUSE_AMOUNT = 1
DIE = list(range(1, 7))
OTUCOME = {(1, 1): 'ピンゾロの丁', (1, 2): 'イチニの半', (1, 3): 'サンミチの丁', (1, 4): 'ヨイチの半', (1, 5): 'グイチの', (1, 6): 'イチロクの半',
           (2, 2): 'ニゾロの丁', (2, 3): 'サニの半', (2, 4): 'シニの丁', (2, 5): 'グニの半', (2, 6): 'ニロクの丁',
           (3, 3): 'サンゾロの丁', (3, 4): 'シソウの半', (3, 5): 'グサンの丁', (3, 6): 'サブロクの',
           (4, 4): 'シゾロの丁', (4, 5): 'グシの半', (4, 6): 'シロクの丁',
           (5, 5): 'ゴゾロの丁', (5, 6): 'ゴロクの半', (6, 6): 'ロクゾロの丁'}


def main():
    print('''Cho-Han
    In this traditional Japanese dice game, two dice are rolled in a bamboo
    cup by the dealer sitting on the floor. The player must guess if the
    dice total to an even (cho) or odd (han) number.
    ''')

    money = 5000

    while money > 0:
        print(
            f'You have {money} mon. How much do you bet? (1-{money} or QUIT)')
        inputBet = input_bet(money)
        if eval(str(inputBet).lower() + '== quit'):
            break

        print('The dealer swirls the cup and you hear the rattle of dice.')
        time.sleep(PAUSE_AMOUNT)
        print('The dealer slams the cup on the floor, still covering the dice and asks for your bet.')
        print(' '*5 + 'CHO (even) or HAN (odd)?')
        userGuess = input_guess()

        print('The dealer lifts the cup to reaveal:')
        diceNum = tuple(sorted(random.choices(DIE, k=2)))
        print(' '*(8-len(OTUCOME[diceNum])) + OTUCOME[diceNum])
        print(' '*5 + str(diceNum[0]) + ' - ' + str(diceNum[1]))

        if (sum(diceNum) % 2 and userGuess == 'HAN') or (sum(diceNum) % 2 == 0 and userGuess == 'CHO'):
            print(f'You won! You take {2*inputBet} mon.')
            print(f'The house collects a {int(0.1*inputBet)} mon fee.')
            money += int(1.9*inputBet)
        else:
            print(f'You lost. The house take yours {inputBet} mon bet.')
            money -= inputBet


def input_bet(userMoney):
    while True:
        bet = input('> ')
        if bet.isdigit() and eval(bet + '<=' + str(userMoney)):
            bet = int(bet)
            print(f'Bet: {bet} mon')
            break
        elif bet.lower() == 'quit':
            print(f'You quit the game. Your money is {userMoney} mon.')
            break
        print(
            f'Invalid input. Please input a bet in range of 1-{userMoney}, or QUIT')

    return bet


def input_guess():
    while True:
        guess = input('> ').upper()
        if guess in ['CHO', 'HAN']:
            print(f'Your guess is {guess}')
            break
        print(f'Invalid input. Please input CHO or HAN')

    return guess


if __name__ == '__main__':
    main()
