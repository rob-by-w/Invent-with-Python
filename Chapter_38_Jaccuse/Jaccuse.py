import random
import pprint
import time
import sys

SUSPECTS = ['DUKE HAUTDOG', 'MAXIMUM POWERS', 'BILL MONOPOLIS', 'SENATOR SCHMEAR', 'MRS. FEATHERTOSS',
            'DR. JEAN SPLICER', 'RAFFLES THE CLOWN', 'ESPRESSA TOFFEEPOT', 'CECIL EDGAR VANDERTON']
ITEMS = ['FLASHLIGHT', 'CANDLESTICK', 'RAINBOW FLAG', 'HAMSTER WHEEL', 'ANIME VHS TAPE',
         'JAR OF PICKLES', 'ONE COWBOY BOOT', 'CLEAN UNDERPANTS', '5 DOLLAR GIFT CARD']
PLACES = ['ZOO', 'OLD BARN', 'DUCK POND', 'CITY HALL', 'HIPSTER CAFE',
          'BOWLING ALLEY', 'VIDEO GAME MUSEUM', 'UNIVERSITY LIBRARY', 'ALBINO ALLIGATOR PIT']
TIME_TO_SOLVE = 300  # Seconds

PLACE_FIRST_LETTERS = {}
LONGEST_PLACE_NAME_LENGTH = 0
for place in PLACES:
    PLACE_FIRST_LETTERS[place[0]] = place
    LONGEST_PLACE_NAME_LENGTH = len(place) if len(
        place) > LONGEST_PLACE_NAME_LENGTH else LONGEST_PLACE_NAME_LENGTH

assert len(SUSPECTS) == 9
assert len(ITEMS) == 9
assert len(PLACES) == 9
assert len(PLACE_FIRST_LETTERS.keys()) == len(PLACES)

knownSuspectsAndItems = []
visitedPlaces = {}
currentLocation = 'TAXI'
accusedSuspects = []
liars = random.sample(SUSPECTS, random.randint(3, 4))
accusationsLeft = 3
culprit = random.choice(SUSPECTS)

random.shuffle(SUSPECTS)
random.shuffle(ITEMS)
random.shuffle(PLACES)

clues = {}
for idx, interviewee in enumerate(SUSPECTS):
    if interviewee in liars:
        continue

    clues[interviewee] = {}
    clues[interviewee]['debug_liar'] = False
    for item in ITEMS:
        clues[interviewee][item] = PLACES[ITEMS.index(item)] if random.randint(
            0, 1) else SUSPECTS[ITEMS.index(item)]
    for suspect in SUSPECTS:
        clues[interviewee][suspect] = PLACES[SUSPECTS.index(
            suspect)] if random.randint(0, 1) else ITEMS[SUSPECTS.index(suspect)]

for i, interviewee in enumerate(SUSPECTS):
    if interviewee not in liars:
        continue

    clues[interviewee] = {}
    clues[interviewee]['debug_liar'] = True

    for item in ITEMS:
        if random.randint(0, 1):
            while True:
                clues[interviewee][item] = random.choice(PLACES)
                if clues[interviewee][item] != PLACES[ITEMS.index(item)]:
                    break
        else:
            while True:
                clues[interviewee][item] = random.choice(SUSPECTS)
                if clues[interviewee][item] != SUSPECTS[ITEMS.index(item)]:
                    break

    for suspect in SUSPECTS:
        if random.randint(0, 1):
            while True:
                clues[interviewee][suspect] = random.choice(PLACES)
                if clues[interviewee][suspect] != PLACES[SUSPECTS.index(suspect)]:
                    break
        else:
            while True:
                clues[interviewee][item] = random.choice(ITEMS)
                if clues[interviewee][item] != ITEMS[SUSPECTS.index(suspect)]:
                    break

zophieClues = {}
for interviewee in random.sample(SUSPECTS, random.randint(3, 4)):
    kindOfClue = random.randint(1, 3)
    if kindOfClue == 1:
        if interviewee not in liars:
            zophieClues[interviewee] = culprit
        elif interviewee in liars:
            while True:
                zophieClues[interviewee] = random.choice(SUSPECTS)
                if zophieClues[interviewee] != culprit:
                    break

    elif kindOfClue == 2:
        if interviewee not in liars:
            zophieClues[interviewee] = PLACES[SUSPECTS.index(culprit)]
        elif interviewee in liars:
            while True:
                zophieClues[interviewee] = random.choice(PLACES)
                if zophieClues[interviewee] != PLACES[SUSPECTS.index(culprit)]:
                    break

    elif kindOfClue == 3:
        if interviewee not in liars:
            zophieClues[interviewee] = ITEMS[SUSPECTS.index(culprit)]
        elif interviewee in liars:
            while True:
                zophieClues[interviewee] = random.choice(ITEMS)
                if zophieClues[interviewee] != ITEMS[SUSPECTS.index(culprit)]:
                    break

# pprint.pprint(clues)
# pprint.pprint(zophieClues)
# print(f'culprit = {culprit}')

print("""J'ACCUSE! (a mystery game)
Inspired by Homestar Runner\'s "Where\'s an Egg?" game

You are the world-famous detective Mathilde Camus.
ZOPHIE THE CAT has gone missing, and you must sift through the clues.
Suspects either always tell lies, or always tell the truth. Ask them
about other people, places, and items to see if the details they give are
truthful and consistent with your observations. Then you will know if
their clue about ZOPHIE THE CAT is true or not. Will you find ZOPHIE THE
CAT in time and accuse the guilty party?
""")
input('Press Enter to begin...')

startTime = time.time()
endTime = startTime + TIME_TO_SOLVE

while True:
    if time.time() > endTime or accusationsLeft == 0:
        if accusationsLeft == 0:
            print('You have accused too manny innocent people!')
        elif time.time() > endTime:
            print('You have run out of time!')
        culpritIdx = SUSPECTS.index(culprit)
        print(
            f'It was {culprit}at the {PLACES[culpritIdx]} with the {ITEMS[culpritIdx]} who catnapped her!')
        print('Better luck next time, Detective.')
        sys.exit()

    print()
    minutesLeft = int(endTime - time.time()) // 60
    secondsLeft = int(endTime - time.time()) % 60
    print(f'Time left: {minutesLeft} min, {secondsLeft} sec')

    if currentLocation == 'TAXI':
        print('  You are in your TAXI. Where do you want to go?')
        for place in sorted(PLACES):
            placeInfo = visitedPlaces[place] if place in visitedPlaces else ''
            nameLabel = '(' + place[0] + ')' + place[1:]
            spacing = " " * (LONGEST_PLACE_NAME_LENGTH - len(place))
            print(f'{nameLabel} {spacing}{placeInfo}')
        print('(Q)UIT GAME')
        while True:
            response = input('> ').upper()
            if response == '':
                continue
            if response == 'Q':
                print('Thanks for playing!')
                sys.exit()
            if response in PLACE_FIRST_LETTERS.keys():
                break
        currentLocation = PLACE_FIRST_LETTERS[response]
        continue

    print(f'  You are at the {currentLocation}.')
    currentLocationIdx = PLACES.index(currentLocation)
    personHere = SUSPECTS[currentLocationIdx]
    itemHere = ITEMS[currentLocationIdx]
    print(f'  {personHere} with the {itemHere} is here.')

    if personHere not in knownSuspectsAndItems:
        knownSuspectsAndItems.append(personHere)
    if ITEMS[currentLocationIdx] not in knownSuspectsAndItems:
        knownSuspectsAndItems.append(ITEMS[currentLocationIdx])
    if currentLocation not in visitedPlaces.keys():
        visitedPlaces[currentLocation] = f'({personHere.lower()}, {itemHere.lower()})'

    if personHere in accusedSuspects:
        print('They are offended that you accused them, and will not help you with your investigation.')
        print('You go back to your TAXI.')
        print()
        input('Press Enter to continue...')
        currentLocation = 'TAXI'
        continue

    print()
    print(f'(J) "J\'ACCUSE!" ({accusationsLeft} accusations left)')
    print('(Z) Ask if they know where ZOPHIE THE CAT is.')
    print('(T) Go back to the TAXI.')
    for idx, suspectOrItem in enumerate(knownSuspectsAndItems):
        print(f'({idx+1}) Ask about {suspectOrItem}')

    while True:
        response = input('> ').upper()
        if response in 'JZT' or (response.isdecimal() and eval(f'0 < {response} <= {len(knownSuspectsAndItems)}')):
            break

    if response == 'J':
        accusationsLeft -= 1
        if personHere == culprit:
            print('You\' ve cracked the case, Detective!')
            print(f'It was {culprit} who had catnapped ZOPHIE THE CAT.')
            minutesTaken = int(time.time() - startTime) // 60
            secondsTaken = int(time.time() - startTime) % 60
            print(
                f'Good job! You solved it in {minutesTaken} min, {secondsTaken} sec.')
            sys.exit()
        else:
            accusedSuspects.append(personHere)
            print('You have accused the wrong person, Detective!')
            print('They will not help you with anymore clues.')
            print('You go back to your TAXI.')
            currentLocation = 'TAXI'

    elif response == 'Z':
        if personHere not in zophieClues:
            print('"I don\'t know anything about ZOPHIE THE CAT.')
        elif personHere in zophieClues:
            print(f'  They give you this clue: "{zophieClues[personHere]}"')
            if zophieClues[personHere] not in knownSuspectsAndItems and zophieClues[personHere] not in PLACES:
                knownSuspectsAndItems.append(zophieClues[personHere])

    elif response == 'T':
        currentLocation = 'TAXI'
        continue

    else:
        inquiry = knownSuspectsAndItems[int(response) - 1]
        if inquiry in (personHere, itemHere):
            print('  They give you this clue: "No comment."')
        else:
            print(f'  They give you this clue: "{clues[personHere][inquiry]}"')
            if clues[personHere][inquiry] not in knownSuspectsAndItems and clues[personHere][inquiry] not in PLACES:
                knownSuspectsAndItems.append(clues[personHere][inquiry])

    input('Press Enter to continue...')
