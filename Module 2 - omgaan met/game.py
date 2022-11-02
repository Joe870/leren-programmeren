import random

# lege variabelen 
hp_player = ''
hp = ''
attack_stat = ''
defense_stat = ''
mp = '' 
# stats slime monster 1 
HP_slime = 20 
attack_slime = 9 
defense_slime = 1
# stats giant bat monster 2
HP_giantbat = 9
attack_giantbat = 12
defense_giantbat = 8
# stats skeleton monster 3
HP_skeleton = 30
attack_skeleton = 28
defense_skeleton = 22
# stats dragon boss monster 
HP_dragon = 60
attack_dragon = 10
defense_dragon = 5

print('versla de leider van het monsters in monster wood zodat onze onderdanen weer veilig zijn dat is mijn opdracht aan jullie als koning van dit land.')
choose_character = input('choose character: A = fighter B = thief C = soldier D = mage')
character = choose_character.upper() 
# stats fighter
if character == 'A':
    hp = 70 
    attack_stat = 10
    defense_stat = 5
    mp = 0 
# stats thief
if character == 'B':
    hp = 60
    attack_stat = 8
    defense_stat = 15
    mp = 0 
# stats soldier
if character == 'C':
    hp = 70
    attack_stat = 8
    defense_stat = 10
    mp = 0
# stats mage
if character == 'D':
    hp = 60 
    attack_stat = 1
    defense_stat = 4
    mp = 100
item = 'poiton'
aantal_item = 3
print(f'hp = {hp}')
print(f'attack = {attack_stat}') 
print(f'defense = {defense_stat}')
print(f'mp = {mp}')
print('je vindt de leider van de monsters een draak je valt aan')
print('player turn:')
if character == 'A' or character == 'C':
    while HP_dragon > 0 or hp > 0: 
        turn_1 = input('choose action: use item, defend, attack')
        if turn_1 == 'attack':
            attack_turn1 = attack_stat - defense_dragon
            HP_dragon = HP_dragon - attack_turn1
            if attack_turn1 < 0:
                attack_turn1 = 0 
            print(HP_dragon)
        elif turn_1 == 'defend':
            defense_stat = defense_stat + 5
            print(defense_stat)
        else: 
            hp + 30 
            aantal_item = aantal_item - 1 
            if hp > 70:
                hp = 70 
            print(hp)
            print(aantal_item) 
        if defense_slime > 5:
            defense_slime = 5
            print(f'defense stat dragon is',{defense_dragon}) 
        print('hpwaarde',hp)
        print('enemy turn')
        action_enemy = random.randint(0,1) 
        if action_enemy == 1:
            attack_enemy = attack_dragon - defense_stat
            hp_player = hp - attack_enemy
            print('action is attack')
            print(hp_player)
        elif action_enemy == 0:
            action_enemy = defense_dragon
            defense_dragon = defense_dragon + 5 
            print('action is defend defense stat dragon is',defense_dragon)
        if defense_stat > 4:
            defense_stat = 4
            print(f' youre defense stat is',{defense_stat})
elif character == 'B':
    while HP_dragon > 0 or hp > 0:
        turn_1 = input('choose action: use item, defend, attack, steal item')
        if turn_1 == 'attack':
            attack_turn1 = attack_stat - defense_dragon
            HP_dragon = HP_dragon - attack_turn1 
            print('hpwaarde dragon',HP_dragon)  
            if attack_turn1 < 0:
                attack = 0 
            print(HP_dragon)
        elif turn_1 == 'defend':
            defense_stat = defense_stat + 5
        elif turn_1 == 'steal item':
            aantal_item = aantal_item + 1 
            print(aantal_item) 
        else:
            hp + 30 
            aantal_item = aantal_item - 1 
            print(aantal_item) 
            if hp > 60:
                hp = 60
            print('hpwaarde',hp)
        if defense_dragon > 1:
            defense_dragon = 1 
            print(f'defend stat dragon is',{defense_dragon}) 
        print('enemy turn')
        action_enemy = random.randint(0,1) 
        if action_enemy == 1:
            attack_enemy = attack_dragon - defense_stat - hp
            print('action enemy is attack')
        elif action_enemy == 0:
            defense_dragon = defense_dragon + 5 
        print(action_enemy)
        if defense_stat > 4:
            defense_stat = 4
            print(f'defend stat is',{defense_stat})
            print('action enemy is defend') 

else:# dit is de mage 
    while HP_dragon > 0 or hp > 0:
        turn_1 = input('choose action: use item, defend, attack, use spell')
        if turn_1 == 'attack':
            attack_turn1 = attack_stat - defense_dragon
            HP_dragon = HP_dragon - attack_turn1
            if attack_turn1 < 0:
                attack_turn1 = 0
                print(HP_dragon)
        elif turn_1 == 'defend':
            defense_stat + 5
        elif turn_1 == 'use spell':
            spell_type = input('choose spell: heal or fireball')
            if spell_type == 'heal':
                hp + 30 
                mp = mp - 5 
                if hp >60:
                    hp = 60 
            print('hpwaarde', hp)
            print('mpwaarde', mp)
            if spell_type == 'fireball':
                HP_dragon - 10 
                mp = mp - 5 
                if HP_dragon == 0:
                    print('dragon is defeated') 
        else:
            hp + 30 
            aantal_item = aantal_item - 1 
            if hp > 60:
                hp = 60 
            print('hpwaarde',hp) 
        if defense_dragon > 1:
            defense_dragon = 1 
            print(f'defend stat dragon is',{defense_dragon})
        print('enemy turn')
        action_enemy = random.randint(0,1) 
        if action_enemy == 1:
            attack_enemy = attack_dragon - defense_stat - hp
            print('action enemy is attack')
        elif action_enemy == 0:
            defense_slime = defense_dragon + 5 
            if hp == 0:
                print('game over') 
            print('action enemy is defend')
        if defense_stat > 4:
            defense_stat = 4
        print('action is defend defense_slime is',defense_dragon)
        print(f'defend stat is',{defense_stat}) 
if HP_dragon < 0:
    print('dragon is defeated') 
    print('je hebt de leider van de monsters verslagen en de omliggende dorpen zijn veilig je missie is volbracht dappere soldaat')
if hp < 0:
    print('game over') 
 