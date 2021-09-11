import sys

GOAL = 4
EMPTY = ' ' * 6
WATER = chr(9617) * 6


def display_buckets(bucket):
    waterDisplay = [EMPTY if bucket['8'] < i else WATER for i in range(
        1, 9)] + [EMPTY if bucket['5'] < i else WATER for i in range(1, 6)] + [EMPTY if bucket['3'] < i else WATER for i in range(1, 4)]

    print(f'Try to get {GOAL}L of water into one of these buckets:')
    print('''
8|{7}|
7|{6}|
6|{5}|
5|{4}|  5|{12}|
4|{3}|  4|{11}|
3|{2}|  3|{10}|  3|{15}|
2|{1}|  2|{9}|  2|{14}|
1|{0}|  1|{8}|  1|{13}|
 +------+   +------+   +------+
    8L         5L         3L
'''.format(*waterDisplay))


def ask_player_move():
    print('You can:')
    print('  (F)ill the bucket')
    print('  (E)mpty the bucket')
    print('  (P)our one bucket into another')
    print('  (Q)uit')

    while True:
        move = input('> ').upper()
        if move in ['QUIT', 'Q']:
            print('Thanks of playing!')
            sys.exit()
        if move in ('F', 'E', 'P'):
            break
        print('Invalid input. Please enter F, E, P, or Q')

    while True:
        print('Select a bucket 8, 5, 3, or QUIT:')
        sourceBucket = input('> '). upper()
        if sourceBucket in ['QUIT', 'Q']:
            print('Thanks of playing!')
            sys.exit()
        if sourceBucket in ('8', '5', '3'):
            break

    return (move, sourceBucket)


def make_move(buckets, move, sourceBucket):
    if move == 'F':
        buckets[sourceBucket] = int(sourceBucket)
    elif move == 'E':
        buckets[sourceBucket] = 0
    elif move == 'P':
        while True:
            print('Select a bucket to pour into: 8, 5, or 3')
            destinationBucket = input('> ').upper()
            if destinationBucket in ('8', '5', '3'):
                break

        dstBucketSize = int(destinationBucket)
        emptySpaceInDstBucket = dstBucketSize - buckets[destinationBucket]
        waterInSrcBucket = buckets[sourceBucket]
        amountToPour = min(emptySpaceInDstBucket, waterInSrcBucket)

        buckets[destinationBucket] += amountToPour
        buckets[sourceBucket] -= amountToPour

    return buckets


if __name__ == "__main__":
    print('Water Bucket Puzzle')
    print()

    bucketDict = {'8': 0, '5': 0, '3': 0}
    steps = 0

    while True:
        display_buckets(bucketDict)
        print(f'Steps: {steps}')
        if GOAL in bucketDict.values():
            print(f'Good job! You solved it in {steps} steps!')
            break

        userMove, sourceBucket = ask_player_move()
        bucketList = make_move(bucketDict, userMove, sourceBucket)
        steps += 1
