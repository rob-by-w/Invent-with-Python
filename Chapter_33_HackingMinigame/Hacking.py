import random

GARBAGE_CHARS = list('~!@#$%^&*()_+-={}[]|;:,.<>?/')
PASSWORDS = ['RESOLVE', 'REFUGEE', 'PENALTY', 'CHICKEN',
             'ADDRESS', 'DESPITE', 'DISPLAY', 'IMPROVE']
MEMORY_LENGTH = 16
NUM_OF_GUESS = 4
LEFT_INDENT = ' ' * 2
RIGHT_INDENT = ' ' * 6


def main():
    print('Hacking Minigame')
    print("Find the password in the computer's memory:")
    print_memory()

    randomPassword = random.choice(PASSWORDS)
    for guessLeft in range(NUM_OF_GUESS, 0, -1):
        print(f'Enter passoword: ({guessLeft} tries remaining)')
        userGuess = input('> ').upper()
        if userGuess == randomPassword:
            print('A C C E S S    G R A N T E D')
            break

        correctGuess = sum([randomPassword.count(char)
                           for char in set(userGuess)])
        print(f'Acccess Denied ({correctGuess}/{len(randomPassword)})')

        if guessLeft == 1:
            print(f'Out of tries. Secret password was {randomPassword}.')


def print_memory():
    memoryAddress = 16 * random.randint(0, 4000)
    passwordList = PASSWORDS[:]
    passwordLocations = random.sample(
        list(range(MEMORY_LENGTH)), len(PASSWORDS))
    random.shuffle(passwordLocations)
    random.shuffle(passwordList)

    for idx in range(MEMORY_LENGTH//2):
        if idx in passwordLocations:
            password = passwordList.pop(0)
            insertionIdx = random.randint(0, 9)
            garbageChars = random.sample(GARBAGE_CHARS, 9)
        else:
            password = ''
            insertionIdx = 15
            garbageChars = random.sample(GARBAGE_CHARS, 16)
        print('0x' + hex(memoryAddress).zfill(4) + LEFT_INDENT +
              ''.join(garbageChars[:insertionIdx]) + password + ''.join(garbageChars[insertionIdx:]) + RIGHT_INDENT, end='')

        if idx + MEMORY_LENGTH//2 in passwordLocations:
            password = passwordList.pop(0)
            insertionIdx = random.randint(0, 9)
            garbageChars = random.sample(GARBAGE_CHARS, 9)
        else:
            password = ''
            insertionIdx = 15
            garbageChars = random.sample(GARBAGE_CHARS, 16)
        print('0x' + hex(memoryAddress + 16 * MEMORY_LENGTH//2).zfill(4) + LEFT_INDENT +
              ''.join(garbageChars[:insertionIdx]) + password + ''.join(garbageChars[insertionIdx:]))

        memoryAddress += 16


if __name__ == "__main__":
    main()
