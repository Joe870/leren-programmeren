# stats fighter
HP_fighter = str(50) 
attack_fighter = str(10)
defense_fighter = str(5)

# stats thief
HP_thief = str(60)
attack_thief = str(6)
defense_thief = str(15) 
# stats soldier
HP_soldier = str(50)
attack_soldier = str(8)
defense_soldier = str(10)
# stats mage 
HP_mage = str(40) 
attack_mage = str(1)
defense_mage = str(4)
MP_mage = str(50) 
# stats slime monster 1 
HP_slime = str(20) 
attack_slime = str(9) 
defense_slime = str(5) 
# stats giant bat monster 2
HP_giantbat = str(9) 
attack_giantbat = str(12) 
defense_giantbat = str(8) 
# stats skeleton monster 3
HP_skeleton = str(30)
attack_skeleton = str(28)
defense_skeleton = str(22)
# stats dragon boss monster 
HP_dragon = str(60)
attack_dragon = str(40)
defense_dragon = str(25) 

print('versla de leider van het monsters in monster wood zodat onze onderdanen weer veilig zijn dat is mijn opdracht aan jullie als koning van dit land.')
choose_character = input('choose character: A = fighter B = thief C = soldier D = mage')
character = choose_character.upper() 
if choose_character == 'A':
    hp = str(50) 
    attack = str(10)
    defense = str(5)
    mp = str(0) 
if choose_character == 'B':
    hp = str(60)
    attack = str(6)
    defense = str(15)
    mp = str(0) 
if choose_character == 'C':
    hp = str(50)
    attack = str(8)
    defense = str(10)
    mp = str(0)
if choose_character == 'D':
    hp = str(40) 
    attack = str(1)
    defense = str(4)
    mp = str(50) 
print(hp)
print(attack) 
print(defense)
print(mp)
print('je komt een monster tegen een slime, de slime is agressief en dus val je aan')
print('player turn')
if choose_character == 'A' or 'B':
    turn_1 = input('use item, defend, attack')
elif choose_character == 'B':
    turn_1 = input('use item, defend, attack, steal item')
else: 
    turn_1 = input('use item, defend, attack, use spell')