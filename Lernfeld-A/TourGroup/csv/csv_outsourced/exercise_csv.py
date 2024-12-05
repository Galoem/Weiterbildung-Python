from plots import line_chart
from file_reader import read_csv_dict
from pprint import pprint

# Aufgaben CSV:

# 1. Lese die CSV Dateien Erwerbstaetige, Lohnentwicklung und Konsumentwicklung ein.
# 2. Entferne die Lehrzeichen in den Werten und wandle die Werte in Zahlen um.

print("\nAufgaben 1 & 2")

erwerbstaetige = read_csv_dict("../source_data/Erwerbstaetige.csv", ";")
lohnentwicklung = read_csv_dict("../source_data/Lohnentwicklung.csv", ";")
konsumentwicklung = read_csv_dict("../source_data/Konsumentwicklung.csv", ";")

# print("""
# ==========================
# ===== Erwerbstaetige =====
# ==========================
# """)
# pprint(erwerbstaetige)
# print("""
# ===========================
# ===== Lohnentwicklung =====
# ===========================
# """)
# pprint(lohnentwicklung)
# print("""
# =============================
# ===== Konsumentwicklung =====
# =============================
# """)
# pprint(konsumentwicklung)

# 3. Berechne die Steigerung in der Lohnentwicklung. (1970 = 100%)

print("\nAufgabe 3")

years_lohn = list(lohnentwicklung.keys())
years_lohn.sort()
BRUTTOLOEHNE = "Bruttoloehne"
BASE: dict = lohnentwicklung.get(years_lohn[0])
BASE_GROSS = BASE.get(BRUTTOLOEHNE)
lohnentwicklung_increase = dict()

for year in years_lohn:
    value: dict = lohnentwicklung.get(year)
    current_gross = value.get(BRUTTOLOEHNE)
    calc_increase = current_gross / BASE_GROSS * 100
    lohnentwicklung_increase.update({year: calc_increase})

# pprint(lohnentwicklung_increase)

# 4. Berechne die Veränderung des Brutto/ Netto- Verhältnisses in der Lohnentwicklung.

print("\nAufgabe 4")

NETTOLOEHNE = "Nettoloehne"
net_gross_ratio = dict()

for year in years_lohn:
    value: dict = lohnentwicklung.get(year)
    gross = value.get(BRUTTOLOEHNE)
    net = value.get(NETTOLOEHNE)
    ratio = net / gross * 100
    net_gross_ratio.update({year: ratio})

# pprint(net_gross_ratio)

# 5. Berechne das Verhältnis von Produktion und Dienstleistungen über die Zeitreihen.

print("\nAufgabe 5")

PROD_ALL = "ProdAll"
DIENST_ALL = "DienstAll"
prod_service_ratio = dict()

years_erwerb = list(erwerbstaetige.keys())
years_erwerb.sort()

for year in years_erwerb:
    value: dict = erwerbstaetige.get(year)
    prod = value.get(PROD_ALL)
    service = value.get(DIENST_ALL)
    prod_dienst_ratio = prod / service * 100
    prod_service_ratio.update({year: {"prod_dienst_ratio": prod_dienst_ratio, "ProdAll": prod, "DienstAll": service}})

# pprint(prod_service_ratio)

# 6. Berechne die Anteile der in der Landwirtschafts-, Forst-, Fischerei- Beschäftigten.

print("\nAufgabe 6")

LAND_FORST_FISCH = "LandForstFisch"
TOTAL = "Insgesamt"

land_forst_fisch_ratio = dict()

for year in years_erwerb:
    value: dict = erwerbstaetige.get(year)
    land_forst_fisch = value.get(LAND_FORST_FISCH)
    total = value.get(TOTAL)
    calc_land_forst_fisch_ratio = land_forst_fisch / total * 100
    land_forst_fisch_ratio.update({year: calc_land_forst_fisch_ratio})

# pprint(land_forst_fisch_ratio)

# 7. Berechne über die Zeitreihen die Anteile der Konsumposten an den Löhnen.

print("\nAufgabe 7")

TOTAL_KONSUM = "Insgesamt"
NETTO = "Nettolohn"
RATIO = "Ratio"

years_konsum = list(konsumentwicklung.keys())
years_lohn = list(lohnentwicklung.keys())
lohn_konsum_ratio = dict()

for year in years_konsum:
    value: dict = konsumentwicklung.get(year)
    total = value.get(TOTAL_KONSUM)
    lohn_konsum_ratio.update({year: {TOTAL_KONSUM: total}})
    
for year in years_lohn:
    value: dict = lohnentwicklung.get(year)
    net = value.get(NETTOLOEHNE)
    konsum_total_entry: dict = lohn_konsum_ratio.get(year)
    konsum_total_entry.update({NETTO: net})
    total_konsum = konsum_total_entry.get(TOTAL_KONSUM)
    konsum_total_entry.update({RATIO: total_konsum / net * 100})

pprint(lohn_konsum_ratio)

# 8. Berechne die Differenz von Löhnen und Konsum über die Zeitreihen.

DIFF = "Diff"

lohn_konsum_diff = dict()

for year in years_konsum:
    value: dict = konsumentwicklung.get(year)
    total = value.get(TOTAL_KONSUM)
    lohn_konsum_diff.update({year: {TOTAL_KONSUM: total}})
    
for year in years_lohn:
    value: dict = lohnentwicklung.get(year)
    net = value.get(NETTOLOEHNE)
    konsum_total_entry: dict = lohn_konsum_diff.get(year)
    konsum_total_entry.update({NETTO: net})
    total_konsum = konsum_total_entry.get(TOTAL_KONSUM)
    konsum_total_entry.update({DIFF: net - total_konsum})

# pprint(lohn_konsum_diff, width=30)

# 9. Zu den Aufgaben 3-8 stelle das Ergebnis in einem geigneten Diagramm aus der Matplotlib dar.

# Aufgabe 3
line_chart.create_plot(lohnentwicklung_increase, "Aufgabe 3: Salary increase from 1970 - 2022", "Years", "Salary")

# Aufgabe 4
line_chart.create_plot(net_gross_ratio, "Aufgabe 4: gross / net ratio from 1970 - 2022", "Years", "Ratio")
