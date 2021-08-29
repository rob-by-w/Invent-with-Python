import random
import pyperclip


def main():
    print('sPoNgEcAsE')
    print()
    print('eNtEr YoUr MeSsAgE:')
    userMessage = convert_to_spongecase(input('> '))
    pyperclip.copy(userMessage)
    print(userMessage)
    print(convert_to_spongecase('(copied spongetext to clipboard.)'))


def convert_to_spongecase(message):
    output = ''
    useUpper = False

    for char in message:
        if not char.isalpha():
            output += char
            continue

        output += char.upper() if useUpper else char.lower()
        if random.random() <= 0.9:
            useUpper = not useUpper
    return output


if __name__ == "__main__":
    main()
