class Link:
    
    def __init__(self, node1, node2, weight):
        self.head = node1
        self.tail = node2
        self.weight = weight

    def getHead(self):
        return self.head
    
    def getTail(self):
        return self.tail
    
    def __str__(self):
        return f'head {self.head} tail {self.tail} weight {self.weight}'
    
    def __eq__(link1, link2):
        return (link1.getHead().getPosition() == link2.getHead().getPosition() and link1.getTail().getPosition() == link2.getTail().getPosition()
                or link1.getHead().getPosition() == link2.getTail().getPosition() and link1.getTail().getPosition() == link2.getHead().getPosition())
