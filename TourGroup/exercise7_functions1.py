# 1.    Quadrat einer Zahl berechnen: Schreibe eine Funktion quadrat(x),
#       die das Quadrat einer Zahl zurückgibt.

print("Aufgabe 1\n")

def square(base: int | float) -> int | float:
    return base * base

# Beispielaufruf
print(square(3))

# 2.    Summe von zwei Zahlen: Schreibe eine Funktion summe(a, b), 
#       die die Summe von zwei Zahlen berechnet.

print("\nAufgabe 2\n")

def sum(a : int | float | str, b : int | float | str) -> int | float | str:
    return a + b

# Beispielaufruf
print(sum("Stefan"," Koschnik"))
print(sum(3, 5))
print(sum(2.3, 6.8))

# 3.    Länge eines Strings: Schreibe eine Funktion laenge(s), 
#       die die Länge eines Strings zurückgibt.

print("\nAufgabe 3\n")

def length(s: str) -> int:
    return len(s)

# Beispielaufruf
print(length("Das ist ein String"))



# 4.    Größere Zahl finden: Schreibe eine Funktion groesser(a, b), 
#       die die größere von zwei Zahlen zurückgibt.

print("\nAufgabe 4\n")

def max(a : int | float, b :int | float) -> int | float:
    return a if a > b else b

# Beispielaufruf
print(max(10,5))

# 5.    Umwandlung in Großbuchstaben: Schreibe eine Funktion grossbuchstaben(s), 
#       die einen String in Großbuchstaben umwandelt.

print("\nAufgabe 5\n")

def caps_lock(s:str) -> str:
    return s.upper() if type(s) == str else f"'{s}' is not a string."

# Beispielaufruf
print(caps_lock("Das ist ein String."))
print(caps_lock({"Hallo":"Dictionary"})) # Muss abgefangen werden, weil kein String übergeben wurde


# 6.    Prüfen auf gerade Zahl: Schreibe eine Funktion ist_gerade(n), 
#       die überprüft, ob eine Zahl gerade ist.

print("\nAufgabe 6\n")

def is_even(a : int | float) -> bool:
    if type(a) == int:
        return a % 2 == 0
    else:
        return f"{a} is not an integer."

# Beispielaufruf
print(is_even(4))
print(is_even(5))
print(is_even(5.5)) # Muss abgefangen werden, weil keine Ganzzahl übergeben wurde


# 7.    Umkehrung eines Strings: Schreibe eine Funktion umkehren(s), 
#       die einen String umkehrt.

print("\nAufgabe 7\n")

def reverse(s: str):
    return s[::-1]

# Beispielaufruf
print(reverse("HAllo"))


# 8.    Durchschnitt von drei Zahlen: Schreibe eine Funktion durchschnitt(a, b, c), 
#       die den Durchschnitt von drei Zahlen berechnet.

print("\nAufgabe 8\n")

def average(number: int | float, *more_numbers: int | float) -> float:
    total = number
    for number in more_numbers:
        total += number
    return f"{total / (1 + len(more_numbers)):.2f}"

# Beispielaufruf
print(average(5,8,10,11,12))
