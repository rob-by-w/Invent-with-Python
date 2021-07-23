import datetime

DAYS = ('Sunday', 'Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday', 'Saturday')
BLANK_LINE = ''.join(['|' + ' '*10 for _ in DAYS]) + '|\n'
WEEK_BREAK = ''.join(['+'+'-'*10 for _ in DAYS]) + '+\n'


def main():
    print('Calendar Maker')
    print('Enter the year for the calendar:')

    while True:
        year = input('> ')
        if year.isdigit() and eval(year + '> 0'):
            year = int(year)
            break
        print('Invalid input. Please enter a year')

    print('Enter the month for the calendar, 1-12:')
    while True:
        month = input('> ')
        if month.isdigit() and eval('1<=' + month + '<=12'):
            month = int(month)
            break
        print('Invalid input. Please enter a month')

    inputDate = datetime.date(year, month, 1)
    endDate = add_month(inputDate, 1)
    currentDate = datetime.date(year, month, 1)
    while currentDate.weekday() != 6:
        currentDate -= datetime.timedelta(1)

    output = ''
    output += (' '*33 + datetime.datetime.strftime(inputDate, '%B %Y') + '\n')
    output += '...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n'
    output += WEEK_BREAK
    while currentDate < endDate:
        for _ in DAYS:
            output += ('|' + str(currentDate.day) + ' ' *
                       (10-len(str(currentDate.day))))
            currentDate += datetime.timedelta(1)
        output += '|\n'

        for _ in range(3):
            output += BLANK_LINE
        output += WEEK_BREAK

    print(output)
    outputText = f'calendar_{year}_{month}.txt'
    with open(outputText, 'w') as f:
        f.write(output)
    print(f'Saved to {outputText}')


def add_month(sourceDate, month):
    newYear = sourceDate.year + (sourceDate.month + month) // 12
    newMonth = (sourceDate.month + month - 1) % 12 + 1

    return datetime.date(newYear, newMonth, 1)


if __name__ == '__main__':
    main()
