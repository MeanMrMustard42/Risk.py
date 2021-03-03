print("Hello world")

name = "yermum"
Player occupyingPower = Player()
units = 0
connections = []

class Country:
    def __init__(name, units, connections, occupyingPower):
    self.name =  name
    self.units = units
    self.connections = connections
    self.occupyingPower = occupyingPower

# returns num of (surrounding hostile units/friendly units)/10. A higher rating means the territory is in more danger of being taken 
# on this turn.

#TODO: See if adding friendly surrounding units to the equation produces a more comprehensive rating
def getVulnerabilityRating():
    rating = 0
    for territory in connections:
        if territory.getName != self.getName():
            rating += territory.getUnits()
    rating = (rating/self.getUnits())/10
    return rating
        



def getReinforcements():


def getName(self):
    return self.name

def getUnits(self):
    return self.units

def getPower(self):
    return self.occupyingPower

def setUnits(self, newUnits):
    self.units = newUnits

def setPower(self, newPower):
    self.occupyingPower = newPower





def setNewPower() 


