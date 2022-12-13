from fruitmand import fruitmand
fruitmand.insert(7, {})
fruitmand[7]['name'] = 'watermeloen'
fruitmand[7]['weight'] = 1204
fruitmand[7]['color'] = 'green' 
fruitmand[7]['round'] = True 
totaal_gewicht = 0 
for fruit in fruitmand:
    som_gewicht = fruit['weight']
    totaal_gewicht += som_gewicht 
print(totaal_gewicht)
