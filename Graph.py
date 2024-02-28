from Link import Link
from Node import Node
from collections import defaultdict
class Graph:

    def __init__(self):
        self.l = defaultdict(list)

    def newNode(self):
        self.l.append([])

    def linkNode(self, start, end):
        self.l[start].append(end)
    

    def genList(self, nodes : list[Node], links : list[Link]) -> dict:
        self.l = defaultdict(list)
        for link in links:
            head = link.getHead().getLabel()
            tail = link.getTail().getLabel()
            self.l[str(head)].append({"node" : tail, "w" : link.getWeight()})
            self.l[str(tail)].append({"node" : head, "w" : link.getWeight()})

        print(self.l)

        return self.l


