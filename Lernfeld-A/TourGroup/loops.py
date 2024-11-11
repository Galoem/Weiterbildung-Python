separator = "\n====================\n"

def getInputNumber(text="Please insert a number: "):
    userInput = input(text)
    if userInput.isnumeric():
        return int(userInput)
    else:
        print(userInput, "is not a number")
        return getInputNumber(text)

def getInputNumbersList(text="Please enter any number of numerical values: "):
    result = []
    userInput = input(text + ": ")
    inputs = userInput.split(",")
    for n in inputs:
        if n.isnumeric():
            result.append(int(n))
        else:
            print(f"user input contains alpha characters")
            return getInputNumbersList(text)
    return result

def dividableBy3(number):
    return number % 3 == 0

def dividableBy5(number):
    return number % 5 == 0

def dividableBy3And5(number):
    return dividableBy3(number) and dividableBy5(number)

# 1. Summe der ersten n natürlichen Zahlen:
# Schreibe ein Programm, das die Summe der ersten n natürlichen Zahlen berechnet.
print("Aufgabe 1 - Summe der ersten n natürlichen Zahlen")

task1 = getInputNumber()
result = 0
for n in range(task1):
    result += n + 1

print(result, separator)

# 2. Durchschnitt berechnen:
# Schreibe ein Programm, das den Durchschnitt einer Liste von Zahlen berechnet.
print("Aufgabe 2 - Durchschnitt berechnen")

task2 = getInputNumbersList()
quantity = len(task2)
total = 0
for number in task2:
    total += number
print(f"The average value of given numbers is {total / quantity:.2f}", separator)

# 3. Zahlenreihe ausgeben:
# Schreibe ein Programm, das die Zahlen von 1 bis 100 ausgibt.
print("Aufgabe 3 - Zahlenreihe")

for index in range(100):
    print(index + 1)

print(separator)

# 4. Gerade Zahlen ausgeben:
# Schreibe ein Programm, das alle geraden Zahlen von 1 bis 50 ausgibt.
print("Aufgabe 4 - Gerade Zahlen")

for index in range(50):
    if (index + 1) % 2 == 0:
        print(index + 1)

print(separator)

# 5. Quadratzahlen berechnen:
# Schreibe ein Programm, das die Quadratzahlen der ersten 10 natürlichen Zahlen berechnet und ausgibt.
print("Aufgabe 5 - Quadrieren")

for index in range(10):
    print(f"{index + 1}² = {(index + 1)**2}")

print(separator)

# 6. Liste invertieren:
# Schreibe ein Programm, das eine Liste von Zahlen invertiert.
print("Aufgabe 6 - Liste invertieren")

task6_1 = getInputNumbersList()
for number in task6_1:
    print(number * -1)

task6_1.reverse()
for number in task6_1:
    print(number)

task6_2 = getInputNumber()
for number in range(task6_2, 0, -1):
    print(number)

print(separator)

# 7. Wörter zählen:
# Schreibe ein Programm, das die Anzahl der Wörter in einem gegebenen Satz zählt.
print("Aufgabe 7 - Wörter zählen")

task7 = input("Please insert a whole sentence or more: ")
words = task7.split()
print(len(words), separator)

# 8. Multiplikationstabelle:
# Schreibe ein Programm, das die Multiplikationstabelle für eine gegebene Zahl n ausgibt (z.B. für n=5: 5x1=5, 5x2=10, ..., 5x10=50).
print("Aufgabe 8 - Multiplikationstabelle")

task8 = getInputNumber()
print(f"n={task8}:")
for multiplier in range(50):
    print(f"\t{task8} x {multiplier + 1} = {task8 * (multiplier + 1)}")

print(separator)

# 9. Zahlenreihe mit Schrittweite:
# Schreibe ein Programm, das die Zahlen von 1 bis 100 mit einer Schrittweite von 5 ausgibt.
print("Aufgabe 9 - Zahlenreihe mit Schrittweite")

for number in range(0, 100, 5):
    print(number)

print(separator)

# 10. Nested Loops:
# Schreibe ein Programm, das eine Multiplikationstabelle für die Zahlen von 1 bis 10 ausgibt.
print("Aufgabe 10 - Verschachtelte Schleifen")

for n in range(10):
    print(n + 1, ": ")
    for multiplier in range(10):
        print(f"\t{n + 1} x {multiplier + 1} = {(n + 1) * (multiplier + 1)}")

print(separator)

# 11. String umkehren:
# Schreibe ein Programm, das einen gegebenen String umkehrt.
print("Aufgabe 11 - String umkehren")

task11 = input("please insert a string: ")
result = ""
for char in task11:
    result = char + result
print(result, separator)

# 12. Liste von Quadraten:
# Schreibe ein Programm, das eine Liste von Zahlen nimmt und eine neue Liste mit den Quadraten dieser Zahlen erstellt.
print("Aufgabe 12 - Eingabeliste Quadrieren")

task12 = getInputNumbersList()
result = []
for number in task12:
    result.append(number**2)
print(result, separator)

# 13. Zahlenreihe mit Bedingung:
# Schreibe ein Programm, das die Zahlen von 1 bis 100 ausgibt, aber jede Zahl durch "Fizz" ersetzt, wenn sie durch 3 teilbar ist, und durch "Buzz" ersetzt, wenn sie durch 5 teilbar ist. Wenn sie durch beide teilbar ist, soll "FizzBuzz" ausgegeben werden.
print("Aufgabe 13 - FizzBuzz")

for number in range(100):
    result = number + 1
    print(f"{"FizzBuzz" if dividableBy3And5(result) else "Fizz" if dividableBy3(result) else "Buzz" if dividableBy5(result) else result}")

print(separator)

# 14. Liste von Wörtern filtern:
# Schreibe ein Programm, das eine Liste von Wörtern nimmt und eine neue Liste mit den Wörtern erstellt, die länger als 5 Zeichen sind.
print("Aufgabe 14 - Lange Worte filtern")

task14 = input("Please insert a sentence or more: ")
words = task14.split()
wordsOfLength5OrGreater = []
for word in words:
    if len(word) >= 5:
        wordsOfLength5OrGreater.append(word)
print(wordsOfLength5OrGreater, separator)

# 15. Matrix ausgeben:
# Schreibe ein Programm, das eine 3x3-Matrix mit Zahlen von 1 bis 9 ausgibt.
print("Aufgabe 15 - Matrix")

result2 = ""
for number in range(1, 10):
    result2 += str(number) + f" {"\n" if number % 3 == 0 else ""}"
print(result2, separator)

# 16. Zahlenreihe mit Bedingung und Schrittweite:
# Schreibe ein Programm, das die Zahlen von 1 bis 100 mit einer Schrittweite von 7 ausgibt, aber jede Zahl durch "Boom" ersetzt, wenn sie durch 7 teilbar ist.
print("Aufgabe 16 - Boom")

for number in range(0, 100, 7):
    print(f"{"Boom" if number % 7 == 0 else number}")

print(separator)
