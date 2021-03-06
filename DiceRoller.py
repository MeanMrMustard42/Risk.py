import requests
import re

class DiceRoller:


    print("Enter in your dice roll (1d20, 3d6, etc)...")

input = input()
positiveMod = True

def getRoll(roll):
    if input.find("+") == -1: #if a plus sign is not found
    positiveMod = False
    numList = re.findall(r'\d+', input) #putting all nums into an array
    print(numList)
    dieNum = int(numList[0])
    dieType = int(numList[1])
    base_url = "https://www.random.org/integers/?num={}&min={}&max={}&col=1&base=10&format=plain&rnd=new"
    url = base_url.format(dieNum, 1, dieType)
    response = requests.get(url)
    #if someone rolls more than one die, put all results in an array and add
    roll = 0
    
    if dieNum > 1:
     rollResults = re.findall(r'\d+', str(response.content)) 
     for i in rollResults:
         roll += int(i)
    
    elif dieNum == 1 and dieType == 1: # if some idiot tries to roll 1d1
    roll = 1
    else:
    roll = int(response.content)
    num = roll
    
    if len(numList) > 2: # if modifier is present
    if positiveMod == True:
        num = roll + int(numList[2])  #numList is actually a String array
    elif positiveMod ==  False:
        num = roll - int(numList[2])
        print(num)
    return num



    




            
             
    

