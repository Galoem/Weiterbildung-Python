import terminal

def question_print(frage: dict) -> None:
    print(frage["question"])
    answers = frage["answers"]
    for index, answer in enumerate(answers):
        print(f"{index+1}) {answer}")

def question_solve(frage: dict) -> bool:
    question_print(frage)
    antwort_ist_valide = False
    while antwort_ist_valide == False:
        eingabe = input("Bitte wählen: ")
        antwort_ist_valide = eingabe.isnumeric() and int(eingabe) > 0 and int(eingabe) <= len(frage["answers"])
        if not antwort_ist_valide:
            print("Eingabe fehlerhaft!")
    eingabe_num = int(eingabe)
    return eingabe_num == frage["correct_answer"]

def task_solve(aufgabe: dict) -> int:
    terminal.clear()
    punkte = 0
    for frage in aufgabe["questions"]:
        print(f"Aufgabe: {aufgabe["title"]}")
        punkte += question_solve(frage)
        terminal.clear()
    return punkte

def quiz_solve(quiz: dict) -> None:
    for index, task in enumerate(quiz["tasks"]):
        erreichten_punkte = task_solve(task)
        quiz["points"][index] = erreichten_punkte
