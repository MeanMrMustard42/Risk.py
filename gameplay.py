#!/usr/bin/python
# -*- coding: utf-8 -*-
# from PIL import Image

import DiceRoller
import PlayerModule
import TerritoryModule
import numpy #important for ML stuff later

allTerritories = []
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

# board = Image.open(r"C:\Users\steve\Desktop\risk.jpg")

with open('riskdata.txt') as f:
    data = f.readlines()


# board.show()

# Each country will start out with a random army count of 1-6
# TODO: Each territory in the territory's connection list should be Territory objects, not strings




def playerOnePick(territory):
    territory.setUnits(dice.getNativeRoll('1d6'))
    p1.addNewTerritory(territory)


def playerTwoPick(territory):
    territory.setUnits(dice.getNativeRoll('1d6'))
    p2.addNewTerritory(territory)



def playerThreePick(territory):
    territory.setUnits(dice.getNativeRoll('1d6'))
    p3.addNewTerritory(territory)



def playerFourPick(territory):
    territory.setUnits(dice.getNativeRoll('1d6'))
    p4.addNewTerritory(territory)


# linear search :')) should return a Territory object
def getTerritory(name):
    for territory in allTerritories:
        if territory.getName() == name:
            return territory
    print(name + " couldn't find " )
    return "fuck"

    
# Fills in every territory's connections. allTerritories should be full when this is called
def connectTerritories():
    global allTerritories
    for territory in allTerritories:
        index = 0
        for connection in territory.getConnections():
            territory.changeConnection(index, getTerritory(connection))
            index +=1
            print(connection)

def createTerritories(): 
    global numTerritories
    global data
    global allTerritories
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
        allTerritories.append(TerritoryModule.Territory(territoryData[0], 0, territoryConnections, dummy))
        index += 1
    connectTerritories()
    pickTerritories()


def pickTerritories():
    for territory in allTerritories:
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
    status = "Current scores: " + p1.getName() + " " + str(p1.getTerritoriesNum()) + " | " + p2.getName() + " " + str(p2.getTerritoriesNum()) + " | " \
    + p3.getName() + " " + str(p3.getTerritoriesNum()) + " | " + p4.getName() + " " + str(p4.getTerritoriesNum())
    return status


# TODO: why aren't the Beatles taking territories from each other :((
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
                
            #print(player.getName() + " has won " + str(player.getTerritoriesNum()) + " territories, out of " + str(numTerritories) + " in total")
            if player.hasWon(numTerritories):
                print('Player ' + player.getName() + ' has won!')
                gameIsRunning = False
                break


def main():
    play()


main()
