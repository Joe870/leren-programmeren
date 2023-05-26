doorgaan = 'ja'
hofb = 'ja'
while doorgaan == 'ja':
    aantal_bolletjes = int(input('hoeveel bolletjes wilt u?'))
    if aantal_bolletjes <=3:
        while hofb != 'hoorntje' or hofb != 'bakje':
            hofb = str(input(f'wilt u deze {aantal_bolletjes} bolletje(s) in een hoorntje of een bakje?'))
            if hofb != 'hoorntje' or hofb != 'bakje':
                print("sorry, dat snap ik niet")
    elif aantal_bolletjes >3 and aantal_bolletjes <=8:
        print(f"dan krijgt u van mij een bakje met {aantal_bolletjes} bolletjes")
    elif aantal_bolletjes >8:
        print("sorry, zulke grote bakken verkopen we niet")
    else:
        print("sorry dat snap ik niet")
    print(f"hier is uw {hofb} met {aantal_bolletjes} bolletje(s)")
    while doorgaan != '':
        doorgaan = input("wilt u nog meer bestellen")
        if doorgaan == 'nee':
            print('bedankt en tot ziens')
        else:
            print("sorry, dat snap ik niet")
    