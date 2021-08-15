import sys
import csv
import re

COLUMNS = ['Atomic Number', 'Symbol', 'Element', 'Origin of name', 'Group', 'Period', 'Atomic weight', 'Density',
           'Melting point', 'Boiling point', 'Specific heat capacity', 'Electronegativity', "Abundance in earth's crust"]
UNITS = {'Atomic weight': 'u',
         'Density': 'g/cm^3',
         'Melting point': 'K',
         'Boiling point': 'K',
         'Specific heat capacity': 'J/(g*K)',
         "Abundance in earth's crust": 'mg/kg'}

elementsDict = {}
with open('periodictable.csv') as tableFile:
    csvReader = csv.reader(tableFile)
    for row in csvReader:
        elementsDict[int(row[0])] = row[1:]

print('Periodic Table')

while True:
    print('''
            Periodic Table of Elements
      1  2  3  4  5  6  7  8  9  10 11 12 13 14 15 16 17 18
    1 H                                                  He
    2 Li Be                               B  C  N  O  F  Ne
    3 Na Mg                               Al Si P  S  Cl Ar
    4 K  Ca Sc Ti V  Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr
    5 Rb Sr Y  Zr Nb Mo Tc Ru Rh Pd Ag Cd In Sn Sb Te I  Xe
    6 Cs Ba La Hf Ta W  Re Os Ir Pt Au Hg Tl Pb Bi Po At Rn
    7 Fr Ra Ac Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og

            Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu
            Th Pa U  Np Pu Am Cm Bk Cf Es Fm Md No Lr
''')
    print('Enter a symbol or atomic number to examine, or QUIT to quit.')
    while True:
        userInquiry = input('> ').title()
        if userInquiry.upper() == 'QUIT':
            sys.exit()
        if userInquiry.isdigit() and eval(f'1<={userInquiry}<=118'):
            userInquiry = int(userInquiry)
            break
        if userInquiry in [value[0] for value in elementsDict.values()]:
            userInquiry = [value[0]
                           for value in elementsDict.values()].index(userInquiry) + 1
            break
        print('Invalid input.')

    print(f'{COLUMNS[0].rjust(26)}: {userInquiry}')
    for idx, entry in enumerate(elementsDict[userInquiry]):
        entry = re.sub(r'\[(I|V|X)+\]', '', entry)

        print(f'{COLUMNS[idx+1].rjust(26)}: {entry}', end=' ')
        if UNITS.get(COLUMNS[idx+1], False):
            print(UNITS[COLUMNS[idx+1]])
        else:
            print()

    input('Press Enter to continue...')
