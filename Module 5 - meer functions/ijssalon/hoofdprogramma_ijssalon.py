from library_ijssalon import *
prijs_bolletjes = 0.95
prijs_hoorntjes = 1.25
prijs_bakjes = 0.75
prijs_liter = 9.80
aantal_aardbei = 0
aantal_chocolade = 0
aantal_vanille = 0
aantal_bolletjes = 0
aantal_liter = 0
aantal_hoorntjes = 0
aantal_bakjes = 0 
aantal_topping = 0
volgende_bestelling = 'ja'
hoorn_of_bak = ''
aantal_geen = 0 
aantal_slagroom = 0
aantal_sprinkels = 0 
aantal_caramel_hoorn = 0
aantal_caramel_bak = 0
prijs_geen = 0
prijs_slagroom = 0.50
prijs_sprinkels = 0.30 
prijs_caramel_hoorn = 0.60
prijs_caramel_bakje = 0.90
eind_prijs_slagroom = 0
eind_prijs_sprinkels = 0
eind_prijs_geen = 0
eind_prijs_caramel_bakje = 0
eind_prijs_caramel_hoorntje =0 
btw = 6

while volgende_bestelling == "ja":
    print('welkom bij Papi Gelato')
    klant = int(soort_klant())
    if klant == 1:
        aantal_bolletjes = aantal_bolletjes_ijs(klant)
        aantal_geen, aantal_slagroom, aantal_sprinkels, aantal_caramel_bak, aantal_caramel_hoorn = welke_topping(aantal_bolletjes,hoorn_of_bak)
        for bolletjes in range(aantal_bolletjes):
            smaken = smaak(aantal_bolletjes, aantal_liter, klant)
            aantal_aardbei, aantal_chocolade, aantal_vanille = aantal_smaak(aantal_aardbei,aantal_chocolade,aantal_vanille,smaken)
        hoorn_of_bak = waar_in(aantal_bolletjes)
        aantal_hoorntjes, aantal_bakjes = aantal_hoorntjes_bakjes(hoorn_of_bak,aantal_hoorntjes,aantal_bakjes)
        meld_transactie = print(f'hier is uw {hoorn_of_bak} met {aantal_bolletjes} bolletje(s)')
        volgende_bestelling = meer()
        aantal_topping = aantal_geen + aantal_slagroom + aantal_sprinkels + aantal_caramel_bak + aantal_caramel_hoorn
        eind_prijs_slagroom += round(aantal_slagroom * prijs_slagroom,2)
        eind_prijs_sprinkels += round(aantal_sprinkels * prijs_sprinkels,2)
        eind_prijs_geen += round(aantal_geen * prijs_geen,2)
        eind_prijs_caramel_bakje += round(aantal_caramel_bak * prijs_caramel_bakje,2)
        eind_prijs_caramel_hoorntje += round(aantal_caramel_hoorn * prijs_caramel_hoorn,2)
        eind_prijs_topping = eind_prijs_slagroom + eind_prijs_sprinkels + eind_prijs_geen + eind_prijs_caramel_bakje + eind_prijs_caramel_hoorntje
        eind_prijs_aardbei = round(aantal_aardbei * prijs_bolletjes,2)
        eind_prijs_chocola = round(aantal_chocolade * prijs_bolletjes,2)
        eind_prijs_vanille = round(aantal_vanille * prijs_bolletjes,2)
        eind_prijs_hoorntjes = round(aantal_hoorntjes * prijs_hoorntjes,2)
        eind_prijs_bakjes = round(aantal_bakjes * prijs_bakjes,2)
        eind_prijs_totaal = round(eind_prijs_bakjes + eind_prijs_hoorntjes + eind_prijs_aardbei + eind_prijs_chocola + eind_prijs_vanille + eind_prijs_topping,2)
    elif klant == 2:
        aantal_liter = aantal_bolletjes_ijs(klant)
        for liters in range(aantal_liter):
            smaken = smaak(aantal_bolletjes, aantal_liter, klant)
            aantal_aardbei, aantal_chocolade, aantal_vanille = aantal_smaak(aantal_aardbei,aantal_chocolade,aantal_vanille,smaken)
        eind_prijs_aardbei = round(aantal_aardbei * prijs_liter,2)
        eind_prijs_chocola = round(aantal_chocolade * prijs_liter,2)
        eind_prijs_vanille = round(aantal_vanille * prijs_liter,2)
        eind_prijs_ijs = round((aantal_aardbei + aantal_chocolade + aantal_vanille) * prijs_liter,2)
        eind_btw = round(eind_prijs_ijs / 100 * btw,2)
        print(eind_btw)
        eind_prijs_totaal = round(eind_prijs_aardbei + eind_prijs_chocola + eind_prijs_vanille + eind_btw,2)
        volgende_bestelling = 'nee'

if klant == 1:
    lob = 'Bolletjes'
    
elif klant == 2:
    lob = 'Liter'
print('-----------["papi gelato"]------------')
if aantal_aardbei >= 1:
    print(f'{lob} aardbei      {aantal_aardbei} x ${prijs_bolletjes} = $ {eind_prijs_aardbei}')
if aantal_chocolade >= 1:
    print(f'{lob} chocola     {aantal_chocolade} x ${prijs_bolletjes} = $ {eind_prijs_chocola}')
if aantal_vanille >= 1:
    print(f'{lob} vanille      {aantal_vanille} x ${prijs_bolletjes} = $ {eind_prijs_vanille}')
if aantal_hoorntjes >= 1:
        print(f'Hoorntjes                 {aantal_hoorntjes} x ${prijs_hoorntjes} = $ {eind_prijs_hoorntjes}')
if aantal_bakjes >= 1:
        print(f'Bakjes         {aantal_bakjes} x ${prijs_bakjes} = $ {eind_prijs_bakjes}')
if aantal_topping >= 1:
        print(f'topping                        = $ {eind_prijs_topping}')
if klant == 2:
    print(f'BTW                       = ${eind_btw}')
print('---------------------------------------')
print(f'totaal         = ${eind_prijs_totaal}')
print('bedankt en tot ziens')
     
     
