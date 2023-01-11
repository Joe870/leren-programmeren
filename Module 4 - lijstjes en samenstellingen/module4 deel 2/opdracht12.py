from fruitmand import fruitmand
fruitmand.sort(reverse = True, key=lambda fruit:len(fruit['name']))
print(f'de {fruitmand[0]["color"]} {len(fruitmand[0]["name"])} letters heeft een {fruitmand[0]["color"]} kleur en heeft een gewicht van {fruitmand[0]["weight"] / 1000}')