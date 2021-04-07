from PIL import Image


 allTerritories = []
 numTerritories = 0
 print("Hello world")

dice = DiceRoller()
p1 = Player()
p2 = Player()
p3 = Player()
p4 = Player()
 
board = Image.open(r"C:\Users\steve\Desktop\risk.jpg")
data = open('riskdata.txt,' 'r')

board.show()

def gameInit():
        numTerritories += 1
        data = line.split("-")
        adjacentCountries = data[1].split(", ") #TODO: See if the brackets [] in riskdata.txt cause any problems with loading in these names
        pickTerritories(dice.roll("1d4"))
        allTerritories.append(country)

#Each country will start out with a random army count of 1-6
def playerOnePick():
    country = Territory(data[0], dice.getRoll("1d6"), adjacentCountries, p1) 

def playerTwoPick():
    country = Territory(data[0], dice.getRoll("1d6"), adjacentCountries, p2)

def playerThreePick():
    country = Territory(data[0], dice.getRoll("1d6"), adjacentCountries, p3)

def playerFourPick():
    country = Territory(data[0], dice.getRoll("1d6"), adjacentCountries, p4)

def pickTerritories(roll): 
    for line in data:
        switcher = {
            1: playerOnePick,
            2: playerTwoPick,
            3: playerThreePick,
            4: playerFourPick
        }
        switcher.get(roll, "Only four players allowed right now")



