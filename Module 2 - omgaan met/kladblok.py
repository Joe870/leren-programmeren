import random

HP_slime = 20 
attack_slime = 9 
defense_slime = 1
hp = 70 
attack_stat = 10
defense_stat = 5
mp = 0 
action_enemy = random.randint(0,1) 
if action_enemy == 1:
        attack_enemy = attack_slime - defense_stat - hp
elif action_enemy == 0:
        defense_slime = defense_slime + 5 
        print(action_enemy)