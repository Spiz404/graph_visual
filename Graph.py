from Link import Link
from Node import Node
from collections import defaultdict
import util as util
import pygame
import math
from constants import *
class Graph:

    def __init__(self):
        self.nodes = list()
        self.links = list()
        self.l = defaultdict(list)
    
    # adding a new node
    def addNode(self, node : Node):

        validPosition = True

        p = node.getPosition()
        for n in self.getNodes():
        
            nodePosition = n.getPosition()
            d = math.sqrt(math.pow(nodePosition[0] - p[0], 2) + math.pow(nodePosition[1] - p[1],2))
            
            if d <= 2 * NODE_RADIUS:
                validPosition = False
                break
        
        if validPosition:
            self.nodes.append(node)

    def getLinks(self) -> list[Link]:
        return self.links
    
    def getNodes(self) -> list[Node]:
        return self.nodes

    # adding a new link
    def addLink(self, link : Link) -> bool:
        
        # check if link doesn't already exists
        if link not in self.getLinks():
            self.links.append(link)
            return True
        
        return False

    # remove a node and all his links
    def removeNode(self, node : Node):
        self.nodes.remove(node)
        nodePosition = node.getPosition()
        # removing node links
        self.links = [link for link in self.links if link.getHead() != node and link.getTail() != node]
    
    # render the whole graph
    def renderGraph(self, screen : pygame.surface):

        for link in self.links:
            link.render(screen)
        
        for node in self.nodes:
            node.render(screen)


    def generateList(self):
        print("here")
        print(self.getLinks())
        return util.genList(self.getNodes(), self.getLinks())