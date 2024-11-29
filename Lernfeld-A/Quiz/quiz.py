from pprint import pprint # pretty print

AUTHOR_MARIA_HILBERT = "Maria Hilbert"

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

quiz = {
    "quizzee": "",
    "questions": [question1, question2],
    "points_total": 0,
    "points_reached": 0
}

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
    questions.append()

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

# pprint(quiz)

print("""
==================
=== Start quiz ===
==================
""")
print("Hello Quizzee!")
quizzee_name = ""
# quizzee_name = input("Please insert your name: ")

quiz.update({"quizzee": quizzee_name if quizzee_name != "" else "Quizzee"})
print(f"""
Welcome {quiz.get("quizzee")}.
Then let us begin!
""")
questions= get_questions()

for question in questions:
    question: dict
    print("====================")
    print_question(question)
    answer = get_valid_answer(question)
    print("====================")
    correct_answer = question.get("correct_answer")
    validate_answer(quiz, question, answer, correct_answer)
    print(f"Current points: {get_current_points(quiz)}.")
    quiz.update({"points_total": get_total_points(quiz) + question.get("points")})
    print(f"Total Points reachable so far: {get_total_points(quiz)}.")

print(f"You finished the quiz and reached {get_current_points(quiz)} of {get_total_points(quiz)} points.")
print(f"That equals {(get_current_points(quiz) / get_total_points(quiz) * 100):.0f}% of total points.")