drinks = ["CocaCola", "Fanta,", "Sprite", "Wasser", "Iced Coffee", "Dr. Pepper", "Caprisun", "Root Beer"]

print(f"\nDrinks:")
for index, drink in enumerate(drinks):
    print(f"\t{index + 1}: {drink}")

input = int(input(f"\nPlease insert a number: "))

print(f"\nYou pressed {input}...")
if input > len(drinks) or input <= 0:
    print(f"The specified compartment is empty or is not being used.")
else:
    print(f"A can of {drinks[input - 1]} fell into the output chute.")

print("")