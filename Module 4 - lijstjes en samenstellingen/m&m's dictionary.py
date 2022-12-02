from random import choice
kleuren = ["rood","blauw","groen","geel","bruin"]
aantal_mms = int(input('hoeveel mms moeten erbij?'))
mms = {} 
for mm in range(aantal_mms): 
    kleur = choice(kleuren)
    if kleur in mms:
        mms[kleur] += 1
    else:
        mms[kleur] = 1 
print(mms)