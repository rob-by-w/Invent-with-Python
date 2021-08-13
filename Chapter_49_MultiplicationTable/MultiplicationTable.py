print('Multiplication Table')

print('  |  0   1   2   3   4   5   6   7   8   9  10  11  12')
print('--+---------------------------------------------------')
for row in range(13):
    print(' ' * (2-len(str(row))) + str(row) + '|', end='')
    for col in range(13):
        print(' ' * (3 - len(str(row*col))) + str(row*col), end=' ')
    print()
