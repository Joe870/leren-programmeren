def addition(n1, n2):
    som_optellen = n1 + n2
    return som_optellen

def subtraction(n1, n2):
    som_aftrekken = n1 - n2
    return som_aftrekken

def multipliction(n1, n2):
    som_vermenigvuldigen = n1 * n2
    return som_vermenigvuldigen

def division(n1,n2):
    som_delen = n1 / n2
    return som_delen


def inputfloat(bericht : str) -> float:
    while True:
        try:
            number = input(bericht)
            number = float(number)
            return number
        except:
            print('vul een getal in')

choice =''
n1 = False
firstround = True
while choice != 'stop':
    if firstround:
        choice = input('wat wil je doen? A getallen optellen, B getallen aftrekken, C getallen vermenigvuldigen, D getallen delen, E getal ophogen, F getal verlagen, G getal verdubbelen, H getal halveren, I stop\n')
    elif not firstround:
        choice = input(f'wat wil je met {n1} doen? A getal optellen, B getal aftrekken, C getal vermenigvuldigen, D getal delen, E getal ophogen, F getal verlagen, G getal verdubbelen, H getal halveren, I stop\n')
    choice = choice.upper()
    # heeft nog geen waarde
    n2 = False
    if choice == 'I':
        break
    if choice in ['E','F']:
        n2 = 1 
    elif choice in ['G','H']:
        n2 = 2 
    if n1 == False:
        n1 = inputfloat('vul een getal in')
        print(f'{n1} n1')
    if n2 == False:
        n2 = inputfloat('vul een getal in')
        print(f'{n2} n2')
    if choice == 'A':
        uitkomst = addition(n1,n2) 
        #optellen 
    elif choice == 'B':
        uitkomst = subtraction(n1,n2)
        print(uitkomst)
        #aftrekken
    elif choice == 'C':
        uitkomst = multipliction(n1,n2)
        print(uitkomst)
        #vermenigvuldigen 
    elif choice == 'D':
        uitkomst = division(n1,n2)
        print(uitkomst)
        #delen
    elif choice == 'E':
        uitkomst = addition(n1,n2)
        print(uitkomst)
        #ophogen
    elif choice == 'F':
        uitkomst = subtraction(n1,n2)
        print(uitkomst) 
        #verlagen
    elif choice == 'G':
        uitkomst= multipliction(n1,n2)
        #verdubbelen
    elif choice == 'H':
        uitkomst = division(n1,n2) 
        #halveren
    else: 
        firstround == False
        print('stop')
    firstround = False
    print(f'uitkomst{uitkomst}')
    n1 = uitkomst
