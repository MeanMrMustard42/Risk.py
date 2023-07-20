#!/usr/bin/python
# -*- coding: utf-8 -*-

import DiceRoller
import TerritoryModule

extraArmies = 0

import copy
import numpy # ML stuff
import TerritoryModule
dice = DiceRoller.Dice()

class Player:
    f = open('game.txt', 'w')
    playerNumber = 0

    def __init__(self, name = "bob"): # bob is placeholder
        self.name = name
        self.controlledTerritories = {}
        self.numControlledTerritories = 0 
        self.reinforcing = False
        self.attacking = False
        self.fortifying = False
        self.IsOnTurn = False
         
    def getName(self):
        return self.name

    def updateAndReturnControlledTerritories(self):
        self.numControlledTerritories = len(self.controlledTerritories)
        return self.numControlledTerritories

    def getControlledTerritoriesList(self):
        return self.controlledTerritories

    # adds and removes territories from the controlled territories list, respectively
    def addNewTerritoryToList(self, newTerritory):
        self.controlledTerritories[newTerritory.getName()] = newTerritory
        newTerritory.setPower(self)
        print("added new territory " + newTerritory.getName() + " to " + self.getName())
        self.updateAndReturnControlledTerritories()

    def removeTerritoryFromList(self, territoryToRemove):
        del self.controlledTerritories[territoryToRemove.getName()]
        self.updateAndReturnControlledTerritories()
                
    def setControlledTerritories(self, newAmount):
        self.numControlledTerritories = newAmount

    # detects if a player has territories and is thus still in the game
    def isDefeated(self):
        if self.numControlledTerritories <= 0:
            self.numControlledTerritories = 0
            #print(self.getName() + " is defeated!")
            return True
        return False
    
    # checking if all territories are controlled
    def hasWon(self, territoriesOnField):
        if self.numControlledTerritories >= territoriesOnField:
            return True
        else:
            return False

    def getFightingTerritories(self):
        idealAttacker = TerritoryModule.Territory('placeholder', 1, [], self)
        lowestVulRating = 1000
        for territory in self.controlledTerritories.values():
            if territory.getVulnerabilityRating() < lowestVulRating and not territory.isSafe() and territory.getUnits() > 1:
                lowestVulRating = territory.getVulnerabilityRating()
                idealAttacker = territory  # deep copy?
                #print(idealAttacker.getName() + " has connections " + idealAttacker.getConnectionListStr())

        defender = self.getMVT(idealAttacker.getHostileConnections())
        return idealAttacker, defender

  # The overall most vulnerable territory that is currently controlled by this player
  # higher rating = more vulnerable as always
    def getOverallMVT(self):
        if not self.controlledTerritories:
            return
        elif len(self.controlledTerritories) == 1:
            tempList = list(self.controlledTerritories.values())
            return tempList[0]
        else:
            MVT = TerritoryModule.Territory('placeholder', 1, [], self)
            highestRating = -100
            for territory in self.controlledTerritories.values():
                if territory.getVulnerabilityRating() > highestRating:
                    MVT = territory # deep copy? maybe
                    return MVT

    def getMVT(self, territoryList): # Most Vulnerable Territory, for use in fortify and attack
         mostVulnerable = TerritoryModule.Territory('placeholder', 1, [], self)
         highestVulRating = -100

         for territory in territoryList.values(): # find most vulnerable territory
            if territory.getVulnerabilityRating() > highestVulRating:
                highestVulRating = territory.getVulnerabilityRating()
                mostVulnerable = territory  # deep copy?
        
         return mostVulnerable


    def reinforce(self):
        extraArmies = int(self.numControlledTerritories / 3)
        self.getOverallMVT().setUnits(self.getOverallMVT().getUnits() + extraArmies)  # putting all the armies into the most vulnerable one for now

    def attack(self):
        fightingCountries = self.getFightingTerritories()
        attacker = fightingCountries[0]
        defender = fightingCountries[1]

        attackingPower = attacker.getPower()
        defendingPower = defender.getPower()

        if attacker.getUnits() == 1:
            return # you can't attack if your best territory has only 1 unit left

        if attackingPower == defendingPower:
            print("Sadge: " + attackingPower.getName() + " equals " + defendingPower.getName())

        # attack time - simplified for the sake of processing time, but maybe we can increase the complexity without
        # increasing the processing time in the future.
        attackRoll = str(attacker.getUnits()) + "d6"
        defenseRoll = str(defender.getUnits()) + "d6"
        attack = dice.getNativeRoll(attackRoll)
        defense = dice.getNativeRoll(defenseRoll)
        print(attacker.getName() + ", controlled by " + attacker.getPower().getName() + ", is attacking " +
            defender.getName() + ", controlled by " + defender.getPower().getName())
        if defense >= attack:
            if defense - attack <= 0:
                attacker.setUnits(1)
        elif attack > defense:
            print(attacker.getPower().getName() + ' takes control of ' \
            + defender.getName() + ' from ' + defender.getPower().getName() \
            + '!')
            defender.getPower().removeTerritoryFromList(defender)
            defender.setUnits(1)
            attacker.getPower().addNewTerritoryToList(defender)
   
    # for use in fortify()
    def moveArmies(self, amount, territory, otherTerritory):
        if territory.isConnected(otherTerritory):
            territory.setUnits(territory.getUnits() - amount)
            otherTerritory.setUnits(otherTerritory.getUnits() + amount)
        else:
            print (territory.getName() + ' and ' \
                + otherTerritory.getName() + ' arent connected, whoops')

    # find connection with highest number of armies and give a proportional amount
    def fortify(self):
        mostArmies = 1
        donatingTerritory = TerritoryModule.Territory('placeholder', 1, [], self)
        mostVulnerable = self.getOverallMVT()

        for connection in mostVulnerable.getConnections().values(): # find territory to donate
            if mostVulnerable.isTerritoryFriendly(connection) and connection.getUnits() > mostArmies:
                mostArmies = connection.getUnits()
                donatingTerritory = connection # again, deep copy?

        if donatingTerritory.getUnits() > 1:
            if donatingTerritory.getUnits() > 9:  # Neither territory should have an army count below 1
                self.moveArmies(5, donatingTerritory, mostVulnerable)
            elif donatingTerritory.getUnits() > 6:
                self.moveArmies(3, donatingTerritory, mostVulnerable)
            elif donatingTerritory.getUnits() > 3:
                self.moveArmies(2, donatingTerritory, mostVulnerable)
            else:
                self.moveArmies(1, donatingTerritory, mostVulnerable)

