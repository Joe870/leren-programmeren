volgende_bestelling = 'ja'

def soort_klant():
    soort_klant = input('bent u 1) een particuliere klant of 2) een zakelijke klant?')
    return soort_klant

def aantal_bolletjes_ijs(klant):
    if klant == 1:
        aantal_bolletjes = int(input('hoeveel bolletjes'))
        print(f'{aantal_bolletjes}aantal bolletjes')
        while aantal_bolletjes > 8:
            print('sorry zulke grote bakjes hebben we niet')
            aantal_bolletjes = int(input('hoeveel bolletjes wilt u?'))
        return aantal_bolletjes 
    else:
        aantal_liter = int(input('hoeveel liter'))
        print(f'{aantal_liter}aantal liter')
    return aantal_liter

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

def smaak(bolletje, liter, klant):
    if klant == 1:
        smaak = input(f'welke smaak wilt u voor bolletje {bolletje}? A) aardbei, C) chocolade, of V) vanille?')
    elif klant == 2:
        smaak = input(f'welke smaak wilt u voor liter {liter}? A) aardbei, C) chocolade, of V) vanille?')
    smaak=smaak.upper()
    return smaak

def aantal_smaak(aantal_aardbei, aantal_chocolade, aantal_vanille, taste):
    if taste == 'A':
        aantal_aardbei +=1
    elif taste == 'C':
        aantal_chocolade +=1
    elif taste == 'V':
        aantal_vanille +=1
    return aantal_aardbei, aantal_chocolade, aantal_vanille

def welke_topping(bolletjes,bofh):
    aantal_sprinkels = 0
    aantal_slagroom = 0
    aantal_caramel_bak = 0 
    aantal_caramel_hoorn = 0
    aantal_geen =0 
    topping = input(f'wat voor topping wilt u: A) geen, B) slagroom, C) sprinkels of D) caramel saus?')
    topping = topping.upper()
    if topping == 'C':
        for bolletjes in range(bolletjes):
            extra_sprinkels = input(f'wilt uw op bolletje {bolletjes+1} sprinkels')
            if extra_sprinkels == 'ja':
                aantal_sprinkels +=1 
    elif topping == 'A':
        aantal_geen += 1
    elif topping == 'B':
        aantal_slagroom +=1 
    else: 
        if bofh == 'hoorntje':
            aantal_caramel_hoorn +=1
        elif bofh == 'bakje':
            aantal_caramel_bak += 1 
    return aantal_geen, aantal_slagroom, aantal_sprinkels, aantal_caramel_bak, aantal_caramel_hoorn

