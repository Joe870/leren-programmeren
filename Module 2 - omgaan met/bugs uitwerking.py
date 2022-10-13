import random

name = input('Wat is jouw naam? ')
print('Hallo', name)

favoriteSeason = input(f"Wat is jouw favorite seizoen {name}? A = Lente,) B Zomer,) C Herfst) of D Winter)")
answer = favoriteSeason.upper() 

if answer == 'A':
    print("Ik hou ook van de lente!")
elif answer == 'B':
    print("De zomer is voor mij te warm.")
elif answer == 'C':
    print("Mooi he, al die blaadjes die dan van de boom vallen.")
elif answer == 'D':
    print("Is de winter niet erg koud?")
else: print("Die ken ik niet...")

favoriteColor = input('En wat is je favoriete kleur?') 
trueOrFalse = random.randint(0,1)
if trueOrFalse == 0:
    print('Ik vind dat ook een mooie kleur!')
else:
    print('TBH, ik hou niet zo van {}...'.format(favoriteColor)) 

num1 = random.randint(1,10)
num2 = random.randint(5,15)

try: 
    number = int(input(f"En weet jij wat, {num1} + {num2} is?"))
    if int(number == num1+num2): 
        print('Dat is juist')
    else: 
        print('Dat niet juist!')
except: 
    print(f'Nee dat klopt niet {name}')


