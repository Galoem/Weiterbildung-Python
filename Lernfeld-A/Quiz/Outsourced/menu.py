import terminal
import create
import solve

def quiz_evaluate(quiz: dict) -> None:
    print(f"Auswertung für {quiz["person"]} aus {quiz["location"]}")
    gesamt_punkte_erreichbar = 0
    for index, task in enumerate(quiz["tasks"]):
        punkte_erreichbar = len(task["questions"])
        punkte_erreicht = quiz["points"][index]
        print(f"Aufgabe {index+1}: {punkte_erreicht} / {punkte_erreichbar} Punkte")
        gesamt_punkte_erreichbar += punkte_erreichbar
    gesamt_punkte_erreicht = sum(quiz["points"])
    print(f"Gesamt: {gesamt_punkte_erreicht} / {gesamt_punkte_erreichbar} Punkte erreicht")

def author_select(katalog: list) -> str:
    autoren = set()
    for aufgabe in katalog:
        autoren.add(aufgabe["author"])
    autoren_sortiert = sorted(autoren)
    for index, autor in enumerate(autoren_sortiert):
        print(f"{index+1}. {autor}")
    position = int(input("Autor wählen: "))
    return autoren_sortiert[position - 1]

def get_user_info(katalog: list) -> tuple[str, str, int]:
    name = input("Wie heißt du: ")
    ort = input("Wo bist du gerade: ")
    aufgabenanzahl = None
    while aufgabenanzahl is None:
        aufgabenanzahl_str = input(f"Wie viele Aufgaben möchtest du bearbeiten (max: {len(katalog)}): ")
        if not aufgabenanzahl_str.isnumeric():
            print(f"'{aufgabenanzahl_str}' is not a number.")
        elif int(aufgabenanzahl_str) not in range(1, len(katalog)) :
            print(f"'{aufgabenanzahl_str}' must be in range of 1 and {len(katalog)}.")
        else:
            aufgabenanzahl = int(aufgabenanzahl_str)
    return name, ort, int(aufgabenanzahl)

def is_game_mode_valid(game_mode):
    return game_mode in ["a", "b", "x"]

def start_quiz(katalog: list):
    terminal.clear()
    name, ort, aufgabenanzahl = get_user_info(katalog)
    game_mode = ""
    while not is_game_mode_valid(game_mode):
        game_mode = input("Wähle a) Zufällige Aufgaben, b) Aufgabenautor wählen, x) schließen: ")
        if not is_game_mode_valid(game_mode):
            print(f"Game mode '{game_mode}' wird nicht unterstützt!")
        
    match game_mode:
        case "a":
            quiz_random = create.quiz_create_random(katalog, aufgabenanzahl, name, ort)
            solve.quiz_solve(quiz_random)
            quiz_evaluate(quiz_random)
        case "b":
            aufgabenautor = author_select(katalog)
            quiz_random = create.quiz_create_by_author(katalog, aufgabenanzahl, aufgabenautor, name, ort)
            solve.quiz_solve(quiz_random)
            quiz_evaluate(quiz_random)
        case "x":
            print("Danke fürs Spielen, bis bald!")

