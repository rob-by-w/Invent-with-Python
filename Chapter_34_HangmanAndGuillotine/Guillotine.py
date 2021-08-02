import random

BLANK = '_'
CATEGORY = 'Animals'
WORDS = 'ANT BABOON BADGER BAT BEAR BEAVER CAMEL CAT CLAM COBRA COUGAR COYOTE CROW DEER DOG DONKEY DUCK EAGLE FERRET FOX FROG GOAT GOOSE HAWK LION LIZARD LLAMA MOLE MONKEY MOOSE MOUSE MULE NEWT OTTER OWL PANDA PARROT PIGEON PYTHON RABBIT RAM RAT RAVEN RHINO SALMON SEAL SHARK SHEEP SKUNK SLOTH SNAKE SPIDER STORK SWAN TIGER TOAD TROUT TURKEY TURTLE WEASEL WHALE WOLF WOMBAT ZEBRA'.split()

GUILLOTINE = [r"""
    |
    |
    |
    |
    |
    |
    |===""",
              r"""
    |   |
    |   |
    |   |
    |   |
    |   |
    |   |
    |===|""",
              r"""
    |===|
    |   |
    |   |
    |   |
    |   |
    |   |
    |===|""",
              r"""
    |===|
    |   |
    |   |
    |   |
    |   |
    |\ /|
    |===|""",
              r"""
    |===|
    |   |
    |   |
    |   |
    |/-\|
    |\ /|
    |===|""",
              r"""
    |===|
    || /|
    ||/ |
    |   |
    |/-\|
    |\ /|
    |===|""",
              r"""
    |===|
    || /|
    ||/ |
    |   |
    |/-\|
    |\O/|
    |===|"""]


def main():
    pictureCount = 0
    userGuess = []
    missedGuess = []
    secretWord = random.choice(WORDS)

    print('Hangman')

    while True:
        print(GUILLOTINE[pictureCount])

        if pictureCount == len(GUILLOTINE)-1:
            print('You have run out of guesses!.')
            print(f'The word was "{secretWord}"')
            break

        print(f'The category is: {CATEGORY}')
        print('Missed letters: ', end='')
        print(' '.join(missedGuess) if missedGuess !=
              [] else 'No missed letters yet.')
        print(
            ' '.join([BLANK if char not in userGuess else char for char in secretWord]))
        print('Guess a letter.')
        while True:
            guessChar = input('> ').upper()
            if guessChar.isalpha() and guessChar not in userGuess and len(guessChar) == 1:
                userGuess.append(guessChar)
                break
            print('Invalid input. Please input a letter.')

        if set(secretWord).issubset(set(userGuess)):
            print(f'Yes! The secret word is: {secretWord}')
            print('You have won!')
            break

        if userGuess[-1] not in secretWord:
            missedGuess.append(userGuess[-1])
            pictureCount += 1


if __name__ == "__main__":
    main()
