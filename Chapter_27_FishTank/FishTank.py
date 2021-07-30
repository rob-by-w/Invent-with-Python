import bext
import random
import sys
import time

WIDTH, HEIGHT = bext.size()
WIDTH -= 1

NUM_KELP = 2
NUM_FISH = 10
NUM_BUBBLERS = 1
FRAMES_PER_SECOND = 6

FISH_TYPES = [
    {'right': ['><>'],          'left': ['<><']},
    {'right': ['>||>'],         'left': ['<||<']},
    {'right': ['>))>'],         'left': ['<[[<']},
    {'right': ['>||o', '>||.'], 'left': ['o||<', '.||<']},
    {'right': ['>))o', '>)).'], 'left': ['o[[<', '.[[<']},
    {'right': ['>-==>'],        'left': ['<==-<']},
    {'right': [r'>\\>'],        'left': ['<//<']},
    {'right': ['><)))*>'],      'left': ['<*(((><']},
    {'right': ['}-[[[*>'],      'left': ['<*]]]-{']},
    {'right': [']-<)))b>'],     'left': ['<d(((>-[']},
    {'right': ['><XXX*>'],      'left': ['<*XXX><']},
    {'right': ['_.-._.-^=>', '.-._.-.^=>', '-._.-._^=>', '._.-._.^=>'],
     'left':  ['<=^-._.-._', '<=^.-._.-.', '<=^_.-._.-', '<=^._.-._.']},
]
LONGEST_FISH_LENGTH = 10

LEFT_EDGE = 0
RIGHT_EDGE = WIDTH - 1 - LONGEST_FISH_LENGTH
TOP_EDGE = 0
BOTTOM_EDGE = HEIGHT - 2


def main():
    global FISHES, BUBBLERS, BUBBLES, KELPS, STEP
    bext.bg('black')
    bext.clear()

    FISHES = [generate_fish() for _ in range(NUM_FISH)]
    BUBBLERS = [random.randint(LEFT_EDGE, RIGHT_EDGE)
                for _ in range(NUM_BUBBLERS)]
    BUBBLES = []
    KELPS = [generate_kelp() for _ in range(NUM_KELP)]

    STEP = 1
    while True:
        simulate_aquarium()
        draw_aquarium()
        time.sleep(1 / FRAMES_PER_SECOND)
        clear_aquarium()


def get_random_color():
    return random.choice(('black', 'red', 'green', 'yellow', 'blue', 'purple', 'cyan', 'white'))


def generate_fish():
    fishType = random.choice(FISH_TYPES)
    colorPattern = random.choice(('random', 'head-tail', 'single'))
    fishLength = len(fishType['right'][0])

    # All parts are randomly colored
    if colorPattern == 'random':
        colors = [get_random_color() for _ in range(fishLength)]

    # All same color
    if colorPattern == 'single' or colorPattern == 'head-tail':
        colors = [get_random_color()] * fishLength

        # Head/tail different from body
        if colorPattern == 'head-tail':
            headTailColor = get_random_color()
            colors[0] = headTailColor
            colors[-1] = headTailColor

    return {'right': fishType['right'],
            'left': fishType['left'],
            'colors': colors,
            'hSpeed': random.randint(1, 6),
            'vSpeed': random.randint(5, 15),
            'timeToHDirChange': random.randint(10, 60),
            'timeToVDirChange': random.randint(2, 20),
            'goingRight': random.choice([True, False]),
            'goingDown': random.choice([True, False]),
            'x': random.randint(0, RIGHT_EDGE),
            'y': random.randint(0, BOTTOM_EDGE)}


def generate_kelp():
    return {'x': random.randint(LEFT_EDGE, RIGHT_EDGE),
            'segments': [random.choice(['(', ')']) for _ in range(random.randint(6, HEIGHT-1))]}


def simulate_aquarium():
    global FISHES, BUBBLERS, BUBBLES, KELPS, STEP

    for fish in FISHES:
        if STEP % fish['hSpeed'] == 0:
            if fish['goingRight']:
                if fish['x'] != RIGHT_EDGE:
                    fish['x'] += 1
                else:
                    fish['goingRight'] = False
                    fish['colors'].reverse()
            else:
                if fish['x'] != LEFT_EDGE:
                    fish['x'] -= 1
                else:
                    fish['goingRight'] = True
                    fish['colors'].reverse()

        fish['timeToHDirChange'] -= 1
        if fish['timeToHDirChange'] == 0:
            fish['timeToHDirChange'] = random.randint(10, 60)
            fish['goingRight'] = not fish['goingRight']

        if STEP % fish['vSpeed'] == 0:
            if fish['goingDown']:
                if fish['y'] != BOTTOM_EDGE:
                    fish['y'] += 1
                else:
                    fish['goingDown'] = False
            else:
                if fish['y'] != TOP_EDGE:
                    fish['y'] -= 1
                else:
                    fish['goingDown'] = True

        fish['timeToVDirChange'] -= 1
        if fish['timeToVDirChange'] == 0:
            fish['timeToVDirChange'] = random.randint(2, 20)
            fish['goingDown'] = not fish['goingDown']

    for bubbler in BUBBLERS:
        if random.randint(1, 5) == 1:
            BUBBLES.append({'x': bubbler, 'y': HEIGHT - 2})

    for bubble in BUBBLES:
        bubble['y'] -= 1
        diceRoll = random.randint(1, 6)
        if (diceRoll == 1) and (bubble['x'] != LEFT_EDGE):
            bubble['x'] -= 1
        elif (diceRoll == 2) and (bubble['x'] != RIGHT_EDGE):
            bubble['x'] += 1

    for i in range(len(BUBBLES) - 1, -1, -1):
        if BUBBLES[i]['y'] == TOP_EDGE:
            del BUBBLES[i]

    for kelp in KELPS:
        for i, kelpSegment in enumerate(kelp['segments']):
            if random.randint(1, 20) == 1:
                if kelpSegment == '(':
                    kelp['segments'][i] = ')'
                elif kelpSegment == ')':
                    kelp['segments'][i] = '('


def draw_aquarium():
    global FISHES, BUBBLERS, BUBBLES, KELPS, STEP

    bext.fg('white')
    bext.goto(0, 0)
    print('Fish Tank.\tCtrl-C to quit.', end='')

    bext.fg('white')
    for bubble in BUBBLES:
        bext.goto(bubble['x'], bubble['y'])
        print(random.choice(('o', 'O')), end='')

    for fish in FISHES:
        bext.goto(fish['x'], fish['y'])
        fishText = fish['right'][STEP % len(
            fish['right'])] if fish['goingRight'] else fish['left'][STEP % len(fish['left'])]

        for i, fishPart in enumerate(fishText):
            bext.fg(fish['colors'][i])
            print(fishPart, end='')

    bext.fg('green')
    for kelp in KELPS:
        for i, kelpSegment in enumerate(kelp['segments']):
            if kelpSegment == '(':
                bext.goto(kelp['x'], BOTTOM_EDGE - i)
            elif kelpSegment == ')':
                bext.goto(kelp['x'] + 1, BOTTOM_EDGE - i)
            print(kelpSegment, end='')

    bext.fg('yellow')
    bext.goto(0, HEIGHT - 1)
    print(chr(9617) * (WIDTH - 1), end='')

    sys.stdout.flush()


def clear_aquarium():
    global FISHES, BUBBLES, KELPS

    for bubble in BUBBLES:
        bext.goto(bubble['x'], bubble['y'])
        print(' ', end='')

    for fish in FISHES:
        bext.goto(fish['x'], fish['y'])
        print(' ' * len(fish['left'][0]), end='')

    for kelp in KELPS:
        for i, _ in enumerate(kelp['segments']):
            bext.goto(kelp['x'], HEIGHT - 2 - i)
            print('  ', end='')

    sys.stdout.flush()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
