vraag_naam = ''
vraag_leeftijd = ''
def vraag_persoon():
    persoon = {}
    vraag_naam = input('wat is je naam')
    vraag_leeftijd = input('wat is je leeftijd')
    persoon["naam"] = vraag_naam
    persoon["leeftijd"] = vraag_leeftijd
    return persoon
lijst_personen = []
while True:
    persoon_dict = vraag_persoon()
    if persoon_dict["naam"] == "stop":
        break
    else:
        lijst_personen.append(persoon_dict)
for persoon in lijst_personen:
    print(f'{persoon["naam"]} is {persoon["leeftijd"]}')
