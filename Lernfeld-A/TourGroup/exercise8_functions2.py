from random import randint
from math import pi, sqrt

# 1. Schreibe eine Funktion, die deinen Namen und dein Alter als Argumente 
# übernimmt und beides in einem Satz ausgibt.

print("Aufgabe 1\n")

def name(name, age):
    return f"Your name is {name} and you are {age} years old."

# Beispielaufruf
print(name("Stefan", 54))

# 2.  Schreibe die Funktion aus 1 so um, dass sie einen formatierten String 
# zurück gibt. Dokumentiere dabei intern alle Argumente und Rückgabewerte, 
# sowie deren Datentyp. 

print("\nAufgabe 2\n")

def name2(name: str, age: int) -> str:
    return f"Your name is {name} and you are {age} years old."

# Beispielaufruf
print(name2("Stefan", 54))

# 3.  Schreibe eine Funktion "Münzwurf", die einen solchen simuliert. Die Häufigkeit
# soll als Argument übergeben werden.

print("\nAufgabe 3\n")

def flip_coin():
    coin_flip = randint(0,1)
    return f"{"Kopf" if coin_flip == 1 else "Zahl"}"

# Beispielaufruf
for i in range(10):
    print(flip_coin())

# 4.  Schreibe eine Funktion zur Kreisberechnung, die zwei Argumente übernimmt: einen Zahlenwert
# und einen String, der aussagt, ob dieser Zahlenwert als Radius, Umfang oder Fläche zu verstehen ist.
# Radius soll dabei als Defaultwert eingestellt sein. Die Funktion soll dann die jeweils restlichen 
# Werte ausgeben.

print("\nAufgabe 4\n")

def calc_circle(value: int |float, unit: str ="r") -> str:
    area = 0
    circumference = 0
    radius = 0
    match unit:
        case "r":
            radius = value
            circumference = pi * (radius * 2)
            area = pi * (radius ** 2)
            return f"Given is a circle with a radius of {value:.2f}. The circumference equals {circumference:.2f} and the surface area equals {area:.2f}."
        case "a":
            area = value
            circumference = 2 * sqrt((pi * area))
            radius = circumference / (2 * pi)
            return f"Given is a circle with a surface area of {value:.2f}. The radius equals {radius:.2f} and the circumference equals {circumference:.2f}."
        case "c":
            circumference = value
            radius = circumference / (2 * pi)
            area = pi * (radius ** 2)
            return f"Given is a circle with a circumference of {value:.2f}. The radius equals {radius:.2f} and the surface area equals {area:.2f}."
        case _:
            return f"{unit} is not valid, please use 'r' for radius, 'a' for area or 'c' for circumference"
    return output

# Beispielaufruf
print(calc_circle(10))
print(calc_circle(10, "r"))
print(calc_circle(20, "a"))
print(calc_circle(20, "c"))

# 5.  Schreibe einen Passwortgenerator, der als Argument die Länge des Passwortes übernimmt
# und dieses zurück gibt.

print("\nAufgabe 5\n")

def pwgenSimple(pw_length: int) -> str:
    pw = ""
    for i in range(pw_length):
        pw += chr(randint(33, 126))
    return pw

# Beispielaufruf
print(pwgenSimple(20))

# 6.  Schreiben einen weiteren Passwortgenerator, der als Argumente die Anzahl der Zeichen
# aus dem Bereich der Kleinbuchstaben, der Großbuchstaben, der Zahlen und der Sonderzeichen
# übernimmt und ein entsprechendes Passwort zurück gibt.

print("\nAufgabe 6\n")

def get_character_in_range(start_character: str, end_character: str):
    character = chr(randint(ord(start_character), ord(end_character)))
    while character in ["i", "o", "l", "I", "O", "L"]:
        chr(randint(ord(start_character), ord(end_character)))
    return character

def pwgen_lower_letters(length: int) -> str:
    pw = ""
    for i in range(length):
        pw += get_character_in_range("a", "z")
    return pw

def pwgen_upper_letters(length: int) -> str:
    pw = ""
    for i in range(length):
        pw += get_character_in_range("A", "Z")
    return pw

def pwgen_numbers(length: int) -> str:
    pw = ""
    for i in range(length):
        pw += get_character_in_range("0", "9")
    return pw

def pwgen_specials(length: int) -> str:
    pw = ""
    for i in range(length):
        pw += get_character_in_range("!", "/")
    return pw

def pwgenPro(length_lower: int, length_upper: int, length_numbers: int, length_specials: int) -> str:
    pw = ""
    while length_lower + length_upper + length_numbers + length_specials > 0:
        character_type = randint(0, 3)
        if (character_type == 0 and length_lower > 0):
            pw += pwgen_lower_letters(1)
            length_lower -= 1
        if (character_type == 1 and length_upper > 0):
            pw += pwgen_upper_letters(1)
            length_upper -= 1
        if (character_type == 2 and length_numbers > 0):
            pw += pwgen_numbers(1)
            length_numbers -= 1
        if (character_type == 3 and length_specials > 0):
            pw += pwgen_specials(1)
            length_specials -= 1
    return pw

# Beispielaufruf
print(pwgenPro(5,5,5,5))
