
connections = []
name = "yermum"
units = 0

class Territory:
    import copy
    from Player import Player
    from DiceRoller import DiceRoller
    occupyingPower = Player()

    def __init__(self,name, units, connections, occupyingPower):
        self.name =  name
        self.units = units
        self.connections = connections
        self.occupyingPower = occupyingPower


    # returns num of (surrounding hostile units/friendly units)/10. A higher rating means the territory is in more danger of being taken 
    # on this turn.

    #TODO: See if adding friendly surrounding units to the equation produces a more comprehensive rating
    def getVulnerabilityRating(self):
        
        rating = 0
        global connections 

        for territory in connections:
            if territory.getPower != self.getPower(): # find countries played by hostile powers
                rating += territory.getUnits()
        rating = (rating/self.getUnits())/10 #ratio of other players units vs this countries' units/10
        return rating
            
    # Returns whether or not the country is safe. A country is safe if all surrounding countries are controlled by the player in question
    def isSafe(self):
        global connections
        
        for territory in connections:
            if(territory.getPower != self.getPower):
                return False
        return True


    def getReinforcements():
        pass


    def getName(self):
        return self.name

    def getUnits(self):
        return self.units

    def getPower(self):
        return self.occupyingPower

    def getConnections(self):
        return self.connections

    def getHostileConnections(self):
        hostileConnections = []
        for territory in connections:
            if(territory.getPower != self.getPower):
                hostileConnections.append(territory)

        return hostileConnections

    def setUnits(self, newUnits):
        self.units = newUnits

    def setPower(self, newPower):
        self.occupyingPower = newPower

    def isTerritoryFriendly(self, otherCountry): # returns if this country is owned by the same player as the invoked one
        return otherCountry.getPower == self.getPower

    def isConnected(self, otherTerritory):
        for territory in connections:
            if(territory.getName == self.getName()):
                return True
        return False




    def setNewPower():
        pass
