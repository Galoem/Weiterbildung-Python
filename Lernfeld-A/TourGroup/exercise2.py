# 1. Schreibe ein Programm, das eine Zahl von der Eingabe liest und ausgibt, 
# ob die Zahl positiv, negativ oder null ist.

print("\nAufgabe 1\nPositive, negativ or 0?\n")

aufgabe1 = int(input("Please insert a number (positive, negative or 0): "))
if aufgabe1 == 0:
    print("inserted number is 0")
elif aufgabe1 > 0:
    print("inserted a positive number")
else:
    print("inserted a negative number")


# 2. Schreibe ein Programm, das eine Zahl von der Eingabe liest und ausgibt, 
# ob die Zahl gerade oder ungerade ist.

print("\nAufgabe 2\nEven or odd?\n")

aufgabe2 = int(input("Please insert a number: "))
if aufgabe2 % 2 == 0:
    print("inserted number is even")
else:
    print("inserted number is odd")


# 3. Schreibe ein Programm, das eine Zahl von der Eingabe liest und ausgibt, 
# ob die Zahl im Bereich von 1 bis 10 liegt.

print("\nAufgabe 3\nIs in range of 1 - 10\n")

aufgabe3 = int(input("Please insert a number: "))
if aufgabe3 < 1 or aufgabe3 > 10:
    print("inserted number is out of bounds")
else:
    print("inserted number is in bounds")


# 4. Schreibe ein Programm, das drei Zahlen von der Eingabe liest 
# und die größte der drei Zahlen ausgibt.

print("\nAufgabe 4\nWhich is greatest?\n")

aufgabe4_1 = int(input("Please insert a first number: "))
aufgabe4_2 = int(input("Please insert a second number: "))
aufgabe4_3 = int(input("Please insert a third number: "))

if aufgabe4_1 > aufgabe4_2 and aufgabe4_1 > aufgabe4_3:
    print(f"{aufgabe4_1} is the greatest number")
elif aufgabe4_2 > aufgabe4_1 and aufgabe4_2 > aufgabe4_3:
    print(f"{aufgabe4_2} is the greatest number")
elif aufgabe4_3 > aufgabe4_1 and aufgabe4_3 > aufgabe4_2:
    print(f"{aufgabe4_3} is the greatest number")
else:
    print(f"there is no greatest number first: {aufgabe4_1}, second: {aufgabe4_2}, third: {aufgabe4_3}")


# 5. Schreibe ein Programm, das eine Zahl (1-7) von der Eingabe liest 
# und den entsprechenden Wochentag ausgibt 
# (1: Montag, 2: Dienstag, ..., 7: Sonntag).

print("\nAufgabe 5\nWhat day is it?\n")

aufgabe5 = int(input("Please insert a number between 1 - 7: "))
match aufgabe5:
    case 1:
        weekday = "monday"
    case 2:
        weekday = "tuesday"
    case 3:
        weekday = "wednesday"
    case 4:
        weekday = "thursday"
    case 5:
        weekday = "friday"
    case 6:
        weekday = "saturday"
    case 7:
        weekday = "sunday"
    case _:
        print(f"input not supported {aufgabe5}")
        exit(-1)

print(f"weekday number {aufgabe5} is {weekday}")

# 6. Schreibe ein Programm, das eine Zahl von der Eingabe liest und ausgibt, 
# ob die Zahl durch 2, 3 oder 5 teilbar ist.

print("\nAufgabe 6\nDividable by 2, 3 or 5?\n")

aufgabe6 = int(input("Please insert a number: "))
isDividable = False
if aufgabe6 % 2 == 0:
    print(f"{aufgabe6} is dividable by 2")
    isDividable = True
if aufgabe6 % 3 == 0:
    print(f"{aufgabe6} is dividable by 3")
    isDividable = True
if aufgabe6 % 5 == 0:
    print(f"{aufgabe6} is dividable by 5")
    isDividable = True
if not isDividable:
    print(f"{aufgabe6} is not dividable by 2, 3 or 5")

# 7. Schreibe ein Programm, das zwei Strings von der Eingabe liest und ausgibt, 
# ob die Strings gleich sind, der erste String länger ist oder 
# der zweite String länger ist.

print("\nAufgabe 7\nWhich is longer?\n")

aufgabe7_1 = input("Please insert a string: ")
aufgabe7_2 = input("Please insert another string: ")

if len(aufgabe7_1) > len(aufgabe7_2):
    print(f"{aufgabe7_1} has more symbols than {aufgabe7_2}")
elif len(aufgabe7_2) > len(aufgabe7_1):
    print(f"{aufgabe7_2} has more symbols than {aufgabe7_1}")
else:
    print(f"{aufgabe7_1} has the same amount of symbols as {aufgabe7_2}")

# 8. Schreibe ein Programm, das einen String und einen Buchstaben von der 
# Eingabe liest und ausgibt, ob der Buchstabe im String enthalten ist, 
# nicht enthalten ist oder der String leer ist.

print("\nAufgabe 8\nIs character included?\n")

aufgabe8_string = input("Please insert a string: ")
aufgabe8_char = input("Please insert a character: ")

if aufgabe8_string.find(aufgabe8_char) != -1:
    print(f"{aufgabe8_char} is included in {aufgabe8_string}")
else:
    print(f"{aufgabe8_char} is not included in {aufgabe8_string}")

# 9. Schreibe ein Programm, das einen String von der Eingabe liest und ausgibt, 
# ob der String nur aus Buchstaben, nur aus Zahlen oder 
# aus einer Mischung von beiden besteht.

print("\nAufgabe 9\nIs numeric, alpha or alphanumeric?\n")

aufgabe9 = input("Please insert something: ")

if aufgabe9.isnumeric():
    print(f"{aufgabe9} is numeric")
elif aufgabe9.isalpha():
    print(f"{aufgabe9} consists only of letters")
else:
    print(f"{aufgabe9} consists of letters and numbers")

# 10. Schreibe ein Programm, das einen String von der Eingabe liest und ausgibt, 
# ob der String mit einem bestimmten Suffix (hinterster Teilstring) endet.

print("\nAufgabe 10\nHas suffix?\n")

aufgabe10_string = input("Please insert a string: ")
aufgabe10_suffix = input("Please insert a suffix: ")

if aufgabe10_string.endswith(aufgabe10_suffix):
    print(f"{aufgabe10_string} ends with {aufgabe10_suffix}")
else:
    print(f"{aufgabe10_string} does not end with {aufgabe10_suffix}")
