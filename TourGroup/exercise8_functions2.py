import string
import random
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

def flip_coin(frequency: int) -> str:
    coin_flips = []
    for _ in range(frequency):
        coin_flips.append("Kopf" if random.randint(0,1) else "Zahl")
    return coin_flips

# Beispielaufruf
print(flip_coin(10))

# 4.  Schreibe eine Funktion zur Kreisberechnung, die zwei Argumente übernimmt: einen Zahlenwert
# und einen String, der aussagt, ob dieser Zahlenwert als Radius, Umfang oder Fläche zu verstehen ist.
# Radius soll dabei als Defaultwert eingestellt sein. Die Funktion soll dann die jeweils restlichen 
# Werte ausgeben.

print("\nAufgabe 4\n")

def calc_circumference_from_radius(radius: int | float) -> float:
    return pi * (radius * 2)

def calc_circumference_from_area(area: int | float) -> int | float:
    return 2 * sqrt((pi * area))

def calc_area_from_radius(radius: int | float) -> int | float:
    return pi * (radius ** 2)

def calc_radius_from_circumference(circumference: int | float) -> int | float:
    return circumference / (2 * pi)

def calc_circle(value: int | float, unit: str = "r") -> str:
    """
    Parameters:
        :param value (int | float): Value for calculation.
        :param unit (str): Unit of value -> 'r' for radius, 'a' for area or 'c' for circumference.
    """
    area = 0
    radius = 0
    circumference = 0
    match unit:
        case "r":
            radius = value
            circumference = calc_circumference_from_radius(radius)
            area = calc_area_from_radius(radius)
            return f"Given is a circle with a radius of {value:.2f}. The circumference equals {circumference:.2f} and the surface area equals {area:.2f}."
        case "a":
            area = value
            circumference = calc_circumference_from_area(area)
            radius = calc_radius_from_circumference(circumference)
            return f"Given is a circle with a surface area of {value:.2f}. The radius equals {radius:.2f} and the circumference equals {circumference:.2f}."
        case "c":
            circumference = value
            radius = calc_radius_from_circumference(circumference)
            area = calc_area_from_radius(radius)
            return f"Given is a circle with a circumference of {value:.2f}. The radius equals {radius:.2f} and the surface area equals {area:.2f}."
        case _:
            return f"{unit} is not valid, please use 'r' for radius, 'a' for area or 'c' for circumference"
    return output

# Beispielaufruf
print(calc_circle(10))
print(calc_circle(10, "r"))
print(calc_circle(20, "a"))
print(calc_circle(20, "c"))
print(calc_circle(20, "z")) # invalid

# 5.  Schreibe einen Passwortgenerator, der als Argument die Länge des Passwortes übernimmt
# und dieses zurück gibt.

print("\nAufgabe 5\n")

def pwgenSimple(pw_length: int) -> str:
    pw = ""
    for _ in range(pw_length):
        pw += chr(random.randint(ord("!"), ord("z")))
    return pw

# Beispielaufruf
print(pwgenSimple(20))

# 6.  Schreiben einen weiteren Passwortgenerator, der als Argumente die Anzahl der Zeichen
# aus dem Bereich der Kleinbuchstaben, der Großbuchstaben, der Zahlen und der Sonderzeichen
# übernimmt und ein entsprechendes Passwort zurück gibt.

print("\nAufgabe 6\n")

def get_character_in_range(start_character: str, end_character: str):
    character = chr(random.randint(ord(start_character), ord(end_character)))
    while character in ["i", "o", "l", "I", "O", "L"]:
        character = chr(random.randint(ord(start_character), ord(end_character)))
    return character

def pwgen_lower_letters(length: int) -> str:
    pw = ""
    for _ in range(length):
        pw += get_character_in_range("a", "z")
    return pw

def pwgen_upper_letters(length: int) -> str:
    pw = ""
    for _ in range(length):
        pw += get_character_in_range("A", "Z")
    return pw

def pwgen_numbers(length: int) -> str:
    pw = ""
    for _ in range(length):
        pw += get_character_in_range("0", "9")
    return pw

def pwgen_specials(length: int) -> str:
    pw = ""
    for _ in range(length):
        pw += get_character_in_range("!", "/")
    return pw

def pwgenPro(length_lower: int, length_upper: int, length_numbers: int, length_specials: int) -> str:
    """
    Generates a random password.

    Paramaters:
        :param length_lower (int): number of lower alpha characters.
        :param length_upper (int): number of upper alpha characters.
        :param length_number (int): number of numberic characters.
        :param length_specials (int): number of special characters.

    Returns:
        a shuffled password containing a number of differen characters.
    """
    pw = ""
    while length_lower + length_upper + length_numbers + length_specials > 0:
        character_type = random.randint(0, 3)
        if (character_type == 0 and length_lower > 0):
            pw += pwgen_lower_letters(1)
            length_lower -= 1
        elif (character_type == 1 and length_upper > 0):
            pw += pwgen_upper_letters(1)
            length_upper -= 1
        elif (character_type == 2 and length_numbers > 0):
            pw += pwgen_numbers(1)
            length_numbers -= 1
        elif (character_type == 3 and length_specials > 0):
            pw += pwgen_specials(1)
            length_specials -= 1
    return pw

# Beispielaufruf
print(pwgenPro(5,5,5,5))


# Alternative
def pwgenPro2(length_lower: int, length_upper: int, length_numbers: int, length_specials: int) -> str:
    pw = []
    pw += random.choices(string.ascii_lowercase, k=length_lower)
    pw += random.choices(string.ascii_uppercase, k=length_upper)
    pw += random.choices(string.digits, k=length_numbers)
    pw += random.choices(string.punctuation, k=length_specials)
    random.shuffle(pw)
    return "".join(pw)

print(pwgenPro2(5,5,5,5))
