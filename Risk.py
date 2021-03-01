from PIL import Image

class RiskML: 

countries = []
numTerritories = 0
print("Hello world")

dr = DiceRoller()
p1 = Player()
p2 = Player()
p3 = Player()
p4 = Player()
 
board = Image.open(r"C:\Users\steve\Desktop\risk.jpg")


board.show()

def getCountryData:
    data = open('riskdata.txt,' 'r')
    for line in data: # reading it line by line
        numTerritories += 1
        data = line.split("-")
        adjacentCountries = data[1].split(", ") #TODO: See if the brackets [] in riskdata.txt cause any problems with loading in these names
        country = Country(data[0], dr.getRoll("1d6"), adjacentCountries, dr.getRoll("1d4") )
        countries.append(country)

def reinforce():

def attack():

def fortify():



