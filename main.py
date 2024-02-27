import pygame
from Node import Node 
import math
from Link import Link
from util import nearestNode
from constants import *
from Message import Message
from Graph import Graph
from Button import Button

pygame.init()

screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
pygame.display.set_caption("graph visual")

running = True

nodes = []
links = []
buttons = []
buttons.append(Button(330, 750, 100, 40, BUTTON_BACKGROUND_COLOR, "bfs", lambda : print("click")))
anchor = None
deleteMode = False
insertMode = False
moving = False
linkError = False
errorTime = None
# current number of nodes -> last node number
nodeCounter = 1
movingNode = None
# font

# graph adjacence list ------------------------------------------
al = Graph()
#----------------------------------------------------------------

# app texts ----------------------------------------------------
deleteText = SECONDARY_FONT.render("DELETE MODE", True, "red")
deleteTextRect = deleteText.get_rect()
deleteTextRect.center = SECONDARY_CENTER

insertText = SECONDARY_FONT.render("INSERT MODE", True, "WHITE")
insertTextRect = deleteText.get_rect()
insertTextRect.center = SECONDARY_CENTER


duplicateLinkError = Message(FONT, "DUPLICATE LINK", "red", (400, 40))
duplicateLinkError = duplicateLinkError.buildText()
#----------------------------------------------------------------

# game loop 
while running:
    left = False
    right = False

    # checking for events
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        
        elif event.type == pygame.KEYDOWN:
                
                # checking if D pressed
                if event.key == pygame.K_d:
                    # toggle delete mode
                    deleteMode = not deleteMode
                    
                    if deleteMode:
                        insertMode = False

                # checking if I pressed
                elif event.key == pygame.K_i:
                    # toggle insert mode    
                    insertMode = not insertMode
                    
                    if insertMode:
                        deleteMode = False

        # checking for mouse click event
        elif event.type == pygame.MOUSEBUTTONDOWN:
            
            match event.button:
                case 1:
                    buttonClick = False
                    # check if a button is clicked
                    for button in buttons:
                        if button.checkClick(pygame.mouse.get_pos()):
                            buttonClick = True
                    
                    if not buttonClick:
                        left = True
                        moving = True

                case 3:
                    right = True

        # checking for mouse button release
        elif event.type == pygame.MOUSEBUTTONUP:

            match event.button:

                case 1:
                    moving = False

        # checking for mouse motion    
        elif event.type == pygame.MOUSEMOTION:

            if moving and movingNode is not None:
                movingNode.updatePosition(pygame.mouse.get_pos())
       
    screen.fill(BACKGROUND_COLOR)

    # check for keyboard input

    keyboardInput = pygame.key.get_pressed()
    

    # left mouse button 

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
            nodes.append(Node(position[0], position[1], nodeCounter))
            al.newNode()
            nodeCounter = nodeCounter + 1
       
      
    elif left:

        # moving node
        print("moving node")
        position = pygame.mouse.get_pos()
        movingNode = nearestNode(position, nodes)

    
    if right and anchor is not None and insertMode:
        
        position = pygame.mouse.get_pos()
        
        linkEnd = nearestNode(position, nodes)

        if linkEnd is not None and linkEnd != anchor:
            
            link = Link(anchor, linkEnd, 1)
            
            if not link in links: 
                links.append(link)
                al.linkNode(anchor.getLabel()  - 1, linkEnd.getLabel() - 1)
                #print(al.l)
            else:
                linkError = True
                errorTime = pygame.time.get_ticks()

            linkEnded = True
            anchor = None

    elif right and anchor is None and insertMode:

        position = pygame.mouse.get_pos()

        
        anchor = nearestNode(position, nodes)
    
    # screen elements display -----------------------------------------------------------------------------
        
    # display links        
    for link in links:
        #pygame.draw.line(screen, LINK_COLOR, link.getHead().getPosition(), link.getTail().getPosition(), 2)
        link.render(screen)
        
    # in the process of creating a new link, show a link attached to the anchor and the mouse position
    if anchor is not None:
        pygame.draw.line(screen, LINK_COLOR, anchor.getPosition(), pygame.mouse.get_pos(), 2)

    # display nodes
    for node in nodes:
        pygame.draw.circle(screen, NODE_COLOR, node.getPosition(), NODE_RADIUS)

        #label = Message(FONT, str(node.getLabel()), (0,0,0), node.getPosition())
        #label = label.buildText()
        #screen.blit(label[0], label[1])

    # display buttons
    for button in buttons:
        button.render(screen)
    
    if deleteMode:
        anchor = None
        screen.blit(deleteText, deleteTextRect)
    
    elif insertMode:    
        screen.blit(insertText, insertTextRect)

    if linkError and pygame.time.get_ticks() - errorTime < ERROR_DURATION:
        screen.blit(duplicateLinkError[0], duplicateLinkError[1])
    
    # -----------------------------------------------------------------------------------------------------

    pygame.display.flip()

    clock.tick(60)

pygame.quit()