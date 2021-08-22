import random
import string
import pyperclip

ALPHABET = list(string.ascii_uppercase)


def sub_chiper_encrypt(message, key):
    output = ''
    for char in message:
        if char.isalpha():
            idx = ALPHABET.index(char.upper())
            output += key[idx] if char.isupper() else key[idx].lower()
        else:
            output += char
    return output


def sub_chipher_decrypt(message, key):
    output = ''
    for char in message:
        if char.isalpha():
            idx = key.index(char.upper())
            output += ALPHABET[idx] if char.isupper() else ALPHABET[idx].lower()
        else:
            output += char
    return output


if __name__ == "__main__":
    print('Smple Substitution Cipher')
    print('''
A simple substitution cipher has a one-to-one translation for each symbol
in the plaintext and each symbol in the ciphertext.
''')

    print('Do you want to (e)ncrypt or (d)ecrypt?')
    while True:
        mode = input('> ').lower()
        if mode in ['e', 'encrypt']:
            mode = 'e'
            break
        if mode in ['d', 'decrypt']:
            mode = 'd'
            break
        print('Invalid input.')

    print('Please specify the key to use.', end=' ')
    print('Or enter RANDOM to have one generated for you.' if mode == 'e' else '')
    while True:
        userKey = input('> ').upper()
        if (len(set(userKey)) == 26 and all([char.isalpha() for char in userKey])):
            print(
                f'The key is {userKey}. KEEP THIS SECRET!\n' if mode == 'e' else '', end='')
            break
        if userKey == 'random' and mode == 'e':
            userKey = ALPHABET.copy()
            random.shuffle(userKey)
            print(f"The key is {''.join(userKey)}. KEEP THIS SECRET!")
            break
        print('Invalid input. The key must contain 26 distinct alphabets.')

    if mode == 'e':
        print('Enter the message to encrypt.')
        userMessage = input('> ')
        encryptedMessage = sub_chiper_encrypt(userMessage, userKey)
        print('The encrypted message is:')
        print(encryptedMessage)
        print('Full encrypted text copied to clipboard.')
        pyperclip.copy(encryptedMessage)
    elif mode == 'd':
        print('Enter the message to decrypt.')
        userMessage = input('> ')
        decryptedMessage = sub_chipher_decrypt(userMessage, userKey)
        print('The decrypted message is:')
        print(decryptedMessage)
        print('Full decrypted text copied to clipboard.')
        pyperclip.copy(decryptedMessage)
