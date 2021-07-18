from random import randint


def input_guess(count):
    print(f'Guess #{count}:')
    guess = input('> ')
    while len(guess) != 3 or not guess.isdigit():
        print('Invalid input. Please input 3-digit number.')
        guess = input('> ')

    return guess


def check_guess(guess):
    output = ''
    for idx, digit in enumerate(guess):
        if digit == answer[idx]:
            output += 'Fermi '
        elif digit in answer:
            output += 'Pico '

    if output == '':
        output = 'Bagels'

    return output


def continue_game():
    print('Do you want to play again? (yes or no)')
    retry = input('> ')
    while retry.lower() not in ['yes', 'no']:
        print('Invalid input. Please input yes or no.')
        retry = input('> ')

    return retry


if __name__ == '__main__':
    print('Bagels, a deductive logic game.\nI am thinking of a 3-digit number. Try to guess what it is.\nHere are some clues:')
    print('When I say:\tThat means:')
    print(' '*3 + 'Pico\t\tOne digit is correct but in the wrong position.')
    print(' '*3 + 'Fermi\tOne digit is correct and in the right position.')
    print(' '*3 + 'Bagels\tNo digit is correct')

    while True:
        numOfGuess = 10
        countGuess = 1
        answer = str(randint(100, 999))
        print(f'I have thought up a number. You have {numOfGuess} to get it')

        while True:
            if countGuess > numOfGuess:
                print('Game over')
                break

            userGuess = input_guess(countGuess)
            if userGuess == answer:
                print(f'Congratulations! Your guess {userGuess} is correct!')
                break

            print(check_guess(userGuess))
            countGuess += 1

        retry = continue_game()
        if retry.lower() == 'no':
            print('Thanks for playing!')
            break
        else:
            print('** New game started **')
