import re

# Taxitarif Frankfurt
# Grundgebühr:                      4,00 EUR
# Kilometerpreis bis inkl. 3km:     2,80 EUR
# Kilometerpreis über 3km bis 7km:  2,60 EUR
# Kilometerpreis über 7km:          2,10 EUR

BASE_PRICE = 4.30
KILOMETER_PRICE_FIRST_SECTION = 2.80
KILOMETER_PRICE_SECOND_SECTION = 2.60
KILOMETER_PRICE_THIRD_SECTION = 2.10
FIRST_SECTION_KILOMETERS = 3
SECOND_SECTION_KILOMETERS = 7
THIRD_SECTION_KILOMETERS_ABOVE = 7

def getInput():
    userInput = input("How far would you like to drive in km: ")

    if not re.match(r"\d+(\.\d+)?", userInput):
        print(f"not a number: {userInput}")
        return getInput()

    return float(userInput)

def calcFirstSection(kilometers=FIRST_SECTION_KILOMETERS):
    return KILOMETER_PRICE_FIRST_SECTION * kilometers

def calcSecondSection(kilometers=SECOND_SECTION_KILOMETERS):
    return KILOMETER_PRICE_SECOND_SECTION * (kilometers - FIRST_SECTION_KILOMETERS)

def calcThirdSection(kilometers):
    return KILOMETER_PRICE_THIRD_SECTION * (kilometers - SECOND_SECTION_KILOMETERS)

def getSpacing(value):
    return "  " if value < 10 else " " if value < 100 else ""

def calcTotal(firstSectionTotal, secondSectionTotal=None, thirdSectionTotal=None):
    return BASE_PRICE + firstSectionTotal + (secondSectionTotal if secondSectionTotal != None else 0) + (thirdSectionTotal if thirdSectionTotal != None else 0)

def printReceipt(total, firstSectionTotal, secondSectionTotal=None, thirdSectionTotal=None):
    print(f"\n\nReceipt for your trip ({kilometers}km):")
    print(f"\tBase price: \t\t\t\t  {BASE_PRICE:.2f} EUR")
    print(f"\tKilometers 0 - 3   (each {KILOMETER_PRICE_FIRST_SECTION:.2f} EUR): \t  {firstSectionTotal:.2f} EUR")
    if secondSectionTotal != None:
        print(f"\tKilometers 3 - 7   (each {KILOMETER_PRICE_SECOND_SECTION:.2f} EUR): \t{getSpacing(secondSectionTotal)}{secondSectionTotal:.2f} EUR")
    if thirdSectionTotal != None:
        print(f"\tKilometers above 7 (each {KILOMETER_PRICE_THIRD_SECTION:.2f} EUR): \t{getSpacing(thirdSectionTotal)}{thirdSectionTotal:.2f} EUR")
    print("\t\t\t====================================")
    print(f"\tTotal: \t\t\t\t\t{"  " if total < 10 else " " if total < 100 else ""}{total:.2f} EUR")
    print(f"\nThank you for traveling with us, have a save trip! :)\n\n")

kilometers = getInput()

if kilometers <= FIRST_SECTION_KILOMETERS:
    firstSectionTotal = calcFirstSection(kilometers)
    secondSectionTotal = None
    thirdSectionTotal = None

elif kilometers <= SECOND_SECTION_KILOMETERS:
    firstSectionTotal = calcFirstSection()
    secondSectionTotal = calcSecondSection(kilometers)
    thirdSectionTotal = None

else:
    firstSectionTotal = calcFirstSection()
    secondSectionTotal = calcSecondSection()
    thirdSectionTotal = calcThirdSection(kilometers)

total = calcTotal(firstSectionTotal, secondSectionTotal, thirdSectionTotal)
printReceipt(total, firstSectionTotal, secondSectionTotal, thirdSectionTotal)
