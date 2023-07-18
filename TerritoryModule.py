#!/usr/bin/python
# -*- coding: utf-8 -*-

# from DiceRoller import DiceRoller

import copy

connections = []


class Territory:

    isGeneric = False

    def __init__(self, name, units, connections, occupyingPower):
        import PlayerModule
        self.name = name
        self.units = units
        self.connections = connections
        self.occupyingPower = occupyingPower
        if occupyingPower is None:  # if occupyingPower is null, don't try to make it a Player object
            self.isGeneric = True
        else:
            occupyingPower = PlayerModule.Player()

    # returns num of (surrounding hostile units/friendly units)/10. A higher rating means the territory is in more danger of being taken
    # on this turn.

    # TODO: See if adding friendly surrounding units to the equation produces a more comprehensive rating

    def getVulnerabilityRating(self):
        if self.getUnits() == 0:
            self.setUnits(1)

        rating = 0
        for territory in self.connections:
            if territory.getPower != self.getPower():  # find countries played by hostile powers
                rating += territory.getUnits()
        rating = rating / self.getUnits() / 10  # ratio of other players units vs this countries' units/10
        return rating

    # Returns whether or not the country is safe. A country is safe if all surrounding countries are controlled by the player in question

    def isSafe(self):
        for territory in self.connections:
            if territory.getPower() != self.getPower():
                return False
        return True

    def getReinforcements(): #TODO: Do we still need this?
        pass

    def getName(self):
        return self.name

    def getUnits(self):
        return self.units

    def getPower(self):
        return self.occupyingPower

    def getConnections(self):
        return self.connections
    
    def changeConnection(self, index, newConnection):
        self.connections[index] = newConnection

    def getHostileConnections(self):
        global connections
        hostileConnections = []
        for territory in self.connections:
            if territory.getPower() != self.getPower():
                hostileConnections.append(territory)

        return hostileConnections

    def setUnits(self, newUnits):
        self.units = newUnits

    def setPower(self, newPower):
        self.occupyingPower = newPower

    def isTerritoryFriendly(self, otherCountry):  # returns if this country is owned by the same player as the invoked one
        return otherCountry.getPower == self.getPower

    def isConnected(self, otherTerritory):
        for territory in connections:
            if territory.getName == self.getName():
                return True
        return False

    def setNewPower():
        pass
