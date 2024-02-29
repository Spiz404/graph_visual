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
   
        for element in graph[str(lab)]:  
            if element["node"] not in visited:
                visited.append(element["node"]) 
                w.append(element["node"])
                link = Link(lab, element["node"], element["w"])
                vl.append(link)
              

    return Graph(visited, vl)

# TODO ALL THIS ALGOS

def dfs(source : Node, graph : Graph):
    pass

def mst(graph : Graph):
    pass

def dijkstra(graph : Graph, source : Node, dest : Node):
    pass