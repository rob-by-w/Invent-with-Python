import string
import pyperclip

ALPHABET = list(string.ascii_uppercase)


def main():
    print('Vigenère Cipher')
    print('The Vigenère cipher is a polyalphabetic substitution cipher that was powerful enough to remain unbroken for centuries.')

    print('Do you want o (e)ncrypt of (d)ecrypt?')
    while True:
        mode = input('> ').lower()
        if mode in ['e', 'd']:
            break
        print('Invalid input. Please enter "e" to encrtpy or "d" to decrpyt')

    while True:
        print('Please specify the key to use.')
        print('It can be a word or any combination of letters:')
        userKey = input('> ').upper()

        if userKey.isalpha():
            break
        print('Invalid key.')

    print('Enter the message to encrypt.' if mode ==
          'e' else 'Enter the message to decrypt.')
    userMessage = input('> ')

    if mode == 'e':
        encrypt_message(userKey, userMessage)
    elif mode == 'd':
        decrypt_message(userKey, userMessage)


def encrypt_message(key, message):
    idx = 0
    output = ''
    for char in message:
        if not char.isalpha():
            output += char
        elif char.isupper():
            output += chr((ord(char) - ord('A') +
                          ALPHABET.index(key[idx % len(key)])) % 26 + ord('A'))
            idx += 1
        elif char.islower():
            output += chr((ord(char) - ord('a') +
                          ALPHABET.index(key[idx % len(key)])) % 26 + ord('a'))
            idx += 1

    print('Encrypted message: ')
    print(output)
    pyperclip.copy(output)
    print('Full encrypted text copied to clipboard.')


def decrypt_message(key, message):
    idx = 0
    output = ''
    for char in message:
        if not char.isalpha():
            output += char
        elif char.isupper():
            output += chr((ord(char) - ord('A') -
                          ALPHABET.index(key[idx % len(key)])) % 26 + ord('A'))
            idx += 1
        elif char.islower():
            output += chr((ord(char) - ord('a') -
                          ALPHABET.index(key[idx % len(key)])) % 26 + ord('a'))
            idx += 1

    print('Decrypted message: ')
    print(output)
    pyperclip.copy(output)
    print('Full decrypted text copied to clipboard.')


if __name__ == "__main__":
    main()
