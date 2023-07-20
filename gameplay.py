#!/usr/bin/python
# -*- coding: utf-8 -*-
# from PIL import Image

import DiceRoller
import PlayerModule
import TerritoryModule
import numpy #important for ML stuff later

#TODO: Update 7/20/23: Everything in this project seems to do what it's supposed to - the only problem is that
#since every player is running on the same predetermined AI script, the game quickly reaches a state where every player is trying to grab
#the same territory, leading to an infinite cycle where no player actually reaches the win condition. Therefore it might be
#time to research Machine Learning in Python and figure out how it can be best implemented into this project. Another idea worth
#considering is incorporating a tiny bit of randomness in the player AI, such that each player makes an occasional strategic "mistake", 
#helping the game go along and preventing the infinite loops we're dealing with now. Also it'd be probably be good to research
#how non-Machine Learning AI is done with online board games like chess and see if we can apply it here as well.

allTerritories = []
territoryMap = {}
adjacentCountries = []
numTerritories = 0
gameIsRunning = False

# f = open("game.txt", "w")

dice = DiceRoller.Dice()
p1 = PlayerModule.Player("John")
p2 = PlayerModule.Player("Paul")
p3 = PlayerModule.Player("George")
p4 = PlayerModule.Player("Ringo")

dummy = PlayerModule.Player("TBD")

players = [p1, p2, p3, p4]  # Might be interesting to support a dynamic amount of players later

with open('riskdata.txt') as f:
    data = f.readlines()

def playerOnePick(territory):
    territory.setUnits(dice.getNativeRoll('1d6'))
    p1.addNewTerritoryToList(territory)

def playerTwoPick(territory):
    territory.setUnits(dice.getNativeRoll('1d6'))
    p2.addNewTerritoryToList(territory)

def playerThreePick(territory):
    territory.setUnits(dice.getNativeRoll('1d6'))
    p3.addNewTerritoryToList(territory)

def playerFourPick(territory):
    territory.setUnits(dice.getNativeRoll('1d6'))
    p4.addNewTerritoryToList(territory)

# O(1) HashMap search :)
def getTerritory(name):
    return territoryMap[name]   
 
# Fills in every territory's connections. allTerritories should be full when this is called
def connectTerritories():
    for territory in territoryMap.values():
        for connectionName in territory.getConnections():
            territory.addConnection(connectionName, getTerritory(connectionName))

def createTerritories(): 
    global numTerritories
    global data
    global allTerritories
    global territoryMap

    index = 0
    
    for line in data:
        if '-' not in data[index]:
            index += 1
            continue

        numTerritories += 1
        territoryData = data[index].split(' - ')

        # preprocessing
        territoryData[0] = territoryData[0].strip()
        territoryData[0] = territoryData[0].replace('\n', '')

        territoryData[1] = territoryData[1].strip()
        territoryData[1] = territoryData[1].replace('\n', '')

        territoryConnections = territoryData[1].split(", ")
        connectionsMap = {}

        for territory_name in territoryConnections:
            connectionsMap[territory_name] = None # converting list to hashmap
            territoryName = territoryData[0]

        territory = TerritoryModule.Territory(territoryName, 0, connectionsMap, dummy)
        territoryMap[territoryName] = territory
        index += 1

    allTerritories = list(territoryMap.values()) # to be used if we need a list of all the territories

    connectTerritories()
    pickTerritories()


def pickTerritories():
    for territory in territoryMap.values():
        roll = dice.getNativeRoll('1d4')
        if roll == 1:
            playerOnePick(territory)
        elif roll == 2:
            playerTwoPick(territory)
        elif roll == 3:
            playerThreePick(territory)
        elif roll == 4:
            playerFourPick(territory)

def getGameStatus():
    status = "Current scores: " + p1.getName() + " " + str(p1.updateAndReturnControlledTerritories()) + " | " + \
    p2.getName() + " " + str(p2.updateAndReturnControlledTerritories()) + " | " \
    + p3.getName() + " " + str(p3.updateAndReturnControlledTerritories()) + " | " + p4.getName() + " " + \
    str(p4.updateAndReturnControlledTerritories())
    return status


# TODO: No player ever reaches a win condition (might be a good time to implement a basic ML algorithm)

# If you currently don't care about game updates or just want to debug something quickly, note that
# commenting out or removing the print statements that execute while the game is running will make the game run
# significantly faster when the code is ran on our local machine (#TODO: See if you can reduce O(n) time complexity to
# make this less of a problem in the future if possible - we've already implemented hashmaps which should help).
def play():
    createTerritories()
    gameIsRunning = True

    while gameIsRunning:
        for player in players:
            if not player.isDefeated():
                player.reinforce()
                player.attack()
                print(getGameStatus())
                player.fortify()
           
            if player.hasWon(numTerritories):
                print('Player ' + player.getName() + ' has won!')
                gameIsRunning = False
                break


def main():
    play()

main()
