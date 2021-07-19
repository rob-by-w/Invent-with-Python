import datetime
import random


def main():
    print('Birthday Paradox\nHow many birthdays shall I generate? (Max 100)')

    numOfBirthday = input_birthday()
    birthdayList = [random_date() for _ in range(numOfBirthday)]
    print(f'Here are {numOfBirthday} birthdays:')
    print(', '.join([datetime.datetime.strftime(birthday, '%b %d')
                     for birthday in birthdayList]))

    for birthday in birthdayList:
        if birthdayList.count(birthday) > 1:
            print(
                f"In this simulation, multiple people have a birthday on {datetime.datetime.strftime(birthday, '%b %d')}")
            break

        if birthday == birthdayList[-1]:
            print('In this simulation, there are no people with a same birthday')

    print(f'Generating {numOfBirthday} random birthdays 100,000 times...')
    input('Press Enter to begin...')
    print("Let's run another 100,000 simulations.")

    countSameBirthdayGroup = run_simulation(numOfBirthday)

    print(
        f'Out of 100,000 simulations of {numOfBirthday} people, there was a matching birthday in that group {countSameBirthdayGroup} times.')
    print('This means that %i people have a %.2f %% chance of having a matching birthday in their group.' %
          (numOfBirthday, countSameBirthdayGroup/(10**3)))
    print("That's propbably more thatn you would think!")


def input_birthday():
    while True:
        try:
            numOfBirthday = int(input('> '))

            if numOfBirthday > 100 or numOfBirthday < 1:
                print(
                    'Invalid input. Please enter a number bigger than 0 and less than 100')
            else:
                break

        except ValueError:
            print('Invalid input. Please enter a number')

    return numOfBirthday


def random_date():
    startDate = datetime.date(2020, 1, 1)
    endDate = datetime.date(2021, 1, 1)

    rangeDate = endDate - startDate
    rangeDay = rangeDate.days
    randomNumOfDays = random.randrange(rangeDay)
    return startDate + datetime.timedelta(days=randomNumOfDays)


def run_simulation(numOfBirthday):
    count = 0
    checkpoint = [num * 10**4 for num in range(11)]

    for n in range(10**5+1):
        birthdayList = [random_date() for _ in range(numOfBirthday)]
        for birthday in birthdayList:
            if birthdayList.count(birthday) > 1:
                count += 1
                break

        if n == checkpoint[-1]:
            print(f'{n} simulations run.')
        elif n in checkpoint:
            print(f'{n} simulations run...')

    return count


if __name__ == '__main__':
    main()
