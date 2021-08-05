import random
import pyperclip

CHANGE_PERCENTAGE = 0.7
CHAR_MAP = {'a': ['4', '@', '/-\\'], 'c': ['('], 'd': ['|)'], 'e': ['3'], 'f': ['ph'], 'h': [']-[', '|-|'], 'i': [
    '1', '!', '|'], 'k': [']<'], 'o': ['0'], 's': ['$', '5'], 't': ['7', '+'], 'u': ['|_|'], 'v': ['\\/']}

if __name__ == "__main__":
    print('L3375P34]< (leetspeek)')
    print()
    print('Enter your leet message:')
    message = input('> ').lower()

    leetMessage = ''.join([random.choice(CHAR_MAP[char]) if char in CHAR_MAP.keys(
    ) and random.random() < CHANGE_PERCENTAGE else char for char in message])

    pyperclip.copy(leetMessage)
    print(leetMessage)
    print('(Copied leetspeak to clipboard.')
