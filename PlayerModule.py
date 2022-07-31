#!/usr/bin/python
# -*- coding: utf-8 -*-

import DiceRoller
import TerritoryModule

extraArmies = 0

import copy
import TerritoryModule
dice = DiceRoller.Dice()

class Player:
    f = open('game.txt', 'w')

    playerNumber = 0

    def __init__(self, name = "bob"):
        self.name = name
        self.controlledTerritories = []
        self.numControlledTerritories = 0 
        self.reinforcing = False
        self.attacking = False
        self.fortifying = False
        self.IsOnTurn = False
        self.isDefeated = False
        
    
    def getName(self):
        return self.name

    def getTerritoriesNum(self):
        return self.numControlledTerritories

    def getControlledTerritoriesList(self):
        return self.controlledTerritories
    
    def addNewTerritory(self, newTerritory):
        self.controlledTerritories.append(newTerritory)
        self.numControlledTerritories += 1
        print("added new territory " + newTerritory.getName() + " to " + self.getName())



    def setControlledTerritories(self, newAmount):
        numControlledTerritories = newAmount

    # checking if all territories are controlled
    def hasWon(self, territoriesOnField):
        if self.numControlledTerritories >= territoriesOnField:
            return True
        else:
            return False

    def reinforce(self):
        global numControlledTerritories
        import copy
       # territory = TerritoryModule.Territory("dummy", 0, [], None)

        reinforcing = True
        isOnTurn = True
        extraArmies = self.numControlledTerritories / 3

        highestRating = 0
        lowestRating = -50
        for territory in self.controlledTerritories:
            if territory.getVulnerabilityRating() > lowestRating:
                mostVulnerable = copy.copy(territory)  # We might not actually need this either but keep it for now
                lowestRating = territory.getVulnerabilityRating()
                territory.setUnits(territory.getUnits() + extraArmies)  # putting all the armies into the most vulnerable one for now

    def attack(self):
        lowestRating = 100
        fightingCountries = self.getFightingTerritories()
        attacker = fightingCountries[0]
        defender = fightingCountries[1]

        attackingPower = attacker.getPower()
        defendingPower = defender.getPower()
        #global territory

        for invader in self.controlledTerritories:
            if invader.getVulnerabilityRating() < lowestRating \
                and not invader.isSafe:  # if the invader's vul rating is less than the lowest rating seen so far and the invader is next to a hostile country
                lowestRating = invader.getVulnerabilityRating()
                attacker = invader  # deep copy?

        highestRating = 10

        for territory in attacker.getHostileConnections():
            if territory.getVulnerabilityRating > highestRating:  # doing same thing here, trying to find hostile country w/ highest rating
                defender = territory

        # attack time

        for attempts in range(attacker.getUnits()):
            attack = dice.getNativeRoll('1d6')
            defense = dice.getNativeRoll('1d6')
            if defense >= attack:
                attacker.setUnits(attacker.getUnits() - 1)
            elif attack > defense:
                defender.setUnits(defender.getUnits() - 1)

            if defender.getUnits == 0:
                print (attacker.getPower() + ' takes control of ' \
                    + defender.getName + ' from ' + defender.getPower() \
                    + '!')
                defendingPower.setControlledTerritories(defendingPower.getTerritoriesNum() - 1)
                defender.setPower(attacker.getPower())
            elif attacker.getUnits == 1:
                print (attacker.getPower \
                    + 'cannot continue the attack from' \
                    + attacker.getName() + ', 1 army left')
                break

    # fortify the territory with the highest vulnerability rating
    # for use in fortify()

    def moveArmies(amount, territory, otherTerritory):
        if territory.isConnected(otherTerritory):
            territory.setUnits(territory.getUnits() - amount)
            otherTerritory.setUnits(otherTerritory.getUnits() + amount)
        else:
            print (territory.getName() + ' and ' \
                + otherTerritory.getName() + ' arent connected, whoops')

    # find connection with highest number of armies and give a proportional amount


    # find the territory with the lowest vul rating BUT borders at least one hostile territory.
    #returns both the attacking territory and the territory that is going to be attacked.

    #TODO: Sus things are goin in the for loop here - if statement never seems to return true
    def getFightingTerritories(self):
        idealAttacker = TerritoryModule.Territory('placeholder', 1, [], self)
        lowestVulRating = 1000
        for territory in self.controlledTerritories:
            if territory.getVulnerabilityRating() < lowestVulRating and not territory.isSafe():
                lowestVulRating = territory.getVulnerabilityRating()
                idealAttacker = territory  # deep copy?

        defender = self.getMVT(idealAttacker.getHostileConnections())

        return idealAttacker, defender
                        


    def getMVT(self, territoryList): # Most Vulnerable Territory, for use in fortify and attack
         mostVulnerable = TerritoryModule.Territory('placeholder', 1, [], self)
         highestVulRating = 10
         for territory in territoryList: # find most vulnerable territory
            if territory.getVulnerabilityRating() > highestVulRating:
                highestVulRating = territory.getVulnerabilityRating()
                mostVulnerable = territory  # deep copy?

         return mostVulnerable

    def fortify(self):
        mostArmies = 1
        donatingTerritory = TerritoryModule.Territory('placeholder', 1, [],
                self) #TODO: what to do about placeholders (if anything lol)?

        mostVulnerable = self.getMVT(self.controlledTerritories)

        for connection in mostVulnerable.getConnections(): # find territory to donate
            if mostVulnerable.isTerritoryFriendly(connection) and connection.getUnits >= mostArmies:
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

        isOnTurn = False
