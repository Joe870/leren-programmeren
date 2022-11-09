printed = ''
welke_dag = input('welke dag is het vandaag')
while welke_dag != printed:
    if printed == '':
        printed = 'maandag'
        print('maandag')
    elif printed == 'maandag':
        printed = 'dinsdag'
        print('dinsdag')
    elif printed == 'dinsdag':
        printed = 'woensdag' 
        print('woensdag')
    elif printed == 'woensdag':
        printed = 'donderdag'
        print('donderdag') 
    elif printed == 'donderdag':
        printed = 'vrijdag'
        print('vrijdag')
    elif printed == 'vrijdag':
        printed = 'zaterdag'
        print('zaterdag')
    else:
        printed = 'zondag'
        print('zondag') 

