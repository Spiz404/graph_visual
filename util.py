import math
from constants import * 
from Node import Node
from Link import Link
from collections import defaultdict

def nearestNode(currentPosition, nodes):
    
    for node in nodes:
            
            nodePosition = node.getPosition()
            d = math.sqrt(math.pow(nodePosition[0] - currentPosition[0], 2) + math.pow(nodePosition[1] - currentPosition[1],2))

            if d <= NODE_RADIUS:
                return node
    
    return None

