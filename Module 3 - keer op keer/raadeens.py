from random import randint
score = 0
ronde = 0 
beurt = 0

while ronde <20:
    raadgetal = randint(1,1000)
    vraag = input('wil je nog een ronde spelen')
    if vraag == 'nee':
        break
    while beurt < 10:
        raadvraag = int(input('welk getal raad je?'))
        if raadvraag < raadgetal:
            print('hoger')
            beurt+=1
            verschil = raadgetal - raadvraag
            if verschil <0:
                verschil *= -1
            elif verschil < 50:
                print('Je bent warm')
            elif verschil < 50 >20:
                print('Je bent heel warm')
        elif raadvraag > raadgetal:
            print('lager') 
            beurt+=1
            verschil = raadgetal - raadvraag
            if verschil <0:
                verschil *= -1
            elif verschil < 50:
                print('Je bent warm')
            elif verschil < 50 >20:
                print('Je bent heel warm')
        elif raadvraag == raadgetal:
            score += 1 
            ronde +=1
            print('getal geraden')
            break 
        print(f'einde beurt {beurt}')
    print('teveel rondes gespeeld einde beurt')
print(score)
print('einde spel')