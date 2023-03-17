import time
from termcolor import colored
from data import JOURNEY_IN_DAYS
from data import mainCharacter
from data import cost_food_human_copper_per_day
from data import cost_food_horse_copper_per_day
from data import friends
from data import cost_horse_silver_per_day
from data import cost_tent_gold_per_week
import math 

##################### M04.D02.O2 #####################

def copper2silver(amount:int) -> float:
    return amount / 10

def silver2gold(amount:int) -> float:
    return amount / 5

def copper2gold(amount:int) -> float:
    return silver2gold(copper2silver(amount))

def platinum2gold(amount:int) -> float:
    return amount * 25

def getPersonCashInGold(personCash:dict) -> float:
    return silver2gold(personCash['silver']) + copper2gold(personCash['copper']) + platinum2gold(personCash['platinum']) + personCash['gold']

##################### M04.D02.O4 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    ultimate_food_cost = ((horses * cost_food_horse_copper_per_day) + (cost_food_human_copper_per_day * people)) * JOURNEY_IN_DAYS
    print(ultimate_food_cost)
    return round(copper2gold(ultimate_food_cost),2)

##################### M04.D02.O5 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    new_list = []
    for element in list:
        if element[key] == value:
            new_list.append(element)
    return new_list


def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs(friends, 'adventuring', True)

def getShareWithFriends(friends:list) -> int:
    return getFromListByKeyIs(friends, 'shareWith', True)

def getAdventuringFriends(friends:list) -> list:
    return getFromListByKeyIs(friends, 'adventuring', True) and getFromListByKeyIs(friends, 'shareWith', True)


##################### M04.D02.O6 #####################

def getNumberOfHorsesNeeded(people:int) -> int:
    return math.ceil(people / 2)

def getNumberOfTentsNeeded(people:int) -> int:
    return math.ceil(people / 3)  

def getTotalRentalCost(horses:int, tents:int) -> float:
    horse_days = getNumberOfHorsesNeeded(len(friends)) * JOURNEY_IN_DAYS
    horse_prijs = horse_days * cost_horse_silver_per_day
    tent_days = (JOURNEY_IN_DAYS/7)
    math.ceil(tent_days)
    uiteindelijke_tent_days=tent_days * getNumberOfTentsNeeded(len(friends))
    tent_prijs = uiteindelijke_tent_days * cost_tent_gold_per_week
    return horse_prijs + tent_prijs

##################### M04.D02.O7 #####################

def getItemsAsText(items:list) -> str:
    pass

def getItemsValueInGold(items:list) -> float:
    pass

##################### M04.D02.O8 #####################

def getCashInGoldFromPeople(people:list) -> float:
    pass

##################### M04.D02.O9 #####################

def getInterestingInvestors(investors:list) -> list:
    pass

def getAdventuringInvestors(investors:list) -> list:
    pass

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    pass

##################### M04.D02.O10 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    pass

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    pass

##################### M04.D02.O12 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    pass

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    pass

##################### M04.D02.O13 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

##################### view functions #####################
def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()