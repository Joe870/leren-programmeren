# Joëlle van Breugel opdracht pizza calculator
afmeting_pizza_1 = "afmeting small" 
print(afmeting_pizza_1)
try:
    prijs_small_1 = float(input(f'wat is de prijs?'))
except if prijs_small_1 == int:
    print('dit klopt niet')
else: print('dit klopt') 

print(prijs_small_1)
prijs_small_totaal = prijs_small_1 * aantal_pizza_1 
afmeting_pizza_2 = "afmeting medium"
print(afmeting_pizza_2)
prijs_medium_1 = 6
aantal_pizza_2 = int(input("aantal:")) 
print(prijs_medium_1) 
afmeting_pizza_3 = "afmeting large"
prijs_medium_totaal = prijs_medium_1 * aantal_pizza_2 
print(afmeting_pizza_3)
aantal_pizza_3 = int(input("aantal:"))
prijs_large_1 = 12  
print(prijs_large_1) 
prijs_large_totaal = prijs_large_1 * aantal_pizza_3 
totale_prijs = prijs_large_totaal + prijs_medium_totaal + prijs_small_totaal
print(totale_prijs) 