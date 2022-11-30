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
kaart_1 = deck.pop(1)
print(f'kaart 1 = {kaart_1}')
kaart_2 = deck.pop(2)
print(f'kaart 2 = {kaart_2}')
kaart_3 = deck.pop(3)
print(f'kaart 3 = {kaart_3}')
kaart_4 = deck.pop(4)
print(f'kaart 4 = {kaart_4}')
kaart_5 = deck.pop(5)
print(f'kaart 5 = {kaart_5}')
kaart_6 = deck.pop(6)
print(f'kaart 6 = {kaart_6}')
kaart_7 = deck.pop(7)
print(f'kaart 7 = {kaart_7}')
print(deck)