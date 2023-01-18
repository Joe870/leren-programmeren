# deze functie stelt een vraag, valideert en controleert of de input een valide leeftijd is
# vraag: str is de parameter
# input(vraag) is een argument
def vraag_leeftijd_gebruiker(vraag: str) -> int:
    while True:
        leeftijd_string = input(vraag)
        if not leeftijd_string.isnumeric():
            print("voer een getal in")
        elif int(leeftijd_string) > 130:
            print("zo oud is nog nooit iemand geworden")
        elif int(leeftijd_string) <0:
            print("u moet nog geboren worden!")
        else:
            leeftijd = int (leeftijd_string)
            break
        return leeftijd
def vraag_naam_gebruiker(vraag: str):
    while True:
        naam_string = input(naam)
        if naam_string.isnumeric():
            print("voer een naam in")
        elif (naam_string) > len(10):
            print("deze naam is te lang")
        elif (naam_string) >len(2):
            print("deze naam is te kort")
        else:
            naam = str(naam_string)
            break
        return naam

print("hallo wereld")
naam = vraag_naam_gebruiker("hoe heet je?")
leeftijd = vraag_leeftijd_gebruiker("hoe oud ben je?")
print(f"hallo {naam} je leeftijd is {leeftijd}")
