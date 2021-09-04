import itertools
import random
import time
import os

POSITION = ['LEFT', 'MIDDLE', 'RIGHT']

valueList = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suitList = [chr(9829), chr(9830), chr(9824), chr(9827)]
cardList = list(itertools.product(valueList, suitList))


def print_card(cards):
    printCard = []
    for value, suit in cards:
        printCard.append([' ___ ', '|' + value + ' '*(3-len(value)) +
                         '|', '| ' + suit + ' |', '|'+'_'*(3-len(value)) + value + '|'])

    for line in list(zip(*printCard)):
        print('  '.join(line))
    print('')


if __name__ == "__main__":
    print('Three\-Card Monte\n')
    print('Find the red lady (the Queen of Hearts)! Keep an eye on how the cards move.\n')

    cards = [cardList.pop(cardList.index(('Q', chr(9829))))]
    cards.extend(random.choices(cardList, k=2))
    random.shuffle(cards)

    print('Here are the cards:')
    print_card(cards)

    input('Press Enter when you are ready to begin')
    for _ in range(random.randint(10, 35)):
        swapIdx = random.randint(1, 3)
        if swapIdx == 1:
            cards[0], cards[1] = cards[1], cards[0]
            print('swapping left and middle...' if random.random()
                  <= 0.5 else 'swapping middle and left...')
        elif swapIdx == 2:
            cards[0], cards[2] = cards[2], cards[0]
            print('swapping left and right...' if random.random()
                  <= 0.5 else 'swapping right and left...')
        elif swapIdx == 3:
            cards[1], cards[2] = cards[2], cards[1]
            print('swapping middle and right...' if random.random()
                  <= 0.5 else 'swapping right and middle...')
        time.sleep(1)

    os.system('cls' if os.name == 'nt' else 'clear')
    print('Which card has the Queen of Hearts? (LEFT MIDDLE RIGHT)')
    while True:
        userAnswer = input('> ').upper()
        if userAnswer in POSITION:
            userAnswer = POSITION.index(userAnswer)
            break
        print('Invalid input.')

    if cards[userAnswer] == ('Q', chr(9829)):
        possibleNewIdx = [0, 1, 2]
        possibleNewIdx.remove(userAnswer)
        idx = random.choice(possibleNewIdx)
        cards[userAnswer], cards[idx] = cards[idx], cards[userAnswer]

    print_card(cards)
    print('You win!' if cards[userAnswer] == ('Q', chr(9829)) else 'You lost!')
    print('Thanks for playing, sucker!')
