from library_ijssalon import *
prijs_bolletjes = 1.10

volgende_bestelling = 'ja'

while volgende_bestelling == "ja":
    aantal_bolletjes = aantal_bolletjes_ijs()
    if aantal_bolletjes <= 3:
        hoorn_of_bak = waar_in(aantal_bolletjes)
    elif aantal_bolletjes >3 and aantal_bolletjes <=8:
        hoorn_of_bak = 'bakje'
    meld_transactie = print(f'hier is uw {hoorn_of_bak} met {aantal_bolletjes} bolletje(s)')
    volgende_bestelling = meer()
