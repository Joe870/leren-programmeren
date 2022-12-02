import random 
kaartenkleuren = ["harten","klaveren", "schoppen", "ruiten"]
kaartensoorten = ["aas","twee","drie","vier","vijf","zes","zeven","acht","negen","tien","boer","vrouw","heer"]
deck = []

for kleur in kaartenkleuren:
    for soort in kaartensoorten:
        deck.append(kleur + soort)
deck.insert(53,'joker 1')
deck.insert(53,'joker 2')
random.shuffle(deck) 
for x in range(1,7):
    print(deck.pop(0))


print(deck)