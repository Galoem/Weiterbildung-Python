# Aufgabe 1: Erstellen eines einfachen Dictionaries 'personen'
# Erstelle ein Dictionary, das die Namen von drei Personen als Schlüssel 
# und ihre Alter als Werte enthält.

print("\nAufgabe 1\n")

name_age_dict = {"Julian": 31,
                "Maximilian": 32,
                "Nuri": 33}

print(name_age_dict)

# Aufgabe 2: Zugriff auf einen Wert
# Greife auf das Alter einer Person aus dem Dictionary personen zu.

print("\nAufgabe 2\n")

print(name_age_dict["Julian"])
print(name_age_dict.get("Maximilian"))
print(name_age_dict.get("Nuri", 0))
print(name_age_dict.get("Fekadu", 0))

# Aufgabe 3: Hinzufügen eines neuen Eintrags
# Füge einen neuen Eintrag für "David" mit dem Alter 28 zum Dictionary personen hinzu.

print("\nAufgabe 3\n")

name_age_dict["Fekadu"] = 35
print(name_age_dict)

# Aufgabe 4: Ändern eines Wertes
# Ändere das Alter einer Person auf 31 im Dictionary personen.

print("\nAufgabe 4\n")

name_age_dict.update({"Maximilian": 31})
print(name_age_dict)

# Aufgabe 5: Entfernen eines Eintrags
# Entferne eine Person aus dem Dictionary personen.

print("\nAufgabe 5\n")
name_age_dict["test"] = 5

print(name_age_dict.pop("test"))
print(name_age_dict)

# Aufgabe 6: Überprüfen, ob ein Schlüssel existiert
# Überprüfe, ob der Schlüssel "Eva" im Dictionary personen existiert.

print("\nAufgabe 6\n")

print("test" in name_age_dict)
print("Julian" in name_age_dict)

# Aufgabe 7: Iterieren über ein Dictionary
# Iteriere über das Dictionary personen und gebe jeden Schlüssel-Wert-Paar aus.

print("\nAufgabe 7\n")

for name, age in name_age_dict.items():
    print(name, "->", age)

# Aufgabe 8: Verschachtelte Dictionaries
# Erstelle ein Dictionary 'personen_info', das Informationen über zwei Personen enthält, wobei jede 
# Person ein eigenes Dictionary mit den Schlüsseln "Name", "Alter" und "Stadt" hat.

print("\nAufgabe 8\n")

nested_name_dict = {"Julian": {"age": 31, "city": "Bremen"},
        "Maximilian": {"age": 32, "city": "Frankfurt"},
        "Nuri": {"age": 33, "city": "Berlin"},
        "Fekadu": {"age": 34, "city": "Augsburg"}}

print(nested_name_dict)

# Aufgabe 9: Zugriff auf verschachtelte Werte
# Greife auf die Stadt von "Person2" aus dem Dictionary 'personen_info' zu.

print("\nAufgabe 9\n")

print(nested_name_dict.get("Julian"))
print(nested_name_dict.get("Julian").get("city"))

# Aufgabe 10: Zusammenführen von Dictionaries
# Erstelle zwei Dictionaries und führe sie zu einem neuen Dictionary zusammen.

print("\nAufgabe 10\n")

dict1 = {"Julian": 31,
        "Emilia": 32}
dict2 = {"Maximilian": 32,
        "Nuri": 33,
        "Fekadu": 35}

merged_dict = dict1.copy()
merged_dict.update(dict2)

print(merged_dict)

# Alternative
dict3 = dict1 | dict2
print(dict3)
