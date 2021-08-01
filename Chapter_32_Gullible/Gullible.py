if __name__ == "__main__":
    print('Gullible')
    while True:
        print('Do you want to know how to keep a gullible person busy for hours? Y/N')
        userAnswer = input('> ')

        if userAnswer.lower() in ['n', 'no']:
            break
        if userAnswer.lower() in ['y', 'yes']:
            continue
        print(f'"{userAnswer}" is not a valid yes/no response.')

    print('Thank you. Have a nice day!')
