class Node:
    def __init__(self, x, y):
        self.posx = x
        self.posy = y

    def getPosition(self):
        return ((self.posx, self.posy))
    
    def updatePosition(self, newPosition):
        self.posx = newPosition[0]
        self.posy = newPosition[1]