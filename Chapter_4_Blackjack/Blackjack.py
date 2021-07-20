import random
import itertools


def print_card(cards):
    printCard = []
    for value, suit in cards:
        if value == 'blank':
            printCard.append([' ___ ', '|## |', '|###|', '|_##|'])
        else:
            printCard.append([' ___ ', '|' + value + ' '*(3-len(value)) + '|',
                              '| ' + suit + ' |', '|'+'_'*(3-len(value)) + value + '|'])

    for line in list(zip(*printCard)):
        print('  '.join(line))
    print('')


def count_card(cards):
    total = 0
    ace = 0
    for value, _ in cards:
        if value == 'A':
            ace += 1
        elif value in valueList[-3:]:
            total += 10
        else:
            total += int(value)

    for _ in range(ace):
        total += 1 if total + 11 > 21 else 11

    return total


print('Blackjack')
print('''Rules:
      Try to get as close to 21 without going over.
      Kings, Queens, and Jacks are worth 10 points.
      Aces are worth 1 or 11 points.
      Cards 2 through 10 are worth their face value.
      (H)it to take another card.
      (S)tand to stop taking cards.
      On your first play, you can (D)ouble down to increase your bet
      but must hit exactly one more time before standing.
      In case of a tie, the bet is returned to the player.
      The dealer stops hitting at 17.
      ''')

money = 5000

print(f'Money: {money}')
print(f'How much do you bet? (1-{money}, or QUIT)')
inputBet = input('> ')
if inputBet.isdigit():
    inputBet = int(inputBet)
    print(f'Bet: {inputBet}')
elif inputBet.lower() == 'quit':
    print(f'You quit the game. Your money is {money}')

valueList = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suitList = [chr(9829), chr(9830), chr(9824), chr(9827)]
cardList = list(itertools.product(valueList, suitList))

playerCard = random.sample(cardList, 2)
playerCount = count_card(playerCard)

dealerCard = [('blank', '')]
dealerCard.extend(random.sample(cardList, 1))

print('\nDEALER: ???')
print_card(dealerCard)

print(f'PLAYER: {playerCount}')
print_card(playerCard)

while True:
    if inputBet * 2 <= money:
        print('(H)it, (S)tand, (D)ouble down')
    else:
        print('(H)it, (S)tand')

    while True:
        nextMove = input('> ').lower()

        if nextMove in ['h', 's']:
            break
        elif nextMove == 'd':
            if inputBet * 2 <= money:
                break

            print(
                f'Your money is {money} and your bet is {inputBet}. You do not have enough money left to double down.')

        if inputBet * 2 <= money:
            print('Invalid input. Please input H/S/D.')
        else:
            print('Invalid input. Please input H/S.')

    if nextMove == 'h':
        while True:
            drawCard = random.sample(cardList, 1)
            if drawCard not in playerCard + dealerCard:
                playerCard.extend(drawCard)
                break
    elif nextMove == 's':
        break
    elif nextMove == 'd':
        inputBet *= 2
        print(f'You increase your bet to {inputBet}')
        while True:
            drawCard = random.sample(cardList, 1)
            if drawCard not in playerCard + dealerCard:
                playerCard.extend(drawCard)
                break

    playerCount = count_card(playerCard)
    print(f'PLAYER: {playerCount}')
    print_card(playerCard)

    if playerCount > 21:
        print(f'Your cards is over 21. You lose ${inputBet}')
        break

if playerCount <= 21:
    while True:
        drawCard = random.sample(cardList, 1)
        if drawCard not in playerCard + dealerCard:
            dealerCard[0] = drawCard[0]
            break

    dealerCount = count_card(dealerCard)
    print(f'DEALER: {dealerCount}')
    print_card(dealerCard)

    while dealerCount <= 17:
        while True:
            drawCard = random.sample(cardList, 1)
            if drawCard not in playerCard + dealerCard:
                dealerCard.extend(drawCard)
                break

        print(dealerCard)
        dealerCount = count_card(dealerCard)
        print(f'DEALER: {dealerCount}')
        print_card(dealerCard)

    if playerCount > dealerCount:
        print(f'You won ${inputBet}!')
        money += inputBet
    elif playerCount < dealerCount:
        print(f'You lose ${inputBet}!')
        money -= inputBet
    else:
        print('Tie. Your bet is returned.')
