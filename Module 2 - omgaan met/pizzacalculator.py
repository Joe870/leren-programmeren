
afmeting_pizza_1 = "afmeting small" 
print(afmeting_pizza_1)
prijs_small_1 = 3 
aantal_pizza_1 = int(input("aantal:"))  
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