

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

def __init__():
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
        



def attack():
    # find country w/ lowest vulnerability rating that is surrounded by at least one hostile country.
    # A country with a low vulnerability rating yet is surrounded by a hostile country means that the country
    # is more likely to have more available armies to use, rather than just being surrounded by friendly countries.
    for invader in controlledTerritories:
        lowestRating = 10
        if(invader.getVulnerabilityRating < lowestRating and invader.)
        for target in invader.getConnections():





def fortify():


    

 