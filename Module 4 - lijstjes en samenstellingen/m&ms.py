from random import choice 
from random import randint
kleur = ("oranje", "blauw", "groen", "bruin")
aantal_mms = int(input('hoeveel m&ms moeten er aan de zak worden toegevoegd?'))
list = [] 
while aantal_mms > 0:
    aantal_kleur = choice(kleur)
    aantal_mms2 = randint(aantal_mms)
    aantal_mms2 - aantal_mms
    aantal_kleur += aantal_mms
print(aantal_kleur)
print(aantal_mms)
list.append(aantal_mms)
print(list)
list.extend(tuple)
print(list)
print(kleur)