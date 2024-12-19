from enum import Enum
from pprint import pprint

"""
Stelle folgenden Sachverhalt objektorientiert dar:

Ein Mensch zieht in ein Haus und 
möbliert es mit Gegenständen aus einem Einrichtungshaus. 

Objekte: Mensch, Haus, Laden (Einrichtungshaus), Waren (Gegenstände)

Mensch:
- Attribute
    - Geschlecht
    - Alter
    - Namen
    - Konto
    - Adresse
- Methoden
    - Einkaufen
    - Einziehen
    - Bezahlen
    - ...

Haus:
- Attribute
    - Räume: List<Raum>

Raum:
- Attribute
    - Art
    - Möbel: List<Möbel>

Möbel:
- Attribute
    - Art
    - Preis

Einrichtungshaus:
- Attribute
    - Konto
    - Inventar: Dict({Möbelart: List<Möbel>})
- Methoden
    - Rechnung ausstellen
    - Waren Liefern
    - Bestand Anderung
    - Konto Anderung
    (- Waren einkaufen)

Möbelart<enum>:
- Attributen
    - Tisch
    - Stuhl
    - Schrank
    - Regal
    - Lampe
    - Bett
    - Geräte
"""
def to_string(self) -> str:
    result = f"{self.__class__.__name__}: " + "{"
    object_attributes_as_dictionary = self.__dict__
    for attribute, value in object_attributes_as_dictionary.items():
        result += f"{attribute}:{value}, "
    return result.removesuffix(", ") + "}"

def to_string_enum(self) -> str:
    result = f"{self.__class__.__name__}: "
    result += self._value_
    return result

class Gender(Enum):
    MALE = "Männlich"
    FEMALE = "Weiblich"
    DIVERS = "Divers"

    def __str__(self):
        return to_string_enum(self)

class Furniture_Category(Enum):
    CLOSET = "Schrank"
    DEVICE = "Gerät"
    TABLE = "Tisch"
    CHAIR = "Stuhl"
    SHELF = "Regal"
    LAMP = "Lampe"
    BED = "Bett"

    def __str__(self):
        return to_string_enum(self)

class Address():
    def __init__(self, street: str, house_number: str, postal_code: int, city: str, country: str):
        self.street = street
        self.house_number = house_number
        self.postal_code = postal_code
        self.city = city
        self.country = country

    def __str__(self):
        return to_string(self)

class Person():
    count_Human = 0

    def __init__(self, name: str, age: int, gender: Gender, address: Address, bank_account: float):
        Person.count_Human += 1
        self.name = name
        self.age = age
        self.gender = gender
        self.address = address
        self.bank_account = bank_account
    
    def __str__(self):
        return to_string(self)
    
    def __eq__(self, other: "Person"): 
        # Name der eigenen Klasse ist erst nach Durchlauf des Interpreters verfügbar. 
        # Workaround: nutze den Namen als string
        self_dict = self.__dict__
        other_dict = other.__dict__
        for key, value in self_dict.items():
            if key not in other_dict or value != other_dict.get(key):
                return False
        return True

test_street = Address("test street", 1, 20014, "test city", "test country")
peter = Person("Peter", 30, Gender.MALE, test_street, 200)
katrin = Person("Katrin", 25, Gender.FEMALE, test_street, 400)
print(peter)
print(katrin)
print(peter == peter)
print(peter == katrin)

class Furniture():
    def __init__(self, name, article_number, furniture_category, cost):
        self.name = name
        self.article_number = article_number
        self.furniture_category = furniture_category
        self.cost = cost
    
    def __str__(self):
        return to_string(self)
    
    def __repr__(self):
        return to_string(self)

table = Furniture("large table", "001", Furniture_Category.TABLE, 200)
table_small = Furniture("small table", "002", Furniture_Category.TABLE, 50)
print(table)
print(table_small)


# Einrichtungshaus:
# - Attribute
#     - Konto
#     - Inventar: Dict({Möbelart: List<Möbel>})
# - Methoden
#     - Rechnung ausstellen
#     - Waren Liefern
#     - Bestand Anderung
#     - Konto Anderung
#     (- Waren einkaufen)

class Furniture_store():
    def __init__(self, bank_account, inventory: dict = dict()):
        self.bank_account = bank_account
        self.inventory = inventory

    def __repr__(self):
        return to_string(self)

    def __str__(self):
        return to_string(self)
    
    def buy_furniture(self, customer: Person, furniture_category: Furniture_Category, furniture_name: str = "", article_number: str = ""):
        if furniture_name in ["", None] and article_number in ["", None]:
            print("Falsche Eingabe, bitte gib mindestens die Artikelnummer oder den Namen des Möbelstücks an!")
            return
        category: list = self.inventory.get(furniture_category)
        for furniture in category:
            furniture:Furniture
            if furniture.name == furniture_name or furniture.article_number == article_number:
                category.remove(furniture)
                self.bank_account += furniture.cost
                customer.bank_account -= furniture.cost

bed = Furniture("bed", "003", Furniture_Category.BED, 600.0)
chair = Furniture("chair", "004", Furniture_Category.CHAIR, 100.99)
closet = Furniture("close", "005", Furniture_Category.CLOSET, 130.95)
lamp = Furniture("lamp", "006", Furniture_Category.LAMP, 60)
device = Furniture("device", "007", Furniture_Category.DEVICE, 340)
shelf = Furniture("shelf", "008", Furniture_Category.SHELF, 120)

inventory: dict = {Furniture_Category.TABLE: [table, table_small],
    Furniture_Category.BED: [bed],
    Furniture_Category.CHAIR: [chair],
    Furniture_Category.CLOSET: [closet],
    Furniture_Category.LAMP: [lamp],
    Furniture_Category.DEVICE: [device],
    Furniture_Category.SHELF: [shelf]}

furniture_store = Furniture_store(200, inventory)
print(Furniture_store(200))
pprint(furniture_store)
