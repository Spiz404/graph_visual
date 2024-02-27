class Graph:

    def __init__(self):
        self.l = []

    def newNode(self):
        self.l.append([])

    def linkNode(self, start, end):
        self.l[start].append(end)
