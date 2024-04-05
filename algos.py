from Node import Node
from Link import Link
from Graph import Graph
from collections import deque, defaultdict
import sys
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


def extractMin(nodes : dict, visitedList : list[Node]):

    min = sys.maxsize
    node = None
    for k, v in nodes.items():
        if v < min and k not in visitedList:
            min = v
            node = k
    
    return node

def mst(graph : Graph):
    
   
    nodes = graph.getNodes()
    if not nodes:
        return []
    print("nodes " + str(nodes))
    weights = defaultdict(lambda  : sys.maxsize)
    prec = defaultdict(lambda  : None)
    
    links = graph.getLinks()
    outLinks = []
    visited = []

    ll = graph.generateList()
    
    # selecting first node randomly
    node = nodes[random.randrange(0, len(nodes), 1)]
    weights[node] = 0
    prec[node] = node
    visited = 0
    visitedList = []

    # looping until every node has been visited
    while visited < len(nodes):

        # extracting min node
        minNode = extractMin(weights, visitedList)
        visitedList.append(minNode)
       
        visited += 1
       
        # getting node links
        nodeLinks = ll[str(minNode)]
    
        outLinks.append(Link(prec[minNode], minNode, weights[minNode]))
       
        # updating dict weight entry for adjacent nodes
        for e in nodeLinks:
            if weights[e["node"]] > e["w"]:
           
                weights[e["node"]] = e["w"]
                prec[e["node"]] = minNode
              
  
    for link in outLinks:
        if link.head == None or link.tail == None:
            print("None")

    for link in outLinks:
        print("link " + str(link.getHead()) + str(link.getHead())) 

    return Graph(nodes, outLinks)

# -- NEED REFACTOR -> BAD LINK WEIGHT LOOK UP
def dijkstra(graph : Graph, source : Node, dest : Node):
    
    if source == dest:
        return graph
    
    ll = graph.generateList()
    
    w = defaultdict(lambda : sys.maxsize)
    p = defaultdict(lambda : None)
    w[source] = 0
    visited = []
    app = [source]

    while True:

        node = extractMin(w, visited)
        
        # if I extract a node with w = inf it means that every reachable node has been visited
        
        if w[node] == sys.maxsize or len(visited) == len(graph.getNodes()) or node == dest:
            break

        visited.append(node)

        for n in ll[str(node)]:
            if w[n["node"]] > w[node] + n["w"]:
                w[n["node"]] = w[node] + n["w"]
                p[n["node"]] = node

    if p[dest] == None:
        return graph
    
    prec = dest
    outNodes = [dest]
    outLinks = []
    iter = 0
    
    while prec != source:
        iter += 1

        # searching for link between the nodes
        link = [l for l in graph.getLinks() if l.__eq__(Link(p[prec], prec, 1))]
        
        outLinks.append(link[0])
        prec = p[prec]
        outNodes.append(prec)
    
    return Graph(outNodes, outLinks)