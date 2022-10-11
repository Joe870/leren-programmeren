# Joëlle van Breugel opdracht pizza calculator
afmeting_pizza_1 = "afmeting small" 
print(afmeting_pizza_1)
prijs_small_1 = 3 
while True:
    try: 
        aantal_small_1 = int(input(f'wat is het aantal?'))
        break 
    except:print('dit is geen getal')
prijs_small_totaal = prijs_small_1 * aantal_small_1 
print(prijs_small_totaal) 
afmeting_pizza_2 = "afmeting medium"
prijs_medium_1 = 6
print(afmeting_pizza_2)
while True:
    try:
        aantal_medium_1 = float(input(f'wat is het aantal?'))
        break
    except:print('dit klopt niet')
prijs_medium_totaal = prijs_medium_1 * aantal_medium_1 
print(prijs_medium_totaal) 
afmeting_pizza_3 = "afmeting large"
prijs_large_1 = 12 
print(afmeting_pizza_3)
while True:
    try:
        aantal_large_3 = float(input(f'wat is de prijs?'))
        break 
    except: print('dit klopt niet')
prijs_large_totaal = prijs_large_1 * aantal_large_3 
print(prijs_large_totaal) 
totale_prijs = prijs_large_totaal + prijs_medium_totaal + prijs_small_totaal
print(totale_prijs) 