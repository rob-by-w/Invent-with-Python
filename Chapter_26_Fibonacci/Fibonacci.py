def fibonacci_sequence(n):
    sequenceList = []
    currentTerm, nextTerm = 0, 1
    for _ in range(n):
        sequenceList.append(currentTerm)
        currentTerm, nextTerm = nextTerm, currentTerm + nextTerm

    return sequenceList


if __name__ == "__main__":
    print('Fibonacci Sequence')
    while True:
        print('''Enter the Nth Fibonacci number you wish to calculate
(such as 5, 50, 1000, 9999), or QUIT to quit:''')

        while True:
            userInput = input('> ').upper()
            if userInput == 'QUIT':
                break
            if userInput.isdigit():
                userInput = int(userInput)
                break
            print('Invalid input. Please enter a number or QUIT to quit.')

        if userInput == 'QUIT':
            break

        output = fibonacci_sequence(userInput)
        print(', '.join(map(str, output)))
