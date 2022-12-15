from fruitmand import fruitmand
fruitmand.sort(reverse = True, key=lambda fruit:len(fruit['name']))
nieuwe_fruitmand = {}
print(fruitmand)
nieuwe_fruitmand.update(fruitmand[0])
print(nieuwe_fruitmand)
kleur = nieuwe_fruitmand['color'] = 'oranje'
gewicht = fruitmand[0]['weight'] / 1000
vrucht = nieuwe_fruitmand['name']
lengte_vrucht = len(nieuwe_fruitmand['name'])
print(f'de {vrucht} {lengte_vrucht} letters heeft een {kleur} kleur en heeft een gewicht van {gewicht} kg')