import sys


def main():
    print('Prime Numbers')
    print('Prime numbers are numbers that are only evenly divisible by one and themselves.')
    print('They are used in a variety of practical applications, but cannot be predicted.')
    print('They must be calculated one at a time.')
    print()
    print('Enter a number to start searching for primes from:')
    print('(Try 0 or 1000000000000 (12 zeros) or another number.)')
    while True:
        startNum = input('> ')
        if startNum.isdigit() and eval(f'-1<{startNum}'):
            startNum = int(startNum)
            break
        print('Invalid input.')

    input('Press Ctrl-C at any time to quit. Press Enter to begin...')
    prime_numbers(startNum)


def prime_numbers(num):
    while True:
        isPrime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                isPrime = False
                break

        if isPrime:
            print(num, end=', ', flush=True)

        num += 1


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
