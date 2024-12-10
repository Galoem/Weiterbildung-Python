PI = 3.14159

def surface_area(radius: float) -> float:
    radius_square = radius * radius
    return radius_square * PI

print(surface_area(10))

# --------------------------------------------

bass_intensity = 2

def bass_increase():
    global bass_intensity

    print("Alter Wert:", bass_intensity)
    if bass_intensity < 3:
        bass_intensity += 1
        print("Neuer Wert:", bass_intensity)
    else:
        print("Wert nicht erhöht")

bass_increase()
print("Wert nach Aufruf von bass_increase:", bass_intensity)


def bass_decrease():
    global bass_intensity 

    print("Alter Wert:", bass_intensity)
    if bass_intensity > -3:
        bass_intensity -= 1
        print("Neuer Wert:", bass_intensity)
    else:
        print("Wert nicht verringert")
        

bass_decrease()
print("Wert nach Aufruf von bass_decrease:", bass_intensity)


def bass_print():
    print(f"Bass intensity: {bass_intensity}")

bass_print()

# --------------------------------------------


def numeric_input(min: int, max: int):

    def is_in_numeric_range(user_input: str) -> bool:
        return user_input.isnumeric() and int(user_input) >= min and int(user_input) <= max

    user_input = input("Eingabe: ")

    user_input_valid = is_in_numeric_range(user_input)

    if user_input_valid:
        return int(user_input)
    else:
        None

# print(numeric_input(5,10))


# --------------------------------------------

x = 0 # V1: Definition einer globalen Variable

def shadowing():
    x = 1 # V2: Definition als lokale Variable
    # print(x)

    def local_access():
        x = 2  # V3: Definition als lokale Variable
        x += 100
        print("78:", x)

    def global_access():
        global x
        x = 50
        print("83:", x)

    def non_local_access():
        nonlocal x
        x = 70
        print("88:", x)

    local_access()
    global_access()
    non_local_access()
    print("93:", x)


shadowing()
print("97:", x)