def vraag_naam_gebruiker(vraag: str):
    naam_lijst = []
    leeftijd_lijst = []
    while True:
        naam_string = input('wat is je naam')
        if naam_string == 'stop':
            break
        naam_lijst += naam_string
        naam = str(naam_string)
        leeftijd_string = input('wat is je leeftijd')
        leeftijd_lijst += leeftijd_string
        leeftijd = str(leeftijd_string)
    for index in range(len(naam_lijst)):
        dict[naam_lijst[index]] = leeftijd_lijst[index]
    return dict
vraag_naam_gebruiker('wat is je naam, hoe oud ben je')

# print(f'{leeftijd_string}')