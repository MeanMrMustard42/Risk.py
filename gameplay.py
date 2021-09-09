#from PIL import Image
import DiceRoller
import PlayerModule
import TerritoryModule


allTerritories = []
adjacentCountries = []
numTerritories = 0
gameIsRunning = False
print("Hello world")
#f = open("game.txt", "w")

dice = DiceRoller.Dice()
p1 = PlayerModule.Player()
p2 = PlayerModule.Player()
p3 = PlayerModule.Player()
p4 = PlayerModule.Player()

players = [p1, p2, p3, p4] # Might be interesting to support a dynamic amount of players later
 
#board = Image.open(r"C:\Users\steve\Desktop\risk.jpg")
with open('riskdata.txt') as f:
    data = f.readlines()

#board.show()


#Each country will start out with a random army count of 1-6
def playerOnePick():
    global adjacentCountries
    country = TerritoryModule.Territory(data[0], dice.getRoll("1d6"), adjacentCountries, p1) 

def playerTwoPick():
    global adjacentCountries
    country = TerritoryModule.Territory(data[0], dice.getRoll("1d6"), adjacentCountries, p2)

def playerThreePick():
    global adjacentCountries
    country = TerritoryModule.Territory(data[0], dice.getRoll("1d6"), adjacentCountries, p3)

def playerFourPick():
    global adjacentCountries
    country = TerritoryModule.Territory(data[0], dice.getRoll("1d6"), adjacentCountries, p4)

def pickTerritories(roll):
    global numTerritories
    global data
    global allTerritories

    for line in data:
        temp = data[line].split("-")     
        numTerritories += 1
        adjacentCountries = data[line].split(", ") #TODO: See if the brackets [] in riskdata.txt cause any problems with loading in these names

        switcher = {
            1: playerOnePick,
            2: playerTwoPick,
            3: playerThreePick,
            4: playerFourPick
        }
        switcher.get(roll, "Only four players allowed right now")


def play():
    pickTerritories()
    gameIsRunning = True   


    while(gameIsRunning):
        for player in players:
            player.reinforce()
            player.attack()
            player.fortify()
            if(player.hasWon):
                print("Player " + player.getName() + " has won!")
                gameIsRunning = False
        
def main():
    print("what the fUCK is this running")
