from random import choice 
kleuren = ("oranje", "blauw", "groen", "bruin")
aantal_mms = (input('hoeveel m&ms moeten er aan de zak worden toegevoegd?'))
mms = [] 
for mm in range(aantal_mms):
    kleur = choice(kleuren)
    mms.append(kleur)
print(mms)
