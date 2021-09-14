#!/usr/bin/python
# -*- coding: utf-8 -*-

import DiceRoller

placeholder = None # placeholder for a placeholder
attacker = None
defender = None

extraArmies = 0
numControlledTerritories = 0 # not sure how this will work as it's not within the scope of the class..but I guess I'll find out lmao
controlledTerritories = []

import copy
import TerritoryModule
dice = DiceRoller.Dice()


class Player:
    reinforcing = False
    attacking = False
    fortifying = False
    IsOnTurn = False
    isDefeated = False
    hasWon = False
    f = open("game.txt", "w")


    playerNumber = 0

    def __init__(self):
        attacker = TerritoryModule.Territory("placeholder", 1, [], placeholder)  # will hopefully have a very low vul rating
        defender = TerritoryModule.Territory("placeholder", 1, [], placeholder)  



 # reinforce most vulnerable territory

    def getTerritoriesNum():
        global numControlledTerritories
        return numControlledTerritories

    def setControlledTerritories(self, newAmount):
        global numControlledTerritories
        numControlledTerritories = newAmount

    def reinforce(self):
        import copy 

        reinforcing = True
        isOnTurn = True
        extraArmies = numControlledTerritories / 3
        highestRating = 0
        for territory in controlledTerritories:
            if territory.getVulnerabilityRating() > lowestRating:
                mostVulnerable = copy.copy(territory)  # We might not actually need this either but keep it for now
                lowestRating = territory.getVulnerabilityRating()


        territory.setUnits(territory.getUnits() + extraArmies)  # putting all the armies into the most vulnerable one for now


    def attack(self):
        lowestRating = 100
        global attacker
        global defender

        for invader in controlledTerritories:
            if (invader.getVulnerabilityRating < lowestRating #if the invader's vul rating is less than the lowest rating seen so far and the invader is next to a hostile country
                and not invader.isSafe):
                lowestRating = invader.getVulnerabilityRating
                attacker = invader #deep copy?

        highestRating = 10

        for territory in attacker.getHostileConnections:
            if territory.getVulnerabilityRating > highestRating: # doing same thing here, trying to find hostile country w/ highest rating
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
                print (attacker.getPower() + ' takes control of ' \
                    + defender.getName + ' from ' + defender.getPower() \
                    + '!')
                defender.setControlledTerritories()
                defender.setPower(attacker.getPower())
            elif attacker.getUnits == 1:
                print (attacker.getPower + 'cannot continue the attack from' 
                    + attacker.getName() + ', 1 army left')
                break


    # fortify the territory with the highest vulnerability rating

    # for use in fortify()

    def moveArmies(amount, territory, otherTerritory):
        if territory.isConnected(otherTerritory):
            territory.setUnits(territory.getUnits() - amount)
            otherTerritory.setUnits(otherTerritory.getUnits() + amount)
        else:
            print (territory.getName() + ' and ' + otherTerritory.getName() \
                + ' arent connected, whoops')


    # find connection with highest number of armies and give a proportional amount

    def fortify(self):
        mostVulnerable = TerritoryModule.Territory()
        highestVulRating = 10
        for territory in controlledTerritories:
            if territory.getVulnerabilityRating() > highestVulRating:
                highestVulRating = territory.getVulnerabilityRating()
                mostVulnerable = territory # deep copy?

        mostArmies = 1
        donatingTerritory = TerritoryModule.Territory()
        for connection in territory.getConnections:
            if (mostVulnerable.isTerritoryFriendly(connection) and connection.getUnits \
                >= mostArmies):
                mostArmies = connection.getUnits()
                donatingTerritory = connection

        if donatingTerritory.getUnits() > 1:
            if donatingTerritory.getUnits() > 9:  # Neither territory should have an army count below 1
                self.moveArmies(5, donatingTerritory, mostVulnerable)
            elif donatingTerritory.getUnits() > 6:
                self.moveArmies(3, donatingTerritory, mostVulnerable)
            elif donatingTerritory.getUnits() > 3:
                self.moveArmies(2, donatingTerritory, mostVulnerable)
            else:
                self.moveArmies(1, donatingTerritory, mostVulnerable)

        isOnTurn = False
