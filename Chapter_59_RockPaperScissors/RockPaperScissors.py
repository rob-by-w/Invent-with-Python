import sys
import time
import random

ROCK = 'ROCK'
PAPER = 'PAPER'
SCISSORS = 'SCISSORS'

print('Rock, Paper, Scissors')
print('- Rock beats scissors.')
print('- Paper beats rocks.')
print('- Scissors beats paper')

score = {'win': 0, 'lose': 0, 'draw': 0}
while True:
    print('Enter your move: (R)ock  (P)aper  (S)cissors or (Q)uit')
    while True:
        userMove = input('> ').upper()
        if userMove in ['Q', 'QUIT']:
            print(
                f"Your score is: {score['win']} Wins, {score['lose']} Losses, {score['draw']} Ties")
            print('Thanks for playing!')
            sys.exit()
        if userMove in ['R', 'ROCK']:
            userMove = ROCK
            break
        if userMove in ['P', 'PAPER']:
            userMove = PAPER
            break
        if userMove in ['S', 'SCISSORS']:
            userMove = SCISSORS
            break
        print('Invalid input.')

    compMove = random.choice([ROCK, PAPER, SCISSORS])

    print(f'{userMove} versus...')
    time.sleep(random.random())
    for num in range(1, 4):
        print(f'{num}...')
        time.sleep(random.random())
    print(compMove)

    if userMove == ROCK:
        if compMove == ROCK:
            print('Ties!')
            score['draw'] += 1
        elif compMove == PAPER:
            print('You lose!')
            score['lose'] += 1
        elif compMove == SCISSORS:
            print('You win!')
            score['win'] += 1
    elif userMove == PAPER:
        if compMove == PAPER:
            print('Ties!')
            score['draw'] += 1
        elif compMove == SCISSORS:
            print('You lose!')
            score['lose'] += 1
        elif compMove == ROCK:
            print('You win!')
            score['win'] += 1
    elif userMove == SCISSORS:
        if compMove == SCISSORS:
            print('Ties!')
            score['draw'] += 1
        elif compMove == ROCK:
            print('You lose!')
            score['lose'] += 1
        elif compMove == PAPER:
            print('You win!')
            score['win'] += 1

    print(f"{score['win']} Wins, {score['lose']} Losses, {score['draw']} Ties")
