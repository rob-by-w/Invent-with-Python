print('Numeral System Counters')
print()
print('This program shows you equivalent numbers in decimal (base 10), hexadecimal (base 16), and binary (base 2) numeral systems.')

print('Enter the starting number (e.g. 0)', end=' ')
while True:
    startNum = input('> ')
    if startNum.isdigit() and eval(f'0<={startNum}'):
        startNum = int(startNum)
        break
    print('Invalid input.')

print('Enter how many numbers to display (e.g. 1000)', end=' ')
while True:
    numToDisplay = input('> ')
    if numToDisplay.isdigit() and eval(f'0<{numToDisplay}'):
        numToDisplay = int(numToDisplay)
        break
    print('Invalid input.')

for num in range(startNum, numToDisplay):
    print(f'DEC: {str(num).ljust(8)}', end='')
    print(f'HEX: {hex(num)[2:].upper().ljust(8)}', end='')
    print(f'BIN: {bin(num)[2:]}')
