from Node import Node
from Link import Link
from Graph import Graph
from collections import deque

def bfs(source : Node, graph : Graph):

    print("bfs, source " + str(source.getLabel()))
    graphList = graph
    w = deque()
    w.append(source)
    vl = []
    visited = [source]
   
    while len(w) != 0:
        print("iterazione")
        lab = w.popleft()
        visited.append(lab)
        print("adj list node " + str(lab.getLabel()) + " " + str(graph[str(lab)]))
        for element in graph[str(lab)]:
            if element["node"] not in visited: 
                print("elemento " + str(element))
                w.append(element["node"])
                vl.append(Link(lab, element["node"], element["w"]))

    print(visited)
    return Graph(visited, vl)

def dfs(source : Node, graph : Graph):
    pass

def mst(graph : Graph):
    pass