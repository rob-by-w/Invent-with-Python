import shutil
import time
import random
import sys

PAUSE_TIME = 0.2
DENSITY = 0.1

DUCKLING_WIDTH = 5
LEFT = 'left'
RIGHT = 'right'
BEADY = 'beady'
WIDE = 'wide'
HAPPY = 'happy'
ALOOF = 'aloof'
CHUBBY = 'chubby'
VERY_CHUBBY = 'very chubby'
OPEN = 'open'
CLOSED = 'closed'
OUT = 'out'
DOWN = 'down'
UP = 'up'
HEAD = 'head'
BODY = 'body'
FEET = 'feet'

WIDTH = shutil.get_terminal_size()[0] - 1


class Duckling:
    def __init__(self) -> None:
        self.direction = random.choice([LEFT, RIGHT])
        self.body = random.choice([CHUBBY, VERY_CHUBBY])
        self.mouth = random.choice([OPEN, CLOSED])
        self.wing = random.choice([OUT, UP, DOWN])
        self.eyes = BEADY if self.body == CHUBBY else random.choice(
            [BEADY, WIDE, HAPPY, ALOOF])
        self.nextPart = HEAD

    def getEye(self):

        if self.eyes == BEADY:
            return '"' if self.body == CHUBBY else '" '
        elif self.eyes == WIDE:
            return "''"
        elif self.eyes == HAPPY:
            return '^^'
        elif self.eyes == ALOOF:
            return '``'

    def getWing(self):
        if self.wing == OUT:
            return '>'
        elif self.wing == UP:
            return '^'
        elif self.wing == DOWN:
            return 'v'

    def getHead(self):
        headStr = ''
        if self.direction == LEFT:
            headStr += '>' if self.mouth == OPEN else '='
            headStr += self.getEye()
            headStr += ') '
        elif self.direction == RIGHT:
            headStr += ' ('
            headStr += self.getEye()
            headStr += '<' if self.mouth == OPEN else '='

        headStr += ' ' if self.body == CHUBBY else ''

        return headStr

    def getBody(self):
        bodyStr = '('
        if self.direction == LEFT:
            bodyStr += ' ' if self.body == CHUBBY else '  '
            bodyStr += self.getWing()
        elif self.direction == RIGHT:
            bodyStr += self.getWing()
            bodyStr += ' ' if self.body == CHUBBY else '  '

        bodyStr += ') ' if self.body == CHUBBY else ')'

        return bodyStr

    def getFeet(self):
        return ' ^^  ' if self.body == CHUBBY else ' ^ ^ '

    def getNextPart(self):
        if self.nextPart == HEAD:
            self.nextPart = BODY
            return self.getHead()
        elif self.nextPart == BODY:
            self.nextPart = FEET
            return self.getBody()
        elif self.nextPart == FEET:
            self.nextPart = None
            return self.getFeet()


def main():
    try:
        print('Duckling Screensaver')
        print('Press Ctrl-C to quit...')
        time.sleep(2)

        ducklingLanes = [None] * (WIDTH // DUCKLING_WIDTH)
        while True:
            for laneNum, ducklingObj in enumerate(ducklingLanes):
                if ducklingObj == None and random.random() <= DENSITY:
                    ducklingObj = Duckling()
                    ducklingLanes[laneNum] = ducklingObj

                if ducklingObj != None:
                    print(ducklingObj.getNextPart(), end='')
                    if ducklingObj.nextPart == None:
                        ducklingLanes[laneNum] = None
                else:
                    print(' ' * DUCKLING_WIDTH, end='')

            print()
            sys.stdout.flush()
            time.sleep(PAUSE_TIME)
    except KeyboardInterrupt:
        sys.exit()


if __name__ == "__main__":
    main()
