import pygame
from Node import Node 
import math
from Link import Link
from util import nearestNode
from constants import *
from Message import Message

pygame.init()

screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
pygame.display.set_caption("graph visual")

running = True

nodes = []
links = []
anchor = None
deleteMode = False
insertMode = False
moving = False
linkError = False
errorTime = None

# font
font = pygame.font.Font('freesansbold.ttf', 32)

# app texts

deleteText = font.render("DELETE MODE", True, "red")
deleteTextRect = deleteText.get_rect()
deleteTextRect.center = (400, 740)

insertText = font.render("INSERT MODE", True, "WHITE")
insertTextRect = deleteText.get_rect()
insertTextRect.center = (400, 740)

duplicateLinkError = Message(font, "DUPLICATE LINK", "red", (400, 40))
duplicateLinkError = duplicateLinkError.buildText()

'''
deleteText = Message(font, "DELETE, MODE", "red", (400, 740))
deleteText = deleteText.build()

insertText = Message(font, "INSERT MODE", "white", (400, 740))
insertText = insertText.build()
'''

while running:

    left = False
    right = False
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # checking if D pressed
        elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d:
                    
                    deleteMode = not deleteMode
                    
                    if deleteMode:
                        insertMode = False

                elif event.key == pygame.K_i:
                    
                    insertMode = not insertMode
                    
                    if insertMode:
                        deleteMode = False

        elif event.type == pygame.MOUSEBUTTONDOWN:

            match event.button:
                case 1:
                    left = True
                    moving = True
                case 3:
                    right = True
        elif event.type == pygame.MOUSEBUTTONUP:
            
            match event.button:

                case 1:
                    moving = False
       
    screen.fill(BACKGROUND_COLOR)

    # check for keyboard input

    keyboardInput = pygame.key.get_pressed()
    
    #left, middle, right = pygame.mouse.get_pressed(3)

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

        
    elif left and insertMode:

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
       
      
    elif left and not insertMode and moving:

        # moving node

        position = pygame.mouse.get_pos()
        node = nearestNode(position, nodes)
        if node is not None:
            node.updatePosition(position)

    # display nodes
    
    if right and anchor is not None and insertMode:
        
        position = pygame.mouse.get_pos()
        
        linkEnd = nearestNode(position, nodes)

        if linkEnd is not None and linkEnd != anchor:
            
            link = Link(anchor, linkEnd, 1)
            
            if not link in links: 
                links.append(link)
            else:
                linkError = True
                errorTime = pygame.time.get_ticks()

            linkEnded = True
            anchor = None

    elif right and anchor is None and insertMode:

        position = pygame.mouse.get_pos()

        
        anchor = nearestNode(position, nodes)
            
            
    for link in links:
        pygame.draw.line(screen, LINK_COLOR, link.getHead().getPosition(), link.getTail().getPosition(), 2)
        
    if anchor is not None:
        pygame.draw.line(screen, LINK_COLOR, anchor.getPosition(), pygame.mouse.get_pos(), 2)

    for node in nodes:
        pygame.draw.circle(screen, NODE_COLOR, node.getPosition(), NODE_RADIUS)

    
    if deleteMode:
        anchor = None
        screen.blit(deleteText, deleteTextRect)
    
    elif insertMode:    
        screen.blit(insertText, insertTextRect)

    if linkError and pygame.time.get_ticks() - errorTime < ERROR_DURATION:
        screen.blit(duplicateLinkError[0], duplicateLinkError[1])

    pygame.display.flip()

    clock.tick(60)

pygame.quit()