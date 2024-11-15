from random import randint



attempts = 5

print("========================================")
print("Welcome to guess the number!")
print(f"You have {attempts} attempts to guess the number.")
print("If you did not guess the right number, you will receive a hint, whether the correct number is higher or lower than your guess.")
print("Lets begin!")

NUMBER_RANGE_START = 1
NUMBER_RANGE_END = 10
NUMBER_RANGE = f"{NUMBER_RANGE_START} - {NUMBER_RANGE_END}"
SEARCHED_NUMBER = randint(NUMBER_RANGE_START, NUMBER_RANGE_END)
guessed_numbers = []

while len(guessed_numbers) < 5:
    print("========================================")

    if len(guessed_numbers) > 0:
        print(f"The numbers you already guessed are: {guessed_numbers}.")
    print(f"The searched number is an integer in the range of {NUMBER_RANGE}.")
    user_input = input("Please insert your guess: ")

    if not user_input.isnumeric():
        print(f"'{user_input}' is not a valid input. Please insert an integer.")
        continue

    guessed_number = int(user_input)

    if not (NUMBER_RANGE_START <= guessed_number <= NUMBER_RANGE_END):
        print(f"'{guessed_number}' is not in range of {NUMBER_RANGE}, please insert a number in that range.")
        continue

    if guessed_number in guessed_numbers:
        print(f"You already guessed {guessed_number}, please try another.")
        continue
    
    print(f"You guessed '{guessed_number}'.")
    guessed_numbers.append(guessed_number)

    if guessed_number == SEARCHED_NUMBER:
        print(f"Congratulations, '{guessed_number}' was the searched number!")
        exit(0)
    else:
        print(f"'{guessed_number}' was not the searched number.")
        print(f"The searched number is {"higher" if guessed_number < SEARCHED_NUMBER else "lower"} than your guess.")

print(f"Sorry, but you did not guess the number in time, the searched number was {SEARCHED_NUMBER}.")
print("Better luck next time, bye!")