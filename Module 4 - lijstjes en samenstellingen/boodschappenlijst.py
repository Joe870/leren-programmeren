meerboodschappen = 'ja'
boodschappenlijst = {}
aantal_boodschappen = 0 
while meerboodschappen == 'ja': 
    meerboodschappen = input('wil je nog meer boodschap toevoegen')
    if meerboodschappen == 'ja': 
        boodschap = input('welke boodschap wil je toevoegen')
        aantal_boodschappen = abs(int(input('hoeveel van dit product wil je toevoegen')))
        boodschap.lower()
        if boodschap in boodschappenlijst:
            boodschappenlijst[boodschap]+=aantal_boodschappen
            aantal_boodschappen+=1 
        else:
            boodschappenlijst[boodschap]=aantal_boodschappen
for key in boodschappenlijst: 
    print(f'{key} x {boodschappenlijst[key]}')

