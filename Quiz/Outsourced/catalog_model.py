def get_catalog() -> list:
    question1 = {"question": "Welcher Aufruf ist falsch?", "correct_answer": 1, "answers": ["sum(1,2,3)", "sum((1,2,3,4))", "sum({1,2,3,4})"]}
    question2 = {"question": "Welche Antwort liefert den groessten Zahlenwert?", "correct_answer": 3, "answers": ["max([2,4,6])", "sorted([1,10,3,4])[-1]", "abs(min([-12,-4,-2,-1]))"]}
    task1 = {"author": "Maria Hilbert", "title": "Built-In-Funktionen", "competence": "Funktionen", "questions": [question1, question2 ]}

    question3 = {"question" : "Welcher Variablenname ist gültig?", "correct_answer": 3, "answers": ["kapital-neu", "5zinssatz", "motor_klein"]}
    question4 = {"question": "Welcher Variablenname ist ungültig?", "correct_answer": 1, "answers": ["ist-wert", "_istwert", "ist_wert"]}
    task2 = {"author": "Johan Müller", "title": "Variablennamen", "competence": "Syntax", "questions": [question3, question4]}

    question5 = {"question": "Welchen Index hat E in folgender Liste: liste = [A,B,C,D,E,F,G,H]?", "correct_answer": 2, "answers": ["3" , "4" , "5"]}
    question6 = {"question": "Welche Antwort konkateniert zwei Listen?", "correct_answer": 1, "answers": ["[1,2,3] + [4,5,6]", "[1,2,3] and [4,5,6]"]}
    task3 = {"author": "Maria Hilbert", "title": "Arbeiten mit Listen", "competence": "Listen", "questions": [question5, question6]}

    question7 = {"question": "Welcher Funktionskopf ist gültig?", "correct_answer": 1, "answers": ["def my_function():", "fct my_method():", "int my_function(void)"]}
    question8 = {"question": "Benötigt eine Funktion immer ein Return Statement?", "correct_answer": 2, "answers": ["ja", "nein"] }
    task4 = {"author": "Johan Müller", "title": "Funktionsdefinition",  "competence": "Funktionen", "questions": [question7, question8]}

    catalog = [task1, task2, task3, task4]

    return catalog
