#!/usr/bin/python
# -*- coding: utf-8 -*-
# from PIL import Image

import DiceRoller
import PlayerModule
import TerritoryModule

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

players = [p1, p2, p3, p4]  # Might be interesting to support a dynamic amount of players later

# board = Image.open(r"C:\Users\steve\Desktop\risk.jpg")

with open('riskdata.txt') as f:
    data = f.readlines()


# board.show()

# Each country will start out with a random army count of 1-6
# TODO: Each territory in the territory's connection list should be Territory objects, not strings


def playerOnePick(territoryInfo, connections):
    global adjacentCountries

    country = TerritoryModule.Territory(territoryInfo[0],
            dice.getNativeRoll('1d6'), connections, p1)
    p1.addNewTerritory(country)


def playerTwoPick(territoryInfo, connections):
    global adjacentCountries
    country = TerritoryModule.Territory(territoryInfo[0],
            dice.getNativeRoll('1d6'), connections, p2)
    p2.addNewTerritory(country)



def playerThreePick(territoryInfo, connections):
    global adjacentCountries
    country = TerritoryModule.Territory(territoryInfo[0],
            dice.getNativeRoll('1d6'), connections, p3)
    p3.addNewTerritory(country)



def playerFourPick(territoryInfo, connections):
    global adjacentCountries
    country = TerritoryModule.Territory(territoryInfo[0],
            dice.getNativeRoll('1d6'), connections, p4)
    p4.addNewTerritory(country)



def pickTerritories(): 
    global numTerritories
    global data
    global allTerritories
    index = 0

    for line in data:

        if '-' not in data[index]:
            index += 1
            continue

        territoryData = data[index].split('-')
        territoryConnections = territoryData[1].split(", ")
        numTerritories += 1
        roll = dice.getNativeRoll('1d4')
        if roll == 1:
            playerOnePick(territoryData, territoryConnections)
        elif roll == 2:
            playerTwoPick(territoryData, territoryConnections)
        elif roll == 3:
            playerThreePick(territoryData, territoryConnections)
        elif roll == 4:
            playerFourPick(territoryData, territoryConnections)
        index += 1


def play():
    pickTerritories()
    gameIsRunning = True

    while gameIsRunning:
        for player in players:
            player.reinforce()
            player.attack()
            player.fortify()
            print(player.getName() + " has won " + str(player.getTerritoriesNum()) + " territories, out of " + str(numTerritories) + " in total")
            if player.hasWon(numTerritories):
                print('Player ' + player.getName() + ' has won!')
                gameIsRunning = False


def main():
    play()


main()
