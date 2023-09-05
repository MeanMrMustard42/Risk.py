#!/usr/bin/python
# -*- coding: utf-8 -*-

# from DiceRoller import DiceRoller

import copy

connections = {}

class Territory:

    isDebugPlaceholder = False # we may not need these flags, going to leave them in for now tho till we overhaul player AI
    territoryIsSafe = True

    def __init__(self, name, units, connections, occupyingPower):
        import PlayerModule
        self.name = name
        self.units = units
        self.connections = connections
        self.occupyingPower = occupyingPower
        if self.name.find("placeholder") != -1:  # trigger placeholder flag
            self.isDebugPlaceholder = True
        else:
            occupyingPower = PlayerModule.Player()

    # Returns whether or not the country is safe. A country is safe if all surrounding countries
    # are controlled by the player in question. Higher rating = more vulnerable territory
    # TODO: See if adding friendly surrounding units to the equation produces a more comprehensive rating
    def isSafe(self):
        for territory in self.connections.values():
            #print("isSafe connections for " + self.getName() + ": " + self.getConnectionListStr() + ". Checking " + territory.getName())
            if territory.getPower() != self.getPower():
                #print(self.getName() + " is not safe, because " + territory.getName() + " is owned by " + territory.getPower().getName())
                self.territoryIsSafe = False  
                return False
        #print(self.getName() + " is safe!")
        self.territoryIsSafe = True
        return True
    
    # higher rating = more vulnerable
    def getVulnerabilityRating(self):
        if self.getUnits() == 0:
            self.setUnits(1)

        rating = 0
        for territory in self.getHostileConnections().values():
                if territory.getUnits() > 1: # territories with only 1 unit can't attack, so why should they be in the vul rating?
                    rating += territory.getUnits()
        rating = rating / self.getUnits() / 10  # ratio of other players units vs this countries' units/10
        return rating

    def getName(self):
        return self.name

    def getUnits(self):
        return self.units

    def getPower(self):
        return self.occupyingPower

    def getConnections(self):
        return self.connections
    
    def getConnectionListStr(self):
        connectionsStr = ", ".join([territory.getName() for territory in self.connections])
        return connectionsStr
    
    def addConnection(self, connectionName, newConnection):
        self.connections[connectionName] = newConnection

    # returns hashmap of territories connected to this territory that are controlled by different players
    def getHostileConnections(self):
        hostileConnections = {}
        for territory in self.connections.values():
            if territory.getPower() != self.getPower():
               hostileConnections[territory.getName()] = territory

        return hostileConnections

    def setUnits(self, newUnits):
        self.units = newUnits

    def setPower(self, newPower):
        self.occupyingPower = newPower
        
    # returns if this country is owned by the same player as the invoked one
    def isTerritoryFriendly(self, otherCountry): 
        return otherCountry.getPower() == self.getPower()

    def isConnected(self, otherTerritory):
        if otherTerritory in self.connections.values():
            return True
        else:
            return False