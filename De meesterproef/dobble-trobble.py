import random
import sys

def dice_roll():
    red_dice = random.randint(1,6)
    blue_dice = random.randint(1,6)
    lijst_white_dice = [1,1,1,2,2,3]
    white_dice = random.sample(lijst_white_dice, k=1)
    return red_dice, blue_dice, white_dice

