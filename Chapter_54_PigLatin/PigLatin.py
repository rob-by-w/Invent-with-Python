import pyperclip

VOWELS = ('a', 'e', 'i', 'o', 'u', 'y')


def english_to_pig_latin(message):
    pigLatin = ''
    for word in message.split():
        prefixNonLetters = ''
        while len(word) > 0 and not word[0].isalpha():
            prefixNonLetters += word[0]
            word = word[1:]
        if len(word) == 0:
            pigLatin += prefixNonLetters + ' '
            continue

        suffixNonLetters = ''
        while not word[-1].isalpha():
            suffixNonLetters = word[-1] + suffixNonLetters
            word = word[:-1]

        wasUpper = word.isupper()
        wasTitle = word.istitle()
        word = word.lower()

        prefixConsonants = ''
        while len(word) > 0 and not word[0] in VOWELS:
            prefixConsonants += word[0]
            word = word[1:]

        word += prefixConsonants + 'ay' if prefixConsonants != '' else 'yay'
        if wasUpper:
            word = word.upper()
        if wasTitle:
            word = word.title()

        pigLatin += prefixNonLetters + word + suffixNonLetters + ' '
    return pigLatin


if __name__ == "__main__":
    print('Igpay Atinlay')
    print()
    print('Enter your message:')
    userSentence = english_to_pig_latin(input('> '))

    print(userSentence)
    pyperclip.copy(userSentence)
    print('(Copied pig latin to clipboard.)')
