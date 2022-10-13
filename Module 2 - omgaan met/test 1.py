lengte_zwembad = float(input('wat is de lengte van het zwembad'))
breedte_zwembad = float(input('wat is de breedte van het zwembad'))
diepte_zwembad = float(input('wat is de diepte van het zwembad'))
voorrijkosten_vast = float(250.00)
voorrijkosten_variabel = float(2.05) 
kilometers = float(input('hoeveel kilometers'))
voorrijkosten_defenitief = voorrijkosten_variabel * kilometers + voorrijkosten_vast
inhoud_zwembad = lengte_zwembad * breedte_zwembad * diepte_zwembad
print(inhoud_zwembad) 
uitgraafkosten_1 = float(25.00)
afvoergrondkosten_1 = float(32.50)
uitgraafkosten_2 = uitgraafkosten_1 * inhoud_zwembad
afvoergrondkosten_2 = afvoergrondkosten_1 * inhoud_zwembad 
totaal_kosten = afvoergrondkosten_2 + uitgraafkosten_2
if kilometers <50 and inhoud_zwembad 
if inhoud_zwembad >20.0:
    prijs_beton_tegels = float(250.0)
    prijs_rode_tegels = float(25.0) 
    prijs_kleur_tegels = float(125.0) 
if inhoud_zwembad <20.0:
    prijs_beton_tegels = float(200.0)
    prijs_rode_tegels = float(20.0)
    prijs_kleur_tegels = float(125.0)
vierkante_meter = lengte_zwembad * breedte_zwembad 
prijs_afwerking = prijs_beton_tegels * vierkante_meter + prijs_rode_tegels * vierkante_meter + prijs_kleur_tegels 
print(vierkante_meter) 
print(f"offerte voor een zwembad van {lengte_zwembad} bij {breedte_zwembad} bij {diepte_zwembad} meter inhoud: {inhoud_zwembad}")
print(f"uitgraven: {uitgraafkosten_2}") 
print(f"afvoeren grond: {afvoergrondkosten_2}")
print(f"totaal: {totaal_kosten}") 
print(f"voorrijkosten: {voorrijkosten_defenitief}") 
print(f"beton + tegel {prijs_afwerking}") 
