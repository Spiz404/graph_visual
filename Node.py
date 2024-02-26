class Node:
    def __init__(self, x, y, label):
        self.posx = x
        self.posy = y
        self.label = label

    def getPosition(self):
        return ((self.posx, self.posy))
    
    def getLabel(self):
        return self.label
    
    def updatePosition(self, newPosition):
        self.posx = newPosition[0]
        self.posy = newPosition[1]