import time
import random

print('Fast Draw')
print('''Time to test your reflexes and see if you are the fastest draw in the west!
When you see "DRAW", you have 0.3 seconds to press Enter.
But you lose if you press Enter before "DRAW" appears.
''')
print()

while True:
    input('Press Enter to begin...')
    print('\nIt is high noon...')
    time.sleep(random.randint(20, 50) / 10)
    print('DRAW')
    startTime = time.time()
    input()
    endTime = time.time()

    responseTime = endTime - startTime
    if responseTime < 0.01:
        print('You drew before "DRAW" appeared! You lose.')
    elif responseTime > 0.3:
        responseTime = round(responseTime, 4)
        print(f'You took {responseTime} seconds to draw. Too slow!')
    else:
        responseTime = round(responseTime, 4)
        print(f'You took {responseTime} seconds to draw.')
        print('You are the fatest draw in the west! You win!')

    print('Enter QUIT to stop, or press Enter to play again.')
    userInput = input('> ').upper()
    if userInput == 'QUIT':
        print('Thanks for playing')
        break
