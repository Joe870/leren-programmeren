from random import shuffle
lijst_namen = []
lijst_lootjes = []
namen_lootjes_dict = {}
ok = True
meer_naam = 'ja'
while meer_naam == 'ja': 
    naam = input('wat is jouw naam')
    if naam not in lijst_namen:
        lijst_namen.append(naam)
        lijst_lootjes.append(naam)
    if len(lijst_namen) >=3:
        meer_naam = input('wil je nog meer namen toevoegen')

while ok == True:
    shuffle(lijst_lootjes)
    for namen in range(len(lijst_namen)):
        if lijst_namen[namen] != lijst_lootjes[namen]:
            ok = False

for index in range(len(lijst_namen)):
    dict[lijst_namen[index]] = lijst_lootjes[index]
print(dict)
