def main():
    print('Diamonds')
    for idx in range(1, 6):
        print_diamonds_outline(idx)
        print()
        print_diamonds_filled(idx)
        print()


def print_diamonds_outline(size):
    size += 1

    for i in range(1, size//2 + 1):
        print(' '*(size//2 - i) + '/' + ' '*(2*i-2) + '\\')
    for i in range(size//2, 0, -1):
        print(' '*(size//2 - i) + '\\' + ' '*(2*i-2) + '/')


def print_diamonds_filled(size):
    size += 1

    for i in range(1, size//2 + 1):
        print(' '*(size//2 - i) + '/'*i + '\\'*i)
    for i in range(size//2, 0, -1):
        print(' '*(size//2 - i) + '\\'*i + '/'*i)


if __name__ == "__main__":
    main()
