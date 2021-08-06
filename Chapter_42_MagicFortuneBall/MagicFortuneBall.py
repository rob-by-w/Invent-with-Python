import random
import time


REPLIES = ['LET ME THINK ON THIS...', 'AN INTERESTING QUESTION...', 'HMMM... ARE YOU SURE YOU WANT TO KNOW..?', 'DO YOU THINK SOME THINGS ARE BEST LEFT UNKNOWN..?', 'I MIGHT TELL YOU, BUT YOU MIGHT NOT LIKE THE ANSWER...',
           'YES... NO... MAYBE... I WILL THINK ON IT...', 'AND WHAT WILL YOU DO WHEN YOU KNOW THE ANSWER? WE SHALL SEE...', 'I SHALL CONSULT MY VISIONS...', 'YOU MAY WANT TO SIT DOWN FOR THIS...']
ANSWERS = ['YES, FOR SURE', 'MY ANSWER IS NO', 'ASK ME LATER', 'I AM PROGRAMMED TO SAY YES', 'THE STARS SAY YES, BUT I SAY NO', 'I DUNNO MAYBE',
           'FOCUS AND ASK ONCE MORE', 'DOUBTFUL, VERY DOUBTFUL', 'AFFIRMATIVE', 'YES, THOUGH YOU MAY NOT LIKE IT', 'NO, BUT YOU MAY WISH IT WAS SO']


def slow_print(string, pauseTime=0.1):
    for char in string.replace('I', 'i'):
        print(char, end=' ', flush=True)
        time.sleep(pauseTime)
    print()


if __name__ == "__main__":
    slow_print('MAGIC FORTUNE BALL')
    time.sleep(0.5)
    slow_print('ASK ME YOUR YES/NO QUESTION.')
    input('> ')
    time.sleep(1)
    slow_print(random.choice(REPLIES))
    slow_print('.'*random.randint(4, 12), 0.7)
    slow_print('I HAVE AN ANSWER...', 0.2)
    slow_print(random.choice(ANSWERS))
