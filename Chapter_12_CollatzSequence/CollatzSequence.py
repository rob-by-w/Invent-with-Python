def main():
    print('Collatz Sequence or the 3n + 1 Problem')
    print('The Collatz sequence is a sequence of numbers produced from a starting number n, following three rules:')
    print('   1. If n is even, the next number n is n/2.')
    print('   2. If n is odd, the next number n is n*3 + 1.')
    print('   3. If n is 1, stop. Otherwise, repeat.')
    print()
    print('Enter a starting number (greater than 0) or QUIT:')
    while True:
        numStart = input('> ')
        if (numStart.isdigit() and eval(numStart + '>0')) or numStart.lower() == 'quit':
            break
        print('Invalid input.')

    if numStart.isdigit():
        print(', '.join(collatz_generator(int(numStart))))


def collatz_generator(n):
    output = [n]
    while n != 1:
        n = 3*n + 1 if n % 2 else n//2
        output.append(n)
    return map(str, output)


if __name__ == '__main__':
    main()
