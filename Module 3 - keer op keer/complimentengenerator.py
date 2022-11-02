from random import randint
naam = input('wat is je naam') 
hoeveel_complimenten = int(input('hoeveel complimenten wil je'))

for x in range(hoeveel_complimenten):
    welk_compliment = randint(1,4) 
    if welk_compliment == 1:
        print(f'je bent geweldig {naam}') 
    elif welk_compliment == 2:
        print(f'je bent superslim {naam}')
    elif welk_compliment == 3:
        print(f'je bent superknap {naam}')
    else:
        print(f'je hebt veel talent {naam}') 


