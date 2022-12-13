from fruitmand import fruitmand
from random import randint
aantal_fruit = int(input('noem een aantal'))
for fruit in range(aantal_fruit):
    dict_numb = randint(0,len(fruitmand)-1)
    print(fruitmand[dict_numb].get("name"))



