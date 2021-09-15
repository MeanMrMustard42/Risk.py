#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import re
import random


class Dice:

    positiveMod = False
    negativeMod = False
    isFlat = False  # seems paradoxical but will be fixed later

    # Debug method for game testing. Using random.org for true random rolls is fun but generating the random numbers clientside
    # for now will take so much less time

    def getNativeRoll(self, roll):
        total = 0
        if roll.find('+') == -1:  # if a plus sign is not found
            positiveMod = False
        if roll.find('-') == -1:  # if a minus sign is also not found - isFlat will be true
            negativeMod = False
        if roll.find('+') == -1 and roll.find('-') == -1:
            isFlat = True

        numList = re.findall(r'\d+', roll)  # putting all nums into an array (i.e. ['1', '6'] for 1d6)

        dieNum = int(numList[0])
        dieType = int(numList[1])
        if isFlat == False:
            modifier = numList[2]
        else:
            modifier = None

        if dieNum > 1:
            for x in range(dieNum):
                total += random.randint(1, dieType)
        else:
            total = random.randint(1, dieType)

        if dieNum == 1 and dieType == 1:  # if some idiot tries to roll 1d1
            total = 1

        if isFlat == False:  # if modifier is present
            if positiveMod == True:
                total = roll + modifier  # numList is actually a String array
        elif negativeMod == True:
            total = roll - modifier
        return total

    def getRoll(self, roll):
        if roll.find('+') == -1:  # if a plus sign is not found
            positiveMod = False
        if roll.find('-') == -1:  # if a minus sign is also not found - isFlat will be true
            negativeMod = False
        if roll.find('+') == -1 and roll.find('-') == -1:
            isFlat = True

        numList = re.findall(r'\d+', roll)  # putting all nums into an array

        dieNum = int(numList[0])
        dieType = int(numList[1])

        if isFlat == False:
            modifier = int(numList[2])
        else:
            modifier = None

        base_url = \
            'https://www.random.org/integers/?num={}&min={}&max={}&col=1&base=10&format=plain&rnd=new'
        url = base_url.format(dieNum, 1, dieType)
        response = requests.get(url)

        # if someone rolls more than one die, put all results in an array and add

        roll = 0

        if dieNum > 1:
            rollResults = re.findall(r'\d+', str(response.content))  # accounting for multiple dice being rolled
            for i in rollResults:
                roll += int(i)
        else:

              # will execute on a flat roll

            roll = int(response.content)
            total = roll

        if dieNum == 1 and dieType == 1:  # if some idiot tries to roll 1d1
            roll = 1

        if isFlat == False:  # if modifier is present
            if positiveMod == True:
                total = roll + modifier  # numList is actually a String array
        elif negativeMod == True:
            total = roll - modifier
        return total
