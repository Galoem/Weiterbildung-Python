import csv
from pprint import pprint

question1 = {
    "question": "which syntax is incorrect?",
    "answers": {
        1: "sum(1,2,3)",
        2: "sum((1,2,3,4))",
        3: "sum({1,2,3,4})"
    },
    "correct_answer": 1,
    "author": "MARIA_HILBERT",
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
    "author": "MARIA_HILBERT",
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
    "author": "JOHAN_MUELLER",
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
    "author": "JOHAN_MUELLER",
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
    "author": "MARIA_HILBERT",
    "points": 1
}
question6 = {
    "question": "Welche Antwort konkateniert zwei Listen?",
    "answers": {
        "[1,2,3] + [4,5,6]",
        "[1,2,3] and [4,5,6]"
    },
    "correct_answer": 1,
    "author": "MARIA_HILBERT",
    "points": 1
}
question7 = { 
    "question": "Welcher Funktionskopf ist gültig?", 
    "answers": {
        "def my_function():", 
        "fct my_method():", 
        "int my_function(void)" 
    },
    "correct_answer": 1, 
    "author": "JOHAN_MUELLER",
    "points": 1
}
question8 = { 
    "question": "Benötigt eine Funktion immer ein Return Statement?", 
    "answers": {
        1: "ja", 
        2: "nein"
    },
    "correct_answer": 2,
    "author": "JOHAN_MUELLER",
    "points": 1
}

quiz = [question1, question2, question3, question4, question5, question6, question7, question8]

with open("output.csv", mode="w", newline="") as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=["question", "answers", "correct_answer", "author", "points"])
    csv_writer.writeheader()
    csv_writer.writerows(quiz)
