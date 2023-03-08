import random


while meerspelen == 'ja':
    print('versla de leider van het monsters in monster wood zodat onze onderdanen weer veilig zijn dat is mijn opdracht aan jullie als koning van dit land.')
    choose_character = input('choose character: A = fighter B = thief C = soldier D = mage')
    character = choose_character.upper() 


    aantal_item = 3

    def defense(defense_stat):
        som_defense = defense_stat + 5 
        return som_defense 

    def attack(attack_stat: int, defense_dragon:int, HP_dragon:int):
        som_attack = attack_stat - defense_dragon
        if som_attack <0:
            som_attack = 0
        HP_dragon = HP_dragon - som_attack
        return HP_dragon 
    
    def item(aantal_item):
        aantal_item = aantal_item - 1
        return aantal_item
    
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
                attackturn = attack(attack_stat,defense_dragon,HP_dragon)
                print(f' de draak heeft nog {attackturn} hp over')
            elif turn_1 == 'defend':
                defense_turn = defense(defense_stat)
                print(f' je hebt {defense_stat} defense')
            else: 
                itemturn = item(aantal_item)
                print(f' je hebt nog {itemturn} items over')
                som_hp = hp +30 
                if hp > 70:
                    hp = 70 
                print(f'je hebt nog {som_hp} hp over')
            if defense_dragon > 5:
                defense_dragon = 5
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
                print(f'action is defend defense stat dragon is {defense_dragon}')
            if defense_stat > 4:
                defense_stat = 4
                print(f' youre defense stat is',{defense_stat})
            aantal_punten -=1
            print(f' je hebt nog zoveel punten over{aantal_punten}')
    elif character == 'B':
        while HP_dragon > 0 or hp > 0:
            turn_1 = input('choose action: use item, defend, attack, steal item')
            if turn_1 == 'attack':
                attackturn = attack(attack_stat,defense_dragon,HP_dragon)
                print(f' de draak heeft nog {attackturn} hp over')
                if attackturn < 0:
                    attackturn = 0 
                print(HP_dragon)
            elif turn_1 == 'defend':
                defense_stat = defense
                print(defense_stat)
            elif turn_1 == 'steal item':
                aantal_item = aantal_item + 1 
                print(aantal_item) 
            else:
                itemturn = item(aantal_item)
                print(f' je hebt nog {itemturn} items over')
                som_hp = hp +30 
                if hp > 60:
                    hp = 60 
                print(f'je hebt nog {som_hp} hp over')
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
            aantal_punten -=1
            print(f' je hebt nog zoveel punten over')
    else:# dit is de mage 
        while HP_dragon > 0 or hp > 0:
            turn_1 = input('choose action: use item, defend, attack, use spell')
            if turn_1 == 'attack':
                attackturn = attack(attack_stat,defense_dragon,HP_dragon)
                print(f' de draak heeft nog {attackturn} hp over')
                if attack_turn1 < 0:
                    attack_turn1 = 0
                    print(HP_dragon)
            elif turn_1 == 'defend':
                defense_stat = defense
                print(defense_stat)
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
                itemturn = item(aantal_item)
                print(f' je hebt nog {itemturn} items over')
                som_hp = hp +30 
                if hp > 60:
                    hp = 60 
                print(f'je hebt nog {som_hp} hp over')
            if defense_dragon > 1:
                defense_dragon = 1 
                print(f'defend stat dragon is',{defense_dragon})
            print('enemy turn')
            action_enemy = random.randint(0,1) 
            if action_enemy == 1:
                attack_enemy = attack_dragon - defense_stat - hp
                print('action enemy is attack')
            elif action_enemy == 0:
                defense_dragon += 5 
                if hp == 0:
                    print('game over') 
                print('action enemy is defend')
            if defense_stat > 4:
                defense_stat = 4
            print('action is defend defense stat is',defense_dragon)
            print(f'defend stat is',{defense_stat}) 
            aantal_punten -=1
            print(f' je hebt nog zoveel punten over{aantal_punten}')                
    if HP_dragon < 0:
        print('dragon is defeated') 
        print('je hebt de leider van de monsters verslagen en de omliggende dorpen zijn veilig je missie is volbracht dappere soldaat')
    if hp < 0:
        print('game over') 
    meerspelen = input('wil je nog een keer spelen?')