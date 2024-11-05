mph = input("Please insert a speed in mp/h: ")

if mph.isnumeric:
    kmh = float(mph) * 1.609344
    print(mph, "mp/h equals", round(kmh, 2), "km/h")
else:
    print(mph, "is not a number")
