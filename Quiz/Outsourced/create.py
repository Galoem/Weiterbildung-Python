import random

def quiz_create_random_lang(aufgabenkatalog: list, aufgabenanzahl: int, name: str, ort: str) -> dict:
    if aufgabenanzahl > len(aufgabenkatalog):
        aufgabenanzahl = len(aufgabenkatalog)
    my_quiz = {"person": name, "location": ort, "tasks": [], "points": []}
    aufgabenkatalog_kopie = aufgabenkatalog.copy()
    aufgabenliste = []
    for _ in range(aufgabenanzahl):
        index_zufall = random.randint(0, len(aufgabenkatalog_kopie)-1)
        aufgabe = aufgabenkatalog_kopie.pop(index_zufall)
        aufgabenliste.append(aufgabe)
    my_quiz["tasks"] = aufgabenliste
    my_quiz["points"] = [0] * aufgabenanzahl
    return my_quiz   

def quiz_create_random(aufgabenkatalog: list, aufgabenanzahl: int, name: str, ort: str) -> dict:
    if aufgabenanzahl > len(aufgabenkatalog):
        aufgabenanzahl = len(aufgabenkatalog)
    my_quiz = {"person": name, "location": ort, "tasks": [], "points": []}
    my_quiz["tasks"] = random.sample(aufgabenkatalog, aufgabenanzahl)
    my_quiz["points"] = [0] * aufgabenanzahl
    return my_quiz   

def quiz_create_by_author_lang(aufgabenkatalog: list, aufgabenanzahl: int, autor: str, name: str, ort: str) -> dict:
    my_quiz = {"person": name, "location": ort, "tasks": [], "points": []}
    aufgabenkatalog_autor = []
    for aufgabe in aufgabenkatalog:
        if aufgabe["author"] == autor:
            aufgabenkatalog_autor.append(aufgabe)
    if aufgabenanzahl > len(aufgabenkatalog_autor):
        print(f"Info: Aufgabenanzahl von {aufgabenanzahl} auf {len(aufgabenkatalog_autor)} reduizert.")
        aufgabenanzahl = len(aufgabenkatalog_autor)
    my_quiz["tasks"] = random.sample(aufgabenkatalog_autor, aufgabenanzahl)
    # fülle die Liste der erreichten Punkte mit Nullen auf
    my_quiz["points"] = [0] * aufgabenanzahl
    return my_quiz  

def quiz_create_by_author(aufgabenkatalog: list, aufgabenanzahl: int, autor: str, name: str, ort: str) -> dict:
    aufgabenkatalog_autor = []
    for aufgabe in aufgabenkatalog:
        if aufgabe["author"] == autor:
            aufgabenkatalog_autor.append(aufgabe)
    return quiz_create_random(aufgabenkatalog_autor, aufgabenanzahl, name, ort)