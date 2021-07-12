

class Player:
import copy


gameIsRunning = False
reinforcing = False
attacking = False
fortifying = False

extraArmies = 0
numControlledTerritories = 0
controlledTerritories = []

dice = DiceRoller()
#def __init__():
# we might not need this

def reinforce(): #reinforce most vulnerable territory
    reinforcing = True
    extraArmies = numControlledTerritories/3
    highestRating = 0
    for territory in territories:
        if(territory.getVulnerabilityRating() > lowestRating):
            mostVulnerable = copy.deepcopy(territory) # We might not actually need this either but keep it for now
            lowestRating = territory.getVulnerabilityRating()
territory.setUnits(territory.getUnits() + extraArmies) # putting all the armies into the most vulnerable one for now
        


# find country w/ lowest vulnerability rating that is surrounded by at least one hostile country.
# A country with a low vulnerability rating yet is surrounded by a hostile country means that the country
# is more likely to have more available armies to use, rather than just being surrounded by friendly countries.

""" 
the idea here is to find the controlled territory w/ lowest rating (but still surrounded by at least one hostile territory) and then, from
the list of those hostile territories, attack the territory with the highest vulnerability rating 
"""
def attack():
    dice = DiceRoller()
    lowestRating = 100
    attacker = Territory() # will hopefully have a very low vul rating
    for invader in controlledTerritories:
        if(invader.getVulnerabilityRating < lowestRating and not invader.isSafe):
            attacker = invader


    highestRating = 10
    defender = Territory()
    for territory in countryWithLowestRating.getHostileConnections:
        if(territory.getVulnerabilityRating > highestRating):
            defender = territory

    #attack time

    for attempts in range(attacker.getUnits()):
        attack = dice.getRoll("1d6")
        defense = dice.getRoll("1d6")
        if(defense >= attack):
            attacker.setUnits(attacker.getUnits() - 1)
        elif (attack > defense):
            defender.setUnits(defender.getUnits() - 1)
        
        if(defender.getUnits == 0):
            print(attacker.getPower() + " takes control of " + defender.getName + " from " + defender.getPower() + "!")
            defender.setPower(attacker.getPower())
        elif(attacker.getUnits == 1):
            print(attacker.getPower + "cannot continue the attack from" + attacker.getName() +", 1 army left")
            break

#fortify the territory with the highest vulnerability rating   

def fortify():
    mostVulnerable = Territory():
    
