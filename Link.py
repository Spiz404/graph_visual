class Link:
    
    def __init__(self, node1, node2, weight):
        self.head = node1
        self.tail = node2
        self.weight = weight

    def getHead(self):
        return self.head
    
    def getTail(self):
        return self.tail
    