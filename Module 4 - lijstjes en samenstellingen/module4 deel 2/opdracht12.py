from fruitmand import fruitmand
nieuwe_fruitmand = {}
def myFunc(e):
    return len(e)
fruitmand.sort(reverse = True, key = lambda fruit:fruit['name'],key=myFunc) 
print(fruitmand)
nieuwe_fruitmand.update(fruitmand[0])
print(nieuwe_fruitmand)
kleur = nieuwe_fruitmand['color'] = 'oranje'
gewicht = nieuwe_fruitmand['weight'] / 1000
vrucht = nieuwe_fruitmand['name']
lengte_vrucht = len(nieuwe_fruitmand['name'])
print(f'de {vrucht}{lengte_vrucht} heeft een{kleur} en heeft een gewicht van {gewicht}')