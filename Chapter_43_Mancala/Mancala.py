import sys

PLAYER1_PITS = ('A', 'B', 'C', 'D', 'E', 'F', '1')
PLAYER2_PITS = ('L', 'K', 'J', 'I', 'H', 'G', '2')
PITS_ORDER = PLAYER1_PITS + PLAYER2_PITS
STARTING_SEEDS = 4


def print_board(pits):
    seedAmounts = [str(pits[pit]).rjust(2) for pit in 'GHIJKL21ABCDEF']
    print('''
+------+------+--<<<<<-Player 2----+------+------+------+
2      |G     |H     |I     |J     |K     |L     |      1
       |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |
S      |      |      |      |      |      |      |      S
T  {}  +------+------+------+------+------+------+  {}  T
O      |A     |B     |C     |D     |E     |F     |      O
R      |  {}  |  {}  |  {}  |  {}  |  {}  |  {}  |      R
E      |      |      |      |      |      |      |      E
+------+------+------+-Player 1->>>>>-----+------+------+
'''.format(*seedAmounts))


def check_win(pits, availablePits):
    if all([pits[pit] == 0 for pit in availablePits[:-1]]):
        print(f"Player {availablePits[-1]}'s pits are empty. Game has ended.")
        for pit in PLAYER2_PITS[:-1]:
            pits[PLAYER2_PITS[-1]] += pits[pit]
        for pit in PLAYER1_PITS[:-1]:
            pits[PLAYER1_PITS[-1]] += pits[pit]

        print(f"Score: Player 1={pits['1']}      Player 2={pits['2']}")
        if pits['1'] > pits['2']:
            print('Player 1 wins the game!')
        elif pits['1'] < pits['2']:
            print('Player 2 wins the game!')
        else:
            print('It is a draw!')
        sys.exit()


if __name__ == "__main__":
    pits = {}
    for pit in PLAYER1_PITS + PLAYER2_PITS:
        pits[pit] = STARTING_SEEDS if pit not in ['1', '2'] else 0
    print_board(pits)

    turn = 0
    while True:
        if turn % 2 == 0:
            availablePits = PLAYER1_PITS
            print(
                f'Player 1, choose move: {PLAYER1_PITS[0]}-{PLAYER1_PITS[-2]} (or QUIT)')
        else:
            availablePits = PLAYER2_PITS
            print(
                f'Player 2, choose move: {PLAYER2_PITS[-2]}-{PLAYER2_PITS[0]} (or QUIT)')

        while True:
            playerMove = input('> ').upper()
            if playerMove in availablePits[:-1] and pits.get(playerMove, False):
                break
            if playerMove == 'QUIT':
                sys.exit()
            print('Invalid input.')

        seedOnHands = pits[playerMove]
        pits[playerMove] = 0
        currentPit = playerMove
        while seedOnHands > 0:
            nextPit = PITS_ORDER[(PITS_ORDER.index(
                currentPit) + 1) % len(PITS_ORDER)]
            if (turn % 2 == 0 and nextPit == '2') or (turn % 2 == 1 and nextPit == '1'):
                currentPit = nextPit
                continue

            pits[nextPit] += 1
            seedOnHands -= 1
            currentPit = nextPit

        if pits[currentPit] == 1 and currentPit in availablePits[:-1]:
            oppositeIdx = 5 - availablePits.index(currentPit)
            oppositePits = PLAYER1_PITS[oppositeIdx] if turn % 2 else PLAYER2_PITS[oppositeIdx]
            pits[currentPit] += pits[oppositePits]
            pits[oppositePits] = 0

        print_board(pits)
        check_win(pits, availablePits)
        turn += 1 if currentPit != availablePits[-1] else 0
