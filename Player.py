#!/usr/bin/python
# -*- coding: utf-8 -*-


class Player:

    import copy


reinforcing = False
attacking = False
fortifying = False
IsOnTurn = False
isDefeated = False
hasWon = False

playerNumber = 0

extraArmies = 0
numControlledTerritories = 0
controlledTerritories = []


dice = DiceRoller()



def __init__():
    player

# reinforce most vulnerable territory

def getTerritoriesNum():
    return numControlledTerritories():

def setControlledTerritories(self, newAmount):
    numControlledTerritories = newAmount

def reinforce():
    reinforcing = True
    isOnTurn = True
    extraArmies = numControlledTerritories / 3
    highestRating = 0
    for territory in territories:
        if territory.getVulnerabilityRating() > lowestRating:
            mostVulnerable = copy.deepcopy(territory)  # We might not actually need this either but keep it for now
            lowestRating = territory.getVulnerabilityRating()


territory.setUnits(territory.getUnits() + extraArmies)  # putting all the armies into the most vulnerable one for now


def attack():
    dice = DiceRoller()
    lowestRating = 100
    attacker = Territory()  # will hopefully have a very low vul rating
    for invader in controlledTerritories:
        if invader.getVulnerabilityRating < lowestRating \
            and not invader.isSafe:
            attacker = invader

    highestRating = 10
    defender = Territory()
    for territory in countryWithLowestRating.getHostileConnections:
        if territory.getVulnerabilityRating > highestRating:
            defender = territory

    # attack time

    for attempts in range(attacker.getUnits()):
        attack = dice.getRoll('1d6')
        defense = dice.getRoll('1d6')
        if defense >= attack:
            attacker.setUnits(attacker.getUnits() - 1)
        elif attack > defense:
            defender.setUnits(defender.getUnits() - 1)

        if defender.getUnits == 0:
            print attacker.getPower() + ' takes control of ' \
                + defender.getName + ' from ' + defender.getPower() \
                + '!'
                defender.setControlledTerritories()
            defender.setPower(attacker.getPower())
        elif attacker.getUnits == 1:
            print attacker.getPower + 'cannot continue the attack from' \
                + attacker.getName() + ', 1 army left'
            break


# fortify the territory with the highest vulnerability rating

# for use in fortify()

def moveArmies(amount, territory, otherTerritory):
    if territory.isConnected(otherTerritory):
        territory.setUnits(territory.getUnits() - amount)
        otherTerritory.setUnits(otherTerritory.getUnits() + amount)
    else:
        print territory.getName() + ' and ' + otherTerritory.getName() \
            + ' arent connected, whoops'


# find connection with highest number of armies and give a proportional amount

def fortify():
    mostVulnerable = Territory()
    highestVulRating = 10
    for territory in controlledTerritories:
        if territory.getVulnerabilityRating() > highestVulRating:
            highestVulRating = territory.getVulnerabilityRating()
            mostVulnerable = territory

    mostArmies = 1
    donatingTerritory = Territory()
    for connection in territory.getConnections:
        if isTerritoryFriendly(connection) and connection.getUnits \
            >= mostArmies:
            mostArmies = connection.getUnits()
            donatingTerritory = connection

    if donatingTerritory.getUnits() > 1:
        if donatingTerritory.getUnits() > 9:  # Neither territory should have an army count below 1
            moveArmies(5, donatingTerritory, mostVulnerable)
        elif donatingTerritory.getUnits() > 6:
            moveArmies(3, donatingTerritory, mostVulnerable)
        elif donatingTerritory.getUnits() > 3:
            moveArmies(2, donatingTerritory, mostVulnerable)
        else:
            moveArmies(1, donatingTerritory, mostVulnerable)

    isOnTurn = False
