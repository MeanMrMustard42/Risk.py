import requests
import re


class Dice:
    positiveMod = False
    negativeMod = False
    isFlat = False # seems paradoxical but will be fixed later


    def getRoll(self, roll):
        if (roll.find("+") == -1): #if a plus sign is not found
            positiveMod = False
        if (roll.find("-") == -1): # if a minus sign is also not found - isFlat will be true
            negativeMod = False
        if (roll.find("+") == -1 and roll.find("-") == -1):
            isFlat = True
            
            

        numList = re.findall(r'\d+', roll) #putting all nums into an array
        print(numList)

        dieNum = int(numList[0])
        dieType = int(numList[1])

        base_url = "https://www.random.org/integers/?num={}&min={}&max={}&col=1&base=10&format=plain&rnd=new"
        url = base_url.format(dieNum, 1, dieType)
        response = requests.get(url)

        #if someone rolls more than one die, put all results in an array and add
        roll = 0
        
        if dieNum > 1:
            rollResults = re.findall(r'\d+', str(response.content)) # accounting for multiple dice being rolled
            for i in rollResults:
                roll += int(i)
            
        elif dieNum == 1 and dieType == 1: # if some idiot tries to roll 1d1
            roll = 1

        else:
            roll = int(response.content)
            num = roll
        
        if isFlat == False: # if modifier is present
            if positiveMod == True:
                num = roll + int(numList[2])  #numList is actually a String array
        elif negativeMod == True:
            num = roll - int(numList[2])
            print(num)
        return num



    




            
             
    

