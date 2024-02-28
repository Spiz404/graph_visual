from Node import Node
from Link import Link
from Graph import Graph
from collections import deque

def bfs(source : Node, graph : Graph):
    graphList = graph
    w = deque()
    w.append(source)
    vl = []
    visited = []
   
    while len(w) != 0:
        lab = w.popleft()
        if lab not in visited:
            visited.append(lab)
        print(visited)
        for element in graph[str(lab)]:
            print(str(element["node"].getLabel()) + " " + str(element["node"] not in visited))
            if element["node"] not in visited:
                visited.append(element["node"]) 
                w.append(element["node"])
                link = Link(lab, element["node"], element["w"])
                vl.append(link)
              

    print("lista visitati" + str(visited))
    print("links " + str(vl))
    return Graph(visited, vl)

def dfs(source : Node, graph : Graph):
    pass

def mst(graph : Graph):
    pass