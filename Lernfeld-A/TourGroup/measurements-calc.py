distance = input("Please insert a distance: ")
intDistance = None

if distance.isnumeric():
    intDistance = float(distance)
else:
    print(f"'{distance}' is not a number")
    exit(-1)

unit = input("Please insert a unit ('in' for inches, 'ft' for feet, 'yd' for yards, 'm' for miles): ")

resultUnit = None

match unit:
    case "in":
        result = intDistance * 2.54
        resultUnit = "cm"
    case "ft":
        result = intDistance * 0.3048
        resultUnit = "m"
    case "yd":
        result = intDistance * 0.914
        resultUnit = "m"
    case "m":
        result = intDistance * 1.609344
        resultUnit = "km"
    case _:
        print(f"'{unit}' is not a supported unit")
        exit(-1)

print(f"{intDistance} in {unit} equals {result} in {resultUnit}")
