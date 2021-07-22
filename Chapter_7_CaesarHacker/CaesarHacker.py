def main():
    print('Caesar Cipher Hacker')
    print('Enter the encrypted Casesar ciper message to hack')
    inputMessage = input('> ')

    for key in range(0, 26):
        decryptedMessage = decrypt_message(inputMessage, key)
        if key < 10:
            print(f'Key #{key}:  {decryptedMessage}')
        else:
            print(f'Key #{key}: {decryptedMessage}')


def decrypt_message(message, key):
    decryptedMessage = ''
    for char in message:
        if char.isalpha():
            if char.islower():
                decryptedMessage += chr((ord(char) -
                                        ord('a') - key) % 26 + ord('a'))
            else:
                decryptedMessage += chr((ord(char) -
                                        ord('A') - key) % 26 + ord('A'))
        else:
            decryptedMessage += char

    return decryptedMessage


if __name__ == '__main__':
    main()
