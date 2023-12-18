import pygame
from Node import Node 
import math
from Link import Link
from util import nearestNode
from constants import *

pygame.init()

screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
pygame.display.set_caption("graph visual")

running = True

nodes = []
links = []
anchor = None
deleteMode = False

# font
font = pygame.font.Font('freesansbold.ttf', 32)

# app texts

deleteText = font.render("DELETE MODE", True, "red")
deleteTextRect = deleteText.get_rect()
deleteTextRect.center = (400, 740)


while running:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # checking if D pressed
        elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    deleteMode = not deleteMode

    screen.fill(BACKGROUND_COLOR)


    # check for keyboard input

    keyboardInput = pygame.key.get_pressed()
    
  


    left, middle, right = pygame.mouse.get_pressed(3)

    # left mouse button click
    if left and deleteMode:

        position = pygame.mouse.get_pos()

        node = nearestNode(position, nodes)
        
        if node is not None:
            nodePosition = node.getPosition()
            # remove all node links
            links = [link for link in links if link.getHead().getPosition() != nodePosition and link.getTail().getPosition() != nodePosition]
            # remove node
            nodes.remove(node)

    elif left:

        anchor = None
        validPosition = True
        position = pygame.mouse.get_pos()
        

        for node in nodes:
            nodePosition = node.getPosition()
            d = math.sqrt(math.pow(nodePosition[0] - position[0], 2) + math.pow(nodePosition[1] - position[1],2))

            if d <= 2 * NODE_RADIUS:
                validPosition = False
                break
        
        if validPosition:
            nodes.append(Node(position[0], position[1]))


    # display nodes
    
    if right and anchor is not None:
        
        position = pygame.mouse.get_pos()
        
        linkEnd = nearestNode(position, nodes)

        if linkEnd is not None and linkEnd != anchor:

            links.append(Link(anchor, linkEnd, 0))
            print(len(links))
            anchor = None

    elif right and anchor is None:

        position = pygame.mouse.get_pos()

        anchor = nearestNode(position, nodes)
        
    
    
    for link in links:
        pygame.draw.line(screen, LINK_COLOR, link.getHead().getPosition(), link.getTail().getPosition(), 2)
        
    if anchor is not None:
        pygame.draw.line(screen, LINK_COLOR, anchor.getPosition(), pygame.mouse.get_pos(), 2)

    for node in nodes:
        pygame.draw.circle(screen, NODE_COLOR, node.getPosition(), NODE_RADIUS)

    
    if deleteMode:
        screen.blit(deleteText, deleteTextRect)
    

    pygame.display.flip()

    clock.tick(60)

pygame.quit()