class Graph:

    def __init__(self):
        self.l = {}

    def newNode(self):
        self.l.append([])

    def linkNode(self, start, end):
        self.l[start].append(end)
    

    def genList(self, nodes, links):
        
        for link in links:
            head = link.getHead().getLabel()
            tail = link.getTail().getLabel()
            self.l[str(head)].append(tail)
            self.l[str(tail)].append(head)


