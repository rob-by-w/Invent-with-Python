import os
import random
import playsound
import time

print('Sound Mimic')
print("""Try to memorize a pattern of A S D F letters (each with its own sound)
as it gets longer and longer.""")
input('Press Enter to begin...')

soundPattern = ''

while True:
    os.system('cls' if os.name == 'nt' else 'clear')
    soundPattern += random.choice(list('ASDF'))
    for pattern in soundPattern:
        print(pattern, end=' ', flush=True)
        playsound.playsound(f'sound{pattern}.wav')

    time.sleep(1)
    os.system('cls' if os.name == 'nt' else 'clear')
    print('Enter the pattern:')

    while True:
        userResponse = input('> ').replace(' ', '').upper()
        if set(userResponse).issubset(set(list('ASDF'))):
            break
        print('Invalid input')

    print('Correct!' if userResponse ==
          soundPattern else f'Incorrect! The pattern was {soundPattern}')
    for pattern in soundPattern:
        playsound.playsound(f'sound{pattern}.wav')

    if userResponse != soundPattern:
        print(f'You scored {len(soundPattern)-1} points.')
        print('Thanks for playing')
        break

    time.sleep(1)
