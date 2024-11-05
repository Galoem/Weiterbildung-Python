weight = input("Please insert a weight in lbs: ")

if weight.isnumeric():
    kilos = float(weight) * 0.45359237
    print(f"{weight} lbs equal {round(kilos, 2)} kg")
else:
    print(f"{weight} is not numeric")
