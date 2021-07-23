import random
import os


def main():
    print('Carrot in a Box')
    player1 = input('Human player 1, enter your name: ')
    player2 = input('Human player 2, enter your name: ')
    print('HERE ARE TWO BOXES:')
    print_boxes([print_box('RED'), print_box('GOLD')], player1, player2)

    print(f'\n{player1}, you have a RED box in front of you.')
    print(f'{player2}, you have a GOLD box in front of you.')
    input('Press Enter to continue...')
    input(f'When {player2} has closed their eyes, press Enter...')
    print(f'{player1} here is the inside of your box:')

    player1Carrot = random.choice([True, False])
    player2Carrot = not player1Carrot
    print_boxes([print_box_open('RED', player1Carrot), print_box('GOLD')],
                player1, player2, player1Carrot)

    input('Press Enter to continue...')
    os.system('cls' if os.name == 'nt' else 'clear')

    input(f'When {player2} has opened their eyes, press Enter...')
    print('HERE ARE TWO BOXES:')
    print_boxes([print_box('RED'), print_box('GOLD')], player1, player2)

    print(f'{player2}, do you want to switch your box with {player1}\'s box? (Y/N)')
    while True:
        change = input('> ').lower()
        if change in ['y', 'n']:
            break
        print('Invalid input. Please input (Y)es or (N)o')

    if change == 'y':
        print('Box are changed')
        player1, player2 = player2, player1
    input('Press Enter to open the boxes...')
    print_boxes([print_box_open('RED', player1Carrot), print_box_open(
        'GOLD', player2Carrot)], player1, player2, player1Carrot, player2Carrot)

    print(player1 if player1Carrot else player2 + ' won the game!')


def print_box(color):
    return [' '*2 + '_'*10, ' '*1 + '/' + ' '*9 + '/|', '+' + '-'*9 + '+ |', '|' + ' '*3 + color + ' '*(6-len(color)) + '| |', '|' + ' '*3 + 'BOX' + ' '*3 + '| /', '+' + '-'*9 + '+/']


def print_box_open(color, carrot):
    return [' '*3 + '_'*3 + 'VV' + '_'*4, '  |' + ' '*3 + 'VV' + ' '*4 + '|', '  |' + ' '*3 + 'VV' + ' '*4 + '|', '  |' + '_'*3 + '||' + '_'*4 + '|', ' /' + ' '*4 + '||' + ' '*3 + '/|', '+' + '-'*9 + '+ |', '|' + ' '*3 + color + ' ' * (6-len(color)) + '| |', '|' + ' '*3 + 'BOX' + ' '*3 + '| /', '+' + '-'*9 + '+/'] if carrot else [' '*3 + '_'*9, '  |' + ' '*9 + '|', '  |' + ' '*9 + '|', '  |' + '_'*9 + '|', ' /' + ' '*9 + '/|', '+' + '-'*9 + '+ |', '|' + ' '*3 + color + ' ' * (6-len(color)) + '| |', '|' + ' '*3 + 'BOX' + ' '*3 + '| /', '+' + '-'*9 + '+/']


def print_boxes(box, name1, name2, carrot1=False, carrot2=False):
    if len(box[0]) > len(box[1]):
        box[1] = ['', '', ''] + box[1]

    box = list(zip(*box))
    for idx, line in enumerate(box):
        print('   '.join(line) if idx in [0, len(box)-1] else '  '.join(line))

    if carrot1:
        print(' (carrot!)')
    elif carrot2:
        print(' '*16 + ' (carrot!)')

    print(' '*3 + name1 + ' '*(9-len(name1)) + ' ' * 7 + name2)


if __name__ == '__main__':
    main()
