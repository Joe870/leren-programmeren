aantal_personen = input("aantal_personen") 
aantal_personen = int(aantal_personen) 
toegangsprijs = input("toegangsprijs") 
toegangsprijs = float(toegangsprijs)
prijs_gameseat = input("prijs_gameseat") 
prijs_gameseat = float(prijs_gameseat) 
tijd_gameseat = input("tijd_gameseat")
tijd_gameseat = int(tijd_gameseat)  
totale_toegangsprijs = toegangsprijs * aantal_personen 
print(totale_toegangsprijs) 
totale_tijd_gameseat = input("totale_tijd_gameseat") 
totale_tijd_gameseat = int(totale_tijd_gameseat)  
totale_tijd_gameseat_berekening = totale_tijd_gameseat / tijd_gameseat
totale_prijs_gameseat_1 = totale_tijd_gameseat_berekening * prijs_gameseat 
totale_prijs_gameseat_2 = totale_prijs_gameseat_1 * aantal_personen 
print(totale_prijs_gameseat_2) 
totale_prijs = totale_prijs_gameseat_2 + totale_toegangsprijs 
print(f'dit geweldige dagje-uit met {aantal_personen} mensen in de speelhal met {totale_tijd_gameseat} minuten VR kost je maar {totale_prijs} euro')



