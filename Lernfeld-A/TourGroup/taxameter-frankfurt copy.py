# Taxitarif Frankfurt
# Grundgebühr: 4,- EUR
# Kilometerpreis: 2,40 EUR

BASE_PRICE = 4.00
PRICE_PER_KILOMETER = 2.40
PROMO_PER_KILOMETER = 2.00

kilometers = input("How far do you want to drive in km: ")

if kilometers.isnumeric:
    
    if kilometers >= 10:
        total = BASE_PRICE + PROMO_PER_KILOMETER * float(kilometers)
    else:
        total = BASE_PRICE + PRICE_PER_KILOMETER * float(kilometers)
    
    print(f"The total price for this trip will be {total:.2f} EUR")
else:
    print(f"{kilometers} is not numeric")
