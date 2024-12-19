# from pprint import pprint # pretty print
import os

# save for later usage
# task1 = { "author" : "Maria Hilbert", "title" : "Built-In-Funktionen", "competence": "Funktionen", "questions" : [ question1, question2 ] }
# task2 = { "author": "Johan Müller", "title": "Variablennamen", "competence": "Syntax", "questions": [ question3, question4 ] }
# task3 = { "author" : "Maria Hilbert", "title": "Arbeiten mit Listen", "competence": "Listen", "questions": [ question5, question6 ] }
# task4 = { "author" : "Johan Müller", "title" : "Funktionsdefinition",  "competence" : "Funktionen", "questions" : [ question7, question8 ] }
# catalog = [ task1, task2, task3, task4 ]

AUTHOR_MARIA_HILBERT = "Maria Hilbert"
AUTHOR_JOHAN_MUELLER = "Johan Müller"

question1 = {
    "question": "which syntax is incorrect?",
    "answers": {
        1: "sum(1,2,3)",
        2: "sum((1,2,3,4))",
        3: "sum({1,2,3,4})"
    },
    "correct_answer": 1,
    "author": AUTHOR_MARIA_HILBERT,
    "points": 2
}
question2 = {
    "question": "What returns the greatest number?",
    "answers": {
        1: "max([2,4,6])",
        2: "sorted(1,10,4,6)[-1]",
        3: "abs(min(-12,-4,-7,-5))"
    },
    "correct_answer": 3,
    "author": AUTHOR_MARIA_HILBERT,
    "points": 3
}
question3 = { 
    "question" : "Welcher Variablenname ist gültig?",
    "answers": {
        1: "kapital-neu",
        2: "5zinssatz",
        3: "motor_klein"
    },
    "correct_answer": 3,
    "author": AUTHOR_JOHAN_MUELLER,
    "points": 1
}
question4 = { 
    "question" : "Welcher Variablenname ist ungültig?",
    "answers": {
        1: "ist-wert",
        2: "_istwert",
        3: "ist_wert"
    },
    "correct_answer": 1,
    "author": AUTHOR_JOHAN_MUELLER,
    "points": 1
}
question5 = { 
    "question": "Welchen Index hat E in folgender Liste: liste = [A,B,C,D,E,F,G,H]?",
    "answers": {
        1: "3", 
        2: "4",
        3: "5"
    },
    "correct_answer": 2,
    "author": AUTHOR_MARIA_HILBERT,
    "points": 1
}
question6 = {
    "question": "Welche Antwort konkateniert zwei Listen?",
    "answers": {
        1: "[1,2,3] + [4,5,6]",
        2: "[1,2,3] and [4,5,6]"
    },
    "correct_answer": 1,
    "author": AUTHOR_MARIA_HILBERT,
    "points": 1
}
question7 = { 
    "question": "Welcher Funktionskopf ist gültig?", 
    "answers": {
        1: "def my_function():", 
        2: "fct my_method():", 
        3: "int my_function(void)" 
    },
    "correct_answer": 1, 
    "author": AUTHOR_JOHAN_MUELLER,
    "points": 1
}
question8 = { 
    "question": "Benötigt eine Funktion immer ein Return Statement?", 
    "answers": {
        1: "ja", 
        2: "nein"
    },
    "correct_answer": 2,
    "author": AUTHOR_JOHAN_MUELLER,
    "points": 1
}

quiz = {
    "quizzee": "",
    "questions": [question1, question2, question3, question4, question5, question6, question7, question8],
    "points_total": 0,
    "points_reached": 0
}

def clear():
    print("\n==============================\n")
    input("Press Enter to continue... ")
    os.system("cls" if os.name == "nt" else "clear")

def get_questions() -> dict:
    return quiz.get("questions")

def get_answers(question: dict) -> dict:
    return question.get("answers")

def get_correct_answer(question: dict) -> str:
    answers = get_answers(question)
    correct_answer = question.get("correct_answer")
    return f"{correct_answer} -> {answers.get(correct_answer)}"

def print_question(question: dict) -> None:
    print(question.get("question"))
    answers = question.get("answers")
    for key, answer in answers.items():
        print("\t", key, "->", answer)

def create_question(question: str, answers: tuple[int, str], correct_answer: list[int], author: str, points: int) -> None:
    question = {
        "question": question,
        "answers": answers,
        "correct_answer": correct_answer,
        "author": author,
        "points": points
    }
    questions = get_questions()
    questions.append(question)

def is_valid_number(user_input: int, answers: dict) -> bool:
    valid_answers: list = answers.keys()
    return user_input in valid_answers

def get_valid_answer(question: dict) -> int:
    is_answer_valid = False
    while not is_answer_valid:
        user_input = input("Please insert your answer: ")
        if user_input.isnumeric() and is_valid_number(int(user_input), get_answers(question)):
            is_answer_valid = True
        elif not user_input.isnumeric():
            print(f"{user_input} is not a number.")
        elif not is_valid_number(user_input, question):
            print(f"There is no answer of number {user_input}.")
    return int(user_input)

def get_total_points(quiz: dict) -> int:
    return quiz.get("points_total")

def get_current_points(quiz: dict) -> int:
    return quiz.get("points_reached")

def validate_answer(quiz: dict, question: dict, user_answer: dict, correct_answer: int) -> None:
    if correct_answer == user_answer:
        points_from_question = question.get("points")
        quiz.update({"points_reached": get_current_points(quiz) + points_from_question})
        print(f"Your answer was correct!\nYou received {points_from_question} points.")
    else:
        print(f"Your answer was not correct, the correct answer would have been: {correct_answer}")

print("""
==================
=== Start quiz ===
==================
""")
print("Hello Quizzee!")
quizzee_name = input("Please enter your name: ")

quiz.update({"quizzee": quizzee_name if quizzee_name != "" else "Quizzee"})
print(f"""
Welcome {quiz.get("quizzee")}.
Then let us begin!""")
questions= get_questions()

for question in questions:
    question: dict
    clear()
    print_question(question)
    answer = get_valid_answer(question)
    print("====================")
    correct_answer = question.get("correct_answer")
    validate_answer(quiz, question, answer, correct_answer)
    print(f"Current points: {get_current_points(quiz)}.")
    quiz.update({"points_total": get_total_points(quiz) + question.get("points")})
    print(f"Total Points reachable so far: {get_total_points(quiz)}.")

clear()
print(f"Congratulations {quizzee_name}, you finished the quiz and reached {get_current_points(quiz)} of {get_total_points(quiz)} points!")
print(f"That equals {(get_current_points(quiz) / get_total_points(quiz) * 100):.0f}% of total points!")
