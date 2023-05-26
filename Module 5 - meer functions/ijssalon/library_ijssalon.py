volgende_bestelling = 'ja'
def aantal_bolletjes_ijs():
    aantal_bolletjes = int(input('hoeveel bolletjes'))
    print(aantal_bolletjes)
    while aantal_bolletjes > 8:
        print('sorry zulke grote bakjes hebben we niet')
        aantal_bolletjes = int(input('hoeveel bolletjes wilt u?'))
    return aantal_bolletjes

def waar_in(aantal_bolletjes):
    hfob = 'hoorntje'
    hofb = input(f'wilt u deze {aantal_bolletjes} bolletje(s) in een hoorntje of een bakje?')
    if aantal_bolletjes >3 and aantal_bolletjes <=8:
        hofb = 'bakje'
    return hofb

def meer():
    doorgaan = input("wilt u nog meer bestellen")
    if doorgaan == 'nee':
        print('bedankt en tot ziens')
    return doorgaan
    