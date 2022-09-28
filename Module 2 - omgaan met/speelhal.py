aantal_personen = 4 
toegangsprijs = 7.45
prijs_gameseat = 0.37 
tijd_gameseat = 5 
totale_tijd_gameseat = 45
totale_tijd_gameseat_prijs = totale_tijd_gameseat / tijd_gameseat * prijs_gameseat
totale_toegangsprijs = aantal_personen * toegangsprijs 
totale_prijs_gameseat = totale_tijd_gameseat_prijs * aantal_personen 
totale_prijs = totale_toegangsprijs + totale_prijs_gameseat
print(totale_tijd_gameseat_prijs)  
print(totale_toegangsprijs)
print(totale_prijs_gameseat)
print(totale_prijs)
print(f'dit geweldige dagje-uit met {aantal_personen} mensen in de speelhal met {totale_tijd_gameseat} minuten VR kost je maar {totale_prijs} euro')
