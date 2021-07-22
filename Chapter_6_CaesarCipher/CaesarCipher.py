import pyperclip  # To copy text to clipboard


def encrypt_or_decrypt():
    print('Do you want to (e)ncrypt or (d)ecrypt?')
    while True:
        process = input('> ').lower()
        if process in ['d', 'e']:
            break

        print('Invalid input. Please enter e or d')

    return process


def input_key():
    print('Please enter the key (0 to 25) to use')
    while True:
        inputKey = input('> ')
        if inputKey in list(map(str, range(0, 26))):
            inputKey = int(inputKey)
            break

        print('Invalid input. Please enter a number 0 to 25')

    return inputKey


def encrypt_message():
    print('Enter the message to encrypt')
    message = input('> ')

    encryptedMessage = ''
    for char in message:
        if char.isalpha():
            if char.islower():
                encryptedMessage += chr((ord(char) -
                                        ord('a') + inputKey) % 26 + ord('a'))
            else:
                encryptedMessage += chr((ord(char) -
                                        ord('A') + inputKey) % 26 + ord('A'))
        else:
            encryptedMessage += char

    print(encryptedMessage)
    print('Full encrypted text copied to clipboard')
    pyperclip.copy(encryptedMessage)


def decrypt_message():
    print('Enter the message to decrypt')
    message = input('> ')

    decryptedMessage = ''
    for char in message:
        if char.isalpha():
            if char.islower():
                decryptedMessage += chr((ord(char) -
                                        ord('a') - inputKey) % 26 + ord('a'))
            else:
                decryptedMessage += chr((ord(char) -
                                        ord('A') - inputKey) % 26 + ord('A'))
        else:
            decryptedMessage += char

    print(decryptedMessage)
    print('Full decrypted text copied to clipboard')
    pyperclip.copy(decryptedMessage)


if __name__ == '__main__':
    print('Caesar Cipher')
    inputProcess = encrypt_or_decrypt()
    inputKey = input_key()

    if inputProcess == 'e':
        encrypt_message()
    else:
        decrypt_message()
