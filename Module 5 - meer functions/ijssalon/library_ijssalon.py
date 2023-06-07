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
    else:
        hofb = input(f'wilt u deze {aantal_bolletjes} bolletje(s) in een hoorntje of een bakje?')
    return hofb

def aantal_hoorntjes_bakjes(aantal_bolletjes):
    aantal_bakjes = 0 
    aantal_hoorntjes = 0 
    prijs_hoorntjes = 1.25
    prijs_bakjes = 0.75
    if aantal_bolletjes >3 and aantal_bolletjes <=8:
        aantal_bakjes += 1
    hofb = waar_in(aantal_bolletjes)
    if hofb == 'hoorntje':
        aantal_hoorntjes += 1 
    elif hofb == 'bakje':
        aantal_bakjes += 1 
    prijs_hoorntjes = round(prijs_hoorntjes * aantal_hoorntjes,2)
    prijs_bakjes = round(prijs_bakjes * aantal_bakjes,2)
    return prijs_hoorntjes, prijs_bakjes

def meer():
    doorgaan = input("wilt u nog meer bestellen")
    if doorgaan == 'nee':
        print('bedankt en tot ziens')
    return doorgaan

