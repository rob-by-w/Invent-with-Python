import random
import sys

print('Powerball Lottery')
print('''
Each powerball lottery ticket costs $2. The jackpot for this game is $1.586 billion! 
It doesn't matter what the jackpot is, though, because the odds are 1 in 292,201,338,
so you won't win.

This simulation gives you the thrill of playing without wasting money.
''')

print('Enter 5 different numbers from 1 to 69, with spaces between each number.')
print('(For example: 5 17 23 42 50 51)')
while True:
    userPick = input('> ')
    try:
        selectedNum = list(map(int, userPick.split()))
    except ValueError:
        print('Invalid input. Please enter 5 different numbers from 1 to 69')
        continue

    if len(selectedNum) == 5 and len(set(selectedNum)) == len(selectedNum) and all([1 <= num <= 69 for num in selectedNum]):
        break

    print('Invalid input. Please enter 5 different numbers from 1 to 69')

print('Enter the powerball number from 1 to 26.')
while True:
    powerball = input('> ')
    if powerball.isdigit() and eval(f'1<={powerball}<=26'):
        powerball = int(powerball)
        break
    print('Invalid input. Please enter a powerball numbers from 1 to 26')

print('How mant times do you want to play? (Max: 1,000,000)')
while True:
    numOfDraws = input('> ')
    if numOfDraws.isdigit() and eval(f'1<={numOfDraws}<=1000000'):
        numOfDraws = int(numOfDraws)
        break
    print('Invalid input. Please enter a numbers from 1 to 1,000,000')

print(
    f'It costs ${2*numOfDraws} to play {numOfDraws} times, but don\'t worry.')
print("I'm sure you'll win it all back.")
input('Press Enter to start...')
for _ in range(numOfDraws):
    drawnLotteryNumbers = random.choices(list(range(1, 70)), k=5)
    drawnPowerball = random.randint(1, 26)

    winningNumbers = ' '.join(
        map(str, drawnLotteryNumbers)) + ' and ' + str(drawnPowerball)
    print('The winning numbers are: ' + winningNumbers.ljust(21), end='  ')
    if set(selectedNum) == set(drawnLotteryNumbers) and powerball == drawnPowerball:
        print('You win!')
        print('Congratulations! You won $1.586 billion dollars!')
        sys.exit()
    else:
        print('You lost.')

print(f'You have wasted ${2*numOfDraws}')
print('Thanks for playing')
