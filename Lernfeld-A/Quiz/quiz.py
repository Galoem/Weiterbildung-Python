from pprint import pprint # pretty print

AUTHOR_MARIA_HILBERT = "Maria Hilbert"

q1 = {
    "question": "which syntax is incorrect?",
    "answers": {
        1: "sum(1,2,3)",
        2: "sum((1,2,3,4))",
        3: "sum({1,2,3,4})"
    },
    "correct_answers": [1],
    "author": AUTHOR_MARIA_HILBERT,
    "points": 2
}
q2 = {
    "question": "What returns the greatest number?",
    "answers": {
        1: "max([2,4,6])",
        2: "sorted(1,10,4,6)[-1]",
        3: "abs(min(-12,-4,-7,-5))"
    },
    "correct_answers": [3],
    "author": AUTHOR_MARIA_HILBERT,
    "points": 2
}

quiz = {
    "quizzee": "",
    "questions": [q1, q2],
    "points_total": 0,
    "points_reached": 0
}

def get_questions() -> dict:
    return quiz.get("questions")

def print_question(question: dict) -> None:
    print(question.get("question"))
    answers = question.get("answers")
    for key, answer in answers.items():
        print("\t", key, "->", answer)


def create_question(question: str, answers: tuple[int, str], correct_answers: list[int], author: str, points: int) -> None:
    question = {
        "question": question,
        "answers": answers,
        "correct_answer": correct_answers,
        "author": author,
        "points": points
    }
    questions = get_questions()
    questions.append()

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
    print_question(question)
    # await answer
    # validate answer
    # get points
