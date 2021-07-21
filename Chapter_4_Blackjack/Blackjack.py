import random
import itertools

valueList = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
suitList = [chr(9829), chr(9830), chr(9824), chr(9827)]
cardList = list(itertools.product(valueList, suitList))


def main():
    money = 5000

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

    while money > 0:
        flagQuit = 0
        print(f'Money: {money}')
        print(f'How much do you bet? (1-{money}, or QUIT)')

        inputBet = input_bet(money)
        if eval(str(inputBet).lower() + '== quit'):
            break

        playerCard = random.sample(cardList, 2)
        playerCount = count_card(playerCard)
        dealerCard = [('blank', '')]
        dealerCard.extend(random.sample(cardList, 1))

        print('\nDEALER: ???')
        print_card(dealerCard)
        print(f'PLAYER: {playerCount}')
        print_card(playerCard)

        while True:
            nextMove = user_move(money, inputBet)

            if nextMove == 'h':
                playerCard.extend(draw_card(playerCard, dealerCard))
                print(f'You drew a {playerCard[-1][0]} of {playerCard[-1][1]}')
            elif nextMove == 's':
                break
            elif nextMove == 'd':
                inputBet *= 2
                print(f'You increase your bet to {inputBet}')
                playerCard.extend(draw_card(playerCard, dealerCard))
                print(
                    f'You drew a {playerCard[-1][0]} of {playerCard[-1][1]}.')

            print('\nDEALER: ???')
            print_card(dealerCard)

            playerCount = count_card(playerCard)
            print(f'PLAYER: {playerCount}')
            print_card(playerCard)

            if playerCount > 21:
                print(f'Your cards is over 21. You lose ${inputBet}')
                money -= inputBet
                break
            elif playerCount == 21:
                break

        if playerCount <= 21:
            dealerCard[0] = draw_card(playerCard, dealerCard)[0]
            dealerCount = count_card(dealerCard)
            print(f'Dealer revealed his card.')
            print(f'DEALER: {dealerCount}')
            print_card(dealerCard)

            print(f'PLAYER: {playerCount}')
            print_card(playerCard)

            while dealerCount < 17:
                dealerCard.extend(draw_card(playerCard, dealerCard))
                dealerCount = count_card(dealerCard)
                print(
                    f'Dealer drew a {dealerCard[-1][0]} of {dealerCard[-1][1]}.')
                print(f'DEALER: {dealerCount}')
                print_card(dealerCard)

                print(f'PLAYER: {playerCount}')
                print_card(playerCard)

                input('Press Enter to continue...')

            if playerCount > dealerCount or dealerCount > 21:
                print(f'You won ${inputBet}!')
                money += inputBet
            elif playerCount < dealerCount:
                print(f'You lose ${inputBet}!')
                money -= inputBet
            else:
                print('Tie. Your bet is returned.')

    if money == 0:
        print('Game over. You lost all your money.')


def input_bet(userMoney):
    while True:
        bet = input('> ')
        if bet.isdigit() and eval(bet + '<=' + str(userMoney)):
            bet = int(bet)
            print(f'Bet: ${bet}')
            break
        elif bet.lower() == 'quit':
            print(f'You quit the game. Your money is ${userMoney}')
            break

        print(
            f'Invalid input. Please input a bet in range of 1-{userMoney}, or QUIT')

    return bet


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


def draw_card(dealerCard, playerCard):
    while True:
        drawCard = random.sample(cardList, 1)
        if drawCard not in playerCard + dealerCard:
            break

    return drawCard


def user_move(money, bet):
    print('(H)it, (S)tand, (D)ouble down' if bet *
          2 <= money else '(H)it, (S)tand')

    while True:
        move = input('> ').lower()

        if move in ['h', 's']:
            break
        elif move == 'd':
            if bet * 2 <= money:
                break

            print(
                f'Your money is ${money} and your bet is ${bet}. You do not have enough money left to double down.')

        print('Invalid input. Please input H/S/D.' if bet * 2 <=
              money else 'Invalid input. Please input H/S.')

    return move


if __name__ == '__main__':
    main()
