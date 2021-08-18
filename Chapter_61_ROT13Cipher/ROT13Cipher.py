import sys
import pyperclip


def rotate_message(message):
    output = ''
    for char in message:
        if not char.isalpha():
            output += char
        elif char.isupper():
            output += chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        elif char.islower():
            output += chr((ord(char) - ord('a') + 13) % 26 + ord('a'))

    return output


if __name__ == "__main__":
    print('ROT13 Cipher')
    print()
    while True:
        print('Enter a message to encrypt/decrypt (or QUIT):')
        userMessage = input('> ')
        if userMessage.upper() == 'QUIT':
            sys.exit()

        rotatedMessage = rotate_message(userMessage)
        print(rotatedMessage)

        pyperclip.copy(rotatedMessage)
        print()
        print('(Copied to clipboard.)')
