lengte_zwembad = float(input('wat is de lengte van het zwembad'))
breedte_zwembad = float(input('wat is de breedte van het zwembad'))
diepte_zwembad = float(input('wat is de diepte van het zwembad'))
kilometers = float(input('hoeveel kilometers'))
inhoud_zwembad = lengte_zwembad * breedte_zwembad * diepte_zwembad
print(inhoud_zwembad) 
uitgraafkosten_1 = 25.00
afvoergrondkosten_1 = 32.50
uitgraafkosten_2 = uitgraafkosten_1 * inhoud_zwembad
afvoergrondkosten_2 = afvoergrondkosten_1 * inhoud_zwembad 
totaal_kosten = afvoergrondkosten_2 + uitgraafkosten_2
if kilometers <50 and inhoud_zwembad <20:
    voorrijkosten_vast = 100.0
    voorrijkosten_variabel = 1.25
if kilometers >50 and inhoud_zwembad <20: 
    voorrijkosten_vast = 100.0
    voorrijkosten_variabel = 1.15
if kilometers <50 and inhoud_zwembad >20:
    voorrijkosten_vast = 250.0
    voorrijkosten_variabel = 2.15 
if kilometers >50 and inhoud_zwembad >20:
    voorrijkosten_vast = 250
    voorrijkosten_variabel = 2.05
vierkante_meter = lengte_zwembad * breedte_zwembad + breedte_zwembad * diepte_zwembad * 2 + lengte_zwembad * diepte_zwembad * 2 
tegels = input('welke tegels wilt u in uw zwembad? a = rood en b = kleur')
if tegels == 'a' and inhoud_zwembad <20.0:
    prijs_beton_tegels = 250.0
    prijs_tegels = 25.0
if tegels == 'a' and inhoud_zwembad >20.0:
    prijs_beton_tegels = 200.0
    prijs_tegels = 20.0 
if tegels == 'b' and inhoud_zwembad <20.0: 
    prijs_beton_tegels = 250.0
    prijs_tegels = 100.0
if tegels == 'b' and inhoud_zwembad >20.0:
    prijs_beton_tegels = 200.0
    prijs_tegels = 125.0
voorrijkosten_defenitief = voorrijkosten_variabel * kilometers + voorrijkosten_vast
if tegels == 'a':
    prijs_afwerking = prijs_beton_tegels * vierkante_meter + prijs_tegels * vierkante_meter
if tegels == 'b':
    prijs_afwerking = prijs_beton_tegels * vierkante_meter + prijs_tegels
print(prijs_afwerking)
print(vierkante_meter) 
print(f"offerte voor een zwembad van {lengte_zwembad} bij {breedte_zwembad} bij {diepte_zwembad} meter inhoud: {inhoud_zwembad}")
print(f"uitgraven: {uitgraafkosten_2}") 
print(f"afvoeren grond: {afvoergrondkosten_2}")
print(f"totaal: {totaal_kosten}") 
print(f"voorrijkosten: {voorrijkosten_defenitief}") 
print(f"beton + tegels {vierkante_meter}: {prijs_afwerking}") 

