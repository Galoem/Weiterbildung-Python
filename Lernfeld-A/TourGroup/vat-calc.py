netValue = input("Please insert your amount in $: ").replace(",", ".")
vatValue = input("Please insert your vat in %: ").replace(",", ".")

if netValue.isnumeric and vatValue.isnumeric:
    netFloatValue = float(netValue)
    vatFloatValue = float(vatValue)
    grossValue = round(netFloatValue * (1 + vatFloatValue / 100), 2)
    print((f"net costs of ${netFloatValue} with vat of {vatFloatValue}% equals ${grossValue} gross").replace(".", ","))
else:
    print(f"net value '{netValue}' and/or vat value '{vatValue}' is not numeric")