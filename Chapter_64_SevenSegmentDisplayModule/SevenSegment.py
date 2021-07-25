def getSevSegStr(number, digits):
    digitsDrawing = {
        0: [' __ ', '|  |', '|__|'],
        1: ['    ', '   |', '   |'],
        2: [' __ ', ' __|', '|__ '],
        3: [' __ ', ' __|', ' __|'],
        4: ['    ', '|__|', '   |'],
        5: [' __ ', '|__ ', ' __|'],
        6: [' __ ', '|__ ', '|__|'],
        7: [' __ ', '   |', '   |'],
        8: [' __ ', '|__|', '|__|'],
        9: [' __ ', '|__|', ' __|']
    }

    output = []
    number = str(number)
    for _ in range(digits-len(number)):
        output.append(digitsDrawing[0])

    for digit in number:
        output.append(digitsDrawing[int(digit)])

    return list(zip(*output))


if __name__ == '__main__':
    getSevSegStr(42, 3)
