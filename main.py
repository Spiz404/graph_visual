import pygame as pg
from Node import Node 
import math 
from Link import Link

pg.init()

screen = pg.display.set_mode((800, 800))
clock = pg.time.Clock()
pg.display.set_caption("graph visual")

running = True
node_radius = 20
nodes = []
links = []
anchor = None

# colors
BACKGROUND_COLOR = "black"
NODE_COLOR = "white"
LINK_COLOR = "red"


def nearestNode(currentPosition, nodes):
    
    for node in nodes:
            
            nodePosition = node.getPosition()
            d = math.sqrt(math.pow(nodePosition[0] - position[0], 2) + math.pow(nodePosition[1] - position[1],2))

            if d <= node_radius:
                return node
    
    return None


while running:

    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    screen.fill(BACKGROUND_COLOR)

    left, middle, right = pg.mouse.get_pressed(3)

    # left mouse button click

    if left:

        anchor = None
        validPosition = True
        position = pg.mouse.get_pos()
        

        for node in nodes:
            nodePosition = node.getPosition()
            d = math.sqrt(math.pow(nodePosition[0] - position[0], 2) + math.pow(nodePosition[1] - position[1],2))

            if d <= 2 * node_radius:
                validPosition = False
                break
        
        if validPosition:
            nodes.append(Node(position[0], position[1]))


    # display nodes
    
    if right and anchor is not None:
        
        position = pg.mouse.get_pos()
        
        linkEnd = nearestNode(position, nodes)

        if linkEnd is not None:
            links.append(Link(anchor, linkEnd))
            anchor = None

    elif right and anchor is None:

        position = pg.mouse.get_pos()

        anchor = nearestNode(position, nodes)
        
    
    
    for link in links:
        pg.draw.line(screen, LINK_COLOR, link.getHead().getPosition(), link.getTail().getPosition(), 2)

    for node in nodes:
        pg.draw.circle(screen, NODE_COLOR, node.getPosition(), node_radius, 3)

    if anchor is not None:
        pg.draw.line(screen, LINK_COLOR, anchor.getPosition(), pg.mouse.get_pos(), 2)

    

    pg.display.flip()

    clock.tick(60)

pg.quit()