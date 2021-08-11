import random
import time

print('Million Dice Roll Statistics Simulator')
print()
print('Enter how many six-sided dice you want to roll:')
while True:
    diceNum = input('> ')
    if diceNum.isdigit() and eval(f'0<{diceNum}'):
        diceNum = int(diceNum)
        break
    print('Invalid input. Please enter an integer larger than 0.')

print(f'Simulating 1,000,000 rolls of {diceNum} dice...' if diceNum !=
      1 else f'Simulating 1,000,000 rolls of {diceNum} die...')

sumList = [0] * (diceNum * 6)
lastPrintTime = time.time()
for idx in range(10**6):
    rollResult = sum([random.randint(1, 6) for _ in range(diceNum)]) - 1
    sumList[rollResult] += 1

    if time.time() > lastPrintTime + 1:
        print(f'{round(idx/(10**4), 1)}% done...')
        lastPrintTime = time.time()

print('TOTAL - ROLLS - PERCENTAGE')
for idx, value in enumerate(sumList):
    if idx < diceNum - 1:
        continue
    print(f'  {idx+1} - {value} rolls - {round(value/(10**4), 1)}%')
