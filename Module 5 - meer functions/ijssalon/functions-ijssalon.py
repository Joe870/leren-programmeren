from library_ijssalon import *
prijs_bolletjes = 1.10
prijs_hoorntjes = 1.25
prijs_bakjes = 0.75
aantal_aardbei = 0
aantal_chocolade = 0
aantal_munt = 0 
aantal_vanille = 0
totale_aantal_bolletjes = 0
aantal_hoorntjes = 0
aantal_bakjes = 0 
volgende_bestelling = 'ja'
hoorn_of_bak = ''

while volgende_bestelling == "ja":
    print('welkom bij Papi Gelato')
    aantal_bolletjes = aantal_bolletjes_ijs()
    totale_aantal_bolletjes += aantal_bolletjes
    hoorn_of_bak = waar_in(aantal_bolletjes)
    meld_transactie = print(f'hier is uw {hoorn_of_bak} met {aantal_bolletjes} bolletje(s)')
    for bolletjes in range(aantal_bolletjes):
        smaken = smaak(aantal_bolletjes,bolletjes)
        aantal_aardbei, aantal_chocolade, aantal_munt, aantal_vanille = aantal_smaak(aantal_aardbei,aantal_chocolade,aantal_munt,aantal_vanille,smaken)
    volgende_bestelling = meer()
    aantal_hoorntjes, aantal_bakjes = aantal_hoorntjes_bakjes(hoorn_of_bak,aantal_hoorntjes,aantal_bakjes)
    print(f'{aantal_aardbei} aardbei')
    print(f'{aantal_chocolade} schocola')
    print(f'{aantal_munt} munt')
    print(f'{aantal_vanille} vanille')
    eind_prijs_aardbei = round(aantal_aardbei * prijs_bolletjes,2)
    eind_prijs_chocola = round(aantal_chocolade * prijs_bolletjes,2)
    eind_prijs_munt = round(aantal_munt * prijs_bolletjes,2)
    eind_prijs_vanille = round(aantal_vanille * prijs_bolletjes,2)
    eind_prijs_hoorntjes = round(aantal_hoorntjes * prijs_hoorntjes,2)
    eind_prijs_bakjes = round(aantal_bakjes * prijs_bakjes,2)
    eind_prijs_totaal = eind_prijs_bakjes + eind_prijs_hoorntjes + eind_prijs_aardbei + eind_prijs_chocola + eind_prijs_munt + eind_prijs_vanille

print('-----------["papi gelato"]------------')
if aantal_aardbei >= 1:
    print(f'Bolletjes aardbei      {aantal_aardbei} x ${prijs_bolletjes} = $ {eind_prijs_aardbei}')
if aantal_chocolade >= 1:
    print(f'Bolletjes chocola     {aantal_chocolade} x ${prijs_bolletjes} = $ {eind_prijs_chocola}')
if aantal_munt >= 1:
    print(f'Bolletjes munt     {aantal_munt} x ${prijs_bolletjes} = $ {eind_prijs_munt}')
if aantal_vanille >= 1:
    print(f'Bolletjes vanille      {aantal_vanille} x ${prijs_bolletjes} = $ {eind_prijs_vanille}')
if aantal_hoorntjes >= 1:
    print(f'Hoorntjes      {aantal_hoorntjes} x ${prijs_hoorntjes} = $ {eind_prijs_hoorntjes}')
if aantal_bakjes >= 1:
    print(f'Bakjes         {aantal_bakjes} x ${prijs_bakjes} = $ {eind_prijs_bakjes}')
print('---------------------------------------')
print(f'totaal         = ${eind_prijs_totaal}')
print('bedankt en tot ziens')