lengte_zwembad = float(8.0)
breedte_zwembad = float(3.0)
diepte_zwembad = float(1.5) 
inhoud_zwembad = lengte_zwembad * breedte_zwembad * diepte_zwembad
print(inhoud_zwembad) 
uitgraafkosten_1 = float(25.0)
afvoergrondkosten_1 = float(32.50)
uitgraafkosten_2 = uitgraafkosten_1 * inhoud_zwembad
afvoergrondkosten_2 = afvoergrondkosten_1 * inhoud_zwembad 
totaal_kosten = afvoergrondkosten_2 + uitgraafkosten_2
print(f" offerte voor een zwembad van 8 bij 3 bij 1,5 meter inhoud: {inhoud_zwembad}")
print(f" uitgraven: {uitgraafkosten_2}") 
print(f" afvoeren grond: {afvoergrondkosten_2}")
print(f"totaal : {totaal_kosten}") 