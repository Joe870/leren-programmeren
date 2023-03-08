import random

# lege variabelen 
hp_player = ''
hp = ''
attack_stat = ''
defense_stat = ''
mp = '' 

aantal_items = 3
meerspelen = 'ja'
aantal_punten = 100 
character_stats = {}
base_stat_hp_fighter = 70
base_stat_hp_thief = 60 
base_stat_hp_soldier = 70
base_stat_hp_mage = 60

foe = {'hp dragon': 60, 'attack dragon': 50, 'defense dragon': 5}


characters = {'A' : {'hp': 70 ,'attack': 10, 'defense': 5, 'mp':0, 'can steal':False}, 'B' : {'hp': 60, 'attack': 8, 'defense': 15, 'mp': 0, 'can steal':True}, 'C' : {'hp': 70, 'attack':8, 'defense': 10, 'mp':0, 'can steal':False}, 'D' : {'hp': 60, 'attack': 1, 'defense':4, 'mp':100, 'can steal':False}}

def character(character_set: dict)-> dict:
    print('versla de leider van het monsters in monster wood zodat onze onderdanen weer veilig zijn dat is mijn opdracht aan jullie als koning van dit land.')
    choose_character = input('choose character: A = fighter B = thief C = soldier D = mage')
    character = choose_character.upper()
    print(characters[character]["hp"])
    print(characters[character]["attack"])
    print(characters[character]["defense"])
    print(characters[character]["mp"])
    character_stats = characters[character]
    print(character_stats)
    return character_stats

def attack(stats: dict, foe:dict): 
    print(stats['attack'])
    attack_turn_1 = stats["attack"] - foe["defense dragon"]
    print(attack_turn_1)
    if attack_turn_1<0:
        attack_turn_1=0
    new_foe_hp = foe["hp dragon"] - attack_turn_1 
    foe.update({"hp dragon" : new_foe_hp})
    return print(f'{foe["hp dragon"]} hp dragon')

def defense(character_stats:dict,):
    new_defense_stat = stats['defense'] + 5
    character_stats.update({'defense': new_defense_stat})
    print(f'je nieuwe defense stat = {new_defense_stat}')

def steal_item(character_stats:dict, aantal_items:int):
    if character_stats["can steal"] == True:
        aantal_items += 1
        print(f'je hebt zoveel items {aantal_items}')
    else: print('je kunt niet stelen je turn heeft gefaald')

def use_spell(character_stats:dict, foe:dict):
    if character_stats['mp']>0:
        spell_type = input('choose spell: heal or fireball')
        if spell_type == 'heal':
            new_character_hp = character_stats['hp'] +30
            new_mp = character_stats['mp'] - 5 
            if new_character_hp > base_stat_hp_mage:
                new_character_hp = character_stats['hp']
                characters.update({'hp':new_character_hp})
                print('je hebt niet genoeg hp verloren dus je spell heeft gefaald')
        elif spell_type == 'fireball':
            new_foe_hp = foe['hp dragon'] - 10 
            new_mp = character_stats['mp'] - 5 
            foe.update({'hp dragon':new_foe_hp})
            characters.update({'mp':new_mp})
            print(f'je hebt zoveel mp {stats["mp"]} over')
            print(f'de draak heeft zoveel hp{foe["hp dragon"]}')
    else: print('je hebt geen mp dus kun je geen spell gebruiken je turn heeft gefaald')

def use_item(stats:dict, aantal_items: int):
    if stats['hp'] == 70 or 60:
        print('je hebt nog niet genoeg hp verloeren dus vergaat je item')
    else:
        new_character_hp = stats['hp'] + 30
    new_character_hp = stats['hp'] + 30 
    print(stats['hp'])
    aantal_items -=1 
    if new_character_hp > stats['hp']:
        new_character_hp = stats['hp']
        print('je hebt niet genoeg hp verloren dus vergaat het item')
    characters.update({'hp':new_character_hp})
    print(f'je hebt nog zoveel items over {aantal_items}')
    print(f'je hebt zoveel hp {stats["hp"]}')
    
def action_foe(stats:dict, foe:dict):
    # turn_foe = random.randint(0,1)
    # if turn_foe == 0: 
    #     new_foe_defense = foe['defense dragon'] + 5
    #     foe.update({'defense':new_foe_defense})
    #     print(f'de draak heeft zoveel defense {foe["defense dragon"]}')
    #     print('the dragon defended')  
    # if turn_foe == 1:
    attack_enemy = foe['attack dragon'] - stats['defense']
    new_character_hp = stats['hp'] - attack_enemy
    stats.update({'hp':new_character_hp})
    print(f'je hebt nog zoveel hp {stats["hp"]} over')
    print('the dragon attacked')

stats = character(characters)
print(stats)
while stats['hp'] > 0 or foe['hp dragon'] > 0:
    print(f'je hebt zoveel {aantal_punten} punten')
    turn_1 = input('choose action: use item, defend, attack, steal item, use spell')
    if turn_1 == 'attack':
        attack(stats,foe) 
    elif turn_1 == 'defend':
        defense(stats)
    elif turn_1 == 'use item':
        use_item(stats, aantal_items)
    elif turn_1 == 'steal item':
        steal_item(stats, aantal_items)
    elif turn_1 == 'use spell':
        use_spell(stats, foe)
    action_foe(stats, foe)
    aantal_punten -= 1 
    print(f'je hebt nog zoveel {aantal_punten} punten')
    meerspelen = input('wil je verder spelen?')
    if meerspelen == 'nee':
        break
    elif stats['hp'] < 0:
        break
    elif foe['hp dragon']<0:
        break
    if turn_1 == 'defend':
        new_defense_stat = stats['defense'] - 5
        character_stats.update({'defense': new_defense_stat})
        print(f'je defense stat is weer {new_defense_stat}')

if foe['hp dragon'] <0:
    print('you have defeated the dragon')
print('game over')






