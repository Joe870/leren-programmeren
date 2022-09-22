omschrijving_croissantjes = "croissantjes"
aantal_croissantjes = 17
prijs_croissantjes = 0.39 
totale_prijs_croissantjes = aantal_croissantjes * prijs_croissantjes
omschrijving_stokbroden = "stokbroden"
aantal_stokbroden = 2
prijs_stokbroden = 2.78
totale_prijs_stokbroden = aantal_stokbroden * prijs_stokbroden 
omschrijving_kortingsbonnen = "kortingsbonnen"
aantal_kortingsbonnen = 3
prijs_kortingsbonnen = -0.50 
totale_prijs_kortingsbonnen = aantal_kortingsbonnen * prijs_kortingsbonnen 
print(f"{aantal_croissantjes} {omschrijving_croissantjes} {prijs_croissantjes}")
print(f"{aantal_stokbroden} {omschrijving_stokbroden} {prijs_stokbroden}")
print(totale_prijs_croissantjes + totale_prijs_stokbroden + totale_prijs_kortingsbonnen)
