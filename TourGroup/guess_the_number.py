from random import randint

MAX_ATTEMPTS = 5
NUMBER_RANGE_START = 1
NUMBER_RANGE_END = 10
NUMBER_RANGE = f"{NUMBER_RANGE_START} - {NUMBER_RANGE_END}"
SEARCHED_NUMBER = randint(NUMBER_RANGE_START, NUMBER_RANGE_END)
SEPARATOR = "========================================"

def user_has_attempts(guessed_numbers: list):
    return len(guessed_numbers) < MAX_ATTEMPTS

def guessed_number_is_correct(guessed_numbers: list):
    if len(guessed_numbers) == 0:
        return False
    return guessed_numbers[-1] == SEARCHED_NUMBER

def get_user_input(guessed_numbers: list):
    if len(guessed_numbers) > 0:
        print(f"The numbers you already guessed are: {guessed_numbers}.")
    print(f"The searched number is an integer in the range of {NUMBER_RANGE}.")
    user_input = input("Please insert your guess: ")
    return user_input

def validate_input(input: str):
    if not input.isnumeric():
        print(f"'{input}' is not a valid input. Please insert an integer.")
        return None
    number = int(user_input)
    if not (NUMBER_RANGE_START <= number <= NUMBER_RANGE_END):
        print(f"'{number}' is not in range of {NUMBER_RANGE}, please insert a number in that range.")
        return None
    if number in guessed_numbers:
        print(f"You already guessed {number}, please try another.")
        return None
    return number

def is_input_invalid(guessed_number: str):
    return guessed_number == None

def calculate_win(guessed_number: int):
    if guessed_number == SEARCHED_NUMBER:
        print(f"Congratulations, '{guessed_number}' was the searched number!")
        print(f"You needed {len(guessed_numbers)} attempts to guess the right number.")
    else:
        print(f"'{guessed_number}' was not the searched number.")
        print(f"The searched number is {"higher" if guessed_number < SEARCHED_NUMBER else "lower"} than your guess.")

print(SEPARATOR)
print("Welcome to guess the number!")
print(f"You have {MAX_ATTEMPTS} attempts to guess the number.")
print("If you did not guess the right number, you will receive a hint, whether the correct number is higher or lower than your guess.")
print("Lets begin!")

guessed_numbers = []

while user_has_attempts(guessed_numbers) and not guessed_number_is_correct(guessed_numbers):
    print(SEPARATOR)
    user_input = get_user_input(guessed_numbers)
    guessed_number = validate_input(user_input)
    if is_input_invalid(guessed_number):
        continue
    print(f"You guessed '{guessed_number}'.")
    guessed_numbers.append(guessed_number)
    calculate_win(guessed_number)

if not guessed_number_is_correct:
    print(f"Sorry, but you did not guess the number in time, the searched number was {SEARCHED_NUMBER}.")
    print("Better luck next time, bye!")

print(SEPARATOR)
