diploma = input('bent uw in het bezit van een mbo-4 diploma?') 
rijbewijs = input('bent uw in het bezit van een geldig vrachtwagen rijbewijs?')
hoed = input('bent uw in bezit van een hoge hoed?') 
geslacht = input('welk geslacht heeft uw?')
if geslacht == 'man':
    snor = input('heeft uw een snor breder dan 10cm?') 
elif geslacht == 'vrouw':
    haar = input('heeft uw rood krulhaar?') 
lengte = int(input('wat is uw lengte in cm?'))
gewicht = int(input('wat is uw gewicht in kg?'))
certificaat = input('bent uw in het bezit van het certificaat overleven met gevaarlijk personeel?')
ervaring_1 = int(input('hoeveel jaar ervaring heeft uw met dieren-dressuur?'))
ervaring_2 = int(input('hoeveel jaar ervaring heeft uw met jongleren?'))
ervaring_3 = int(input('hoeveel jaar praktijkervaring heeft uw met acrobatiek?'))
if diploma == 'nee':
    print('helaas bent uw niet geschikt')
if rijbewijs == 'nee':
    print('helaas bent uw niet geschikt')
if hoed == 'nee':
    print('helaas bent uw niet geschikt')
if geslacht == 'man' and snor == 'nee':
      print('helaas bent uw niet geschikt')
if geslacht == 'vrouw' and haar == 'nee': 
    print('helaas bent uw niet geschikt')
if lengte < 150:
    print('helaas bent uw niet geschikt')
if lengte > 220:
    print('helaas bent uw niet geschikt')
if gewicht < 90:
    print('helaas bent uw niet geschikt')
if gewicht > 120: 
    print('helaas bent uw niet geschikt')
if certificaat == 'nee':
    print('helaas bent uw niet geschikt')
if ervaring_1 <4 or ervaring_2 <5 or ervaring_3 <3:
    print('helaas bent uw niet geschikt')
if diploma == 'ja' and rijbewijs == 'ja' and hoed == 'ja' and geslacht == 'man' and snor == 'ja' or geslacht == 'vrouw' and haar == 'ja' and lengte <150 and lengte >220 and gewicht <90 and gewicht >120 and certificaat == 'ja' and ervaring_1 >4 or ervaring_2 >5 or ervaring_3 >3:
    print('uw bent geschikt en mag op gesprek komen') 

   


