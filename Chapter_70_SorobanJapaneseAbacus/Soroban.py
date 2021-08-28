import sys

NUMBER_OF_DIGITS = 10


def main():
    print('Soroban')
    print()

    charsDict = {}
    for idx, char in enumerate(list('qwertyuiop')):
        charsDict[char] = 10 ** (9 - idx)
    for idx, char in enumerate(list('asdfghjkl;')):
        charsDict[char] = -1 * (10 ** (9 - idx))

    sorobanNum = 0

    while True:
        display_soroban(sorobanNum)
        display_controls()

        while True:
            userInput = input('> ').lower()
            if userInput == 'quit':
                sys.exit()
            if userInput.isdecimal():
                sorobanNum = int(userInput)
                break
            if userInput in charsDict.keys():
                sorobanNum += charsDict[userInput]
                break
            print('Invalid input.')

        if sorobanNum < 0:
            sorobanNum = 0
        if sorobanNum > 10 ** 10 - 1:
            sorobanNum = 10**10 - 1


def display_soroban(num):
    numList = list(str(num).zfill(NUMBER_OF_DIGITS))
    hasBead = []

    beadPatternPerRow = ['01234', '56789', '12346789',
                         '234789', '034589', '014569', '012567', '01235678']
    for row in beadPatternPerRow:
        for i in numList:
            hasBead.append('O' if i in row else '|')

    chars = hasBead + numList
    print("""
+================================+
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  |  |  |  |  |  |  |  |  |  |  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
+================================+
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
I  {}  {}  {}  {}  {}  {}  {}  {}  {}  {}  I
+=={}=={}=={}=={}=={}=={}=={}=={}=={}=={}==+""".format(*chars))


def display_controls():
    print('  +q  w  e  r  t  y  u  i  o  p')
    print('  -a  s  d  f  g  h  j  k  l  ;')
    print('(Enter a number, "quit", or a stream of up/down letters.)')


if __name__ == "__main__":
    main()
