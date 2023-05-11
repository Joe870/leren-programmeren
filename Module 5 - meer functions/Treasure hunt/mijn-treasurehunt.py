import time
from termcolor import colored
from data import *
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
    ultimate_food_cost = ((horses * COST_FOOD_HORSE_COPPER_PER_DAY) + (COST_FOOD_HUMAN_COPPER_PER_DAY * people)) * JOURNEY_IN_DAYS
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
    horse_prijs = horses * JOURNEY_IN_DAYS * COST_HORSE_SILVER_PER_DAY
    tent_prijs = tents * COST_TENT_GOLD_PER_WEEK * math.ceil(JOURNEY_IN_DAYS/7)
    return silver2gold(horse_prijs) + tent_prijs

##################### M04.D02.O7 #####################

def getItemsAsText(items:list) -> str:
    lijst = []
    for item in items:
        lijst_text = f"{item['amount']}{item['unit']} {item['name']}"
        lijst.append(lijst_text)
    print(lijst)
    return ', ' .join(lijst)

def getItemsValueInGold(items:list) -> float:
    hoeveelheid_goud = 0
    for element in items:
        if element['price']['type']=='copper':
            hoeveelheid_goud += copper2gold(element['price']['amount'] * element['amount'])
        elif element['price']['type']=='silver':
            hoeveelheid_goud += silver2gold(element['price']['amount'] * element['amount'])
        elif element['price']['type']=='platinum':
            hoeveelheid_goud += platinum2gold(element['price']['amount'] * element['amount'])
        elif element['price']['type'] == 'gold':
            hoeveelheid_goud += (element['price']['amount'] * element['amount'])
    print(hoeveelheid_goud)
    return hoeveelheid_goud

##################### M04.D02.O8 #####################

def getCashInGoldFromPeople(people:list) -> float:
    new_gold = 0
    for elements in people:
        new_gold  += copper2gold(elements['cash']['copper'])
        new_gold += silver2gold(elements['cash']['silver'])
        new_gold += platinum2gold(elements['cash']['platinum'])
        new_gold += elements['cash']['gold']
        print(new_gold)
    return round(new_gold, 2)

##################### M04.D02.O9 #####################

def getInterestingInvestors(investors:list) -> list:
    new_list = []
    for element in investors:
        if element['profitReturn'] <= 10:
            new_list.append(element)
    return new_list


def getAdventuringInvestors(investors:list) -> list:
    investors_list = []
    for element in getInterestingInvestors(investors):
        if element['adventuring'] == True:
            investors_list.append(element)
    return investors_list

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    total_cost_investors = 0
    item_cost = 0
    good_investors = getAdventuringInvestors(investors)
    print(good_investors)
    amount_horses = len(good_investors)
    amount_tents = len(good_investors)
    total_rent_cost = getTotalRentalCost(amount_horses, amount_tents)
    food_cost = getJourneyFoodCostsInGold(len(good_investors), amount_horses)
    for investors in good_investors:
        item_cost += getItemsValueInGold(gear) 
    total_cost_investors = food_cost + total_rent_cost + item_cost
    return total_cost_investors

##################### M04.D02.O10 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    prijs_inn_human = silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT * people)
    print(f'{prijs_inn_human} mens')
    prijs_inn_horse = copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT * horses)
    print(f'{prijs_inn_horse} paard')
    uiteindelijke_prijs = (leftoverGold // (prijs_inn_horse + prijs_inn_human))
    print(uiteindelijke_prijs)
    return math.floor(leftoverGold / (prijs_inn_horse + prijs_inn_human))
    

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    prijs_inn_human = silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT * people)
    prijs_inn_horse = copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT * horses)
    return round(nightsInInn * (prijs_inn_horse + prijs_inn_human),2)
    

##################### M04.D02.O12 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    investorsprofit =[]
    profittekst = 0
    good_investors = getInterestingInvestors(investors)
    for element in good_investors:
        profittekst = profitGold /100 * element['profitReturn']
        profittekst = round(profittekst,2)
        investorsprofit.append(profittekst)
    return investorsprofit

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    for elements in investorsCuts:
        profitGold = profitGold - elements 
    friendprofit = profitGold / fellowship
    friendprofit = round(friendprofit,2)
    return friendprofit


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