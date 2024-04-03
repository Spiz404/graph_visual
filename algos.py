from Node import Node
from Link import Link
from Graph import Graph
from collections import deque
import random

# bfs visit, return visit tree

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

# dfs visit, return visit forest

def dfs(graph : Graph):

    nodes = graph.getNodes()
    links = graph.getLinks()
    ll = graph.generateList()
    outLinks = []
    visited = []

    def visit(node):
        if node not in visited:
            visited.append(node)
            for element in ll[str(node)]:
                if element["node"] not in visited:
                    outLinks.append(Link(node, element["node"], element["w"]))
                    visit(element["node"])

    for node in nodes:
        if node not in visited:
            visit(node)

    return Graph(visited, outLinks)

def mst(graph : Graph):
    
    fringe = []
    nodes = graph.getNodes()
    if not nodes:
        return []
    
    links = graph.getLinks()
    outLinks = []
    visited = []

    ll = graph.generateList()
    
    # selecting first node randomly
    node = nodes[random.randrange(0, len(nodes), 1)]
    
    # looping until every node has been visited
    while len(visited) < len(nodes):
        
        # getting node links
        nodeLinks = ll[str(node)]
        print(nodeLinks)
    

def dijkstra(graph : Graph, source : Node, dest : Node):
    pass