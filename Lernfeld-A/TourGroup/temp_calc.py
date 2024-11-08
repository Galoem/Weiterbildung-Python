fahrenheit = input("Please insert a temperature in °Fahrenheit: ")

if fahrenheit.isnumeric():
    celsius =  (float(fahrenheit) - 32) * 5 / 9
    print(f"{fahrenheit}°F equals {celsius:.2f}°C")
else:
    print(fahrenheit, "is not numeric")
