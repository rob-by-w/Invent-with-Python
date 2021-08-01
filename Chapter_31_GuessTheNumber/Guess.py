import random

NUM_OF_GUESS = 10


def ask_guess():
    while True:
        guess = input('> ')
        if guess.isdigit and eval('1<=' + guess + '<=100'):
            return int(guess)
        print('Invalid input. Please enter an integer inclusive between 1 and 100.')


print('Guess the Number')
print('\nI am thinking of an integer inclusive between 1 and 100.')

randomNum = random.randint(1, 100)
for guessLeft in range(NUM_OF_GUESS, 0, -1):
    print(f'You have {guessLeft} guess left. Take a guess.' if guessLeft ==
          1 else f'You have {guessLeft} guesses left. Take a guess.')

    userGuess = ask_guess()
    if userGuess < randomNum:
        print('Your guess is too low.')
    elif userGuess > randomNum:
        print('Your guess is too high.')
    elif userGuess == randomNum:
        print('Yay! You guessed my number!')
        break

    if guessLeft == 0:
        print(f'Game over! The number I was thinking of was {randomNum}.')
        break
