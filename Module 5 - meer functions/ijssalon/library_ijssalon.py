prijs_bolletjes = 1.10
prijs_hoorntjes = 1.25
prijs_bakjes = 0.75
aantal_bolletjes = 0
aantal_hoorntjes = 0
aantal_bakjes = 0 
volgende_bestelling = 'ja'
hoorn_of_bak = ''
aantal = 0
aantal_aardbei = 0
aantal_chocolade = 0
aantal_munt = 0 
aantal_vanille = 0
volgende_bestelling = 'ja'

def aantal_bolletjes_ijs():
    aantal_bolletjes = int(input('hoeveel bolletjes'))
    print(aantal_bolletjes)
    while aantal_bolletjes > 8:
        print('sorry zulke grote bakjes hebben we niet')
        aantal_bolletjes = int(input('hoeveel bolletjes wilt u?'))
    return aantal_bolletjes

def waar_in(aantal_bolletjes):
    hofb = ''
    if aantal_bolletjes >3 and aantal_bolletjes <8:
        hofb = 'bakje'
    elif aantal_bolletjes>=1:
        hofb = input(f'wilt u deze {aantal_bolletjes} bolletje(s) in een hoorntje of een bakje?')
    return hofb

def aantal_hoorntjes_bakjes(hoorn_of_bak,aantal_hoorntjes,aantal_bakjes):
    if hoorn_of_bak == 'bakje':
        aantal_bakjes += 1
    elif hoorn_of_bak == 'hoorntje':
        aantal_hoorntjes += 1 
    return aantal_hoorntjes, aantal_bakjes

def meer():
    doorgaan = input("wilt u nog meer bestellen")
    if doorgaan == 'nee':
        print('bedankt en tot ziens')
    return doorgaan

def smaak(aantal_bolletjes, bolletje):
    smaak = input(f'welke smaak wilt u voor bolletje {bolletje}? A) aardbei, C) chocolade, M) munt of V) vanille?')
    smaak=smaak.upper()
    print(smaak) 
    return smaak

def aantal_smaak(aantal_aardbei, aantal_chocolade, aantal_munt, aantal_vanille,taste):
    if taste == 'A':
        aantal_aardbei +=1
    elif taste == 'C':
        aantal_chocolade +=1
    elif taste == 'M':
        aantal_munt +=1
    elif taste == 'V':
        aantal_vanille +=1
    return aantal_aardbei, aantal_chocolade, aantal_munt, aantal_vanille