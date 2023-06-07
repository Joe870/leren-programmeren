from library_ijssalon import *
prijs_bolletjes = 1.10
prijs_hoorntjes = 1.25
prijs_bakjes = 0.75
aantal_bolletjes = 0
aantal_hoorntjes = 0
aantal_bakjes = 0 
volgende_bestelling = 'ja'
hoorn_of_bak = ''

while volgende_bestelling == "ja":
    aantal_bolletjes = aantal_bolletjes_ijs()
    hoorn_of_bak = waar_in(aantal_bolletjes)
    meld_transactie = print(f'hier is uw {hoorn_of_bak} met {aantal_bolletjes} bolletje(s)')
    volgende_bestelling = meer()

aantal_hoorntjes = aantal_hoorntjes_bakjes(aantal_bolletjes)
eind_prijs_bolletjes = round(prijs_bolletjes * aantal_bolletjes,2)
eind_prijs_hoorntjes = round(prijs_hoorntjes * aantal_hoorntjes,2)
eind_prijs_bakjes = round(prijs_bakjes * aantal_bakjes,2) 
eind_prijs_totaal = prijs_bakjes + prijs_hoorntjes + prijs_bolletjes

print('-----------["papi gelato"]------------')
if aantal_bolletjes >= 1:
    print(f'Bolletjes      {aantal_bolletjes} x ${prijs_bolletjes} = $ {eind_prijs_bolletjes}')
if aantal_hoorntjes >= 1:
    print(f'Hoorntjes      {aantal_hoorntjes} x ${prijs_hoorntjes} = $ {eind_prijs_hoorntjes}')
if aantal_bakjes >= 1:
    print(f'Bakjes         {aantal_bakjes} x ${prijs_bakjes} = $ {eind_prijs_bakjes}')
print('---------------------------------------')
print(f'totaal         = ${eind_prijs_totaal}')
print('bedankt en tot ziens')