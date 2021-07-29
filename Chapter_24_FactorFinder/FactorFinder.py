def factor_finder(num):
    output = []
    for i in range(1, int(num ** 0.5) + 1):
        if userInput % i == 0 and i not in output:
            output.append(i)
            output.append(userInput // i)

    return sorted(list(set(output)))


if __name__ == "__main__":
    print('Factor Finder')
    while True:
        print('Enter a number to factor (or "QUIT" to quit):')

        userInput = input('> ').upper()
        if userInput == 'QUIT':
            break

        if userInput.isdigit() and eval(userInput + '>0'):
            userInput = int(userInput)
        else:
            print('Invalid input. Please enter a number larger than 0.')
            continue

        output = factor_finder(userInput)
        print(', '.join(map(str, output)))
