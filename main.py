import pygame
from Node import Node 
import math
from Link import Link
from util import nearestNode
from constants import *
from Message import Message
from Graph import Graph
from Button import Button
from algos import *

# pygame screen init --------------------------------------------
pygame.init()
global screen
screen = pygame.display.set_mode((800, 800))
clock = pygame.time.Clock()
pygame.display.set_caption("graph visual")
#----------------------------------------------------------------



# graph object --------------------------------------------------
global graph
global algGraph
graph = Graph()
algGraph = Graph()
#----------------------------------------------------------------




# variables -----------------------------------------------------
running = True
global alg
alg = False
anchor = None
deleteMode = False
insertMode = False
moving = False
linkError = False
errorTime = None
# current number of nodes -> last node number
nodeCounter = 1
movingNode = None
modifyWeight = False
newWeight = ""
dijkstraSourceAndDest = []
#----------------------------------------------------------------

# onclick functions ---------------------------------------------

def mstButtonClick(screen):
    global alg
    global algGraph
    
    algGraph = mst(graph)
    alg = True


def bfsButtonOnClick(screen):
    
    global alg
    global algGraph

    sourceMessage = Message(FONT, "select source", "white", (400, 40))
    sourceMessage = sourceMessage.buildText()
    
    source = None
    while source is None:
        screen.blit(sourceMessage[0], sourceMessage[1])
        pygame.display.flip()
      
        for event in pygame.event.get():
            
            if event.type == pygame.MOUSEBUTTONDOWN:
            
                match event.button:
                    case 1:
                        pos = pygame.mouse.get_pos()
                        source = nearestNode(pos, graph.getNodes())
    
    algGraph = bfs(source, graph.generateList())
    alg = True

def dfsButtonOnClick(screen):

    global algGraph
    global alg
    alg = True
    algGraph = dfs(graph)


def dijkstraButtonClick(screen):

    global algGraph
    global alg


    dijkstraSourceAndDest = []
    dijkstraText = Message(FONT, "select source and destination", TEXT_COLOR, (400,40))
    dijkstraText = dijkstraText.buildText()

    alg = True
    while len(dijkstraSourceAndDest) != 2:
        screen.blit(dijkstraText[0], dijkstraText[1])
        pygame.display.flip()

        for event in pygame.event.get():
        
            if event.type == pygame.MOUSEBUTTONDOWN:
            
                match event.button:
                    case 1:
                        pos = pygame.mouse.get_pos()
                        dijkstraSourceAndDest.append(nearestNode(pos, graph.getNodes()))
    
    algGraph = dijkstra(graph, dijkstraSourceAndDest[0], dijkstraSourceAndDest[1])
    

#----------------------------------------------------------------

# algos buttons ------------------------------------------------


buttons = []
buttons.append(Button(210, 750, 100, 40, BUTTON_BACKGROUND_COLOR, "mst", lambda: mstButtonClick(screen)))
buttons.append(Button(330, 750, 100, 40, BUTTON_BACKGROUND_COLOR, "bfs", lambda : bfsButtonOnClick(screen)))
buttons.append(Button(450, 750, 100, 40, BUTTON_BACKGROUND_COLOR, "dfs", lambda : dfsButtonOnClick(screen)))
buttons.append(Button(570, 750, 125, 40, BUTTON_BACKGROUND_COLOR, "dijkstra", lambda : dijkstraButtonClick(screen) ))

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

escAlgVis = Message(SECONDARY_FONT, "press esc to end algo visualization", "white", (400,40))
escAlgVis = escAlgVis.buildText()

modLinkText = Message(SECONDARY_FONT, "type weight and press enter", TEXT_COLOR, (400,40))
modLinkText = modLinkText.buildText()

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
                
                elif event.key == pygame.K_ESCAPE and alg:
                    alg = False
                    algGraph = None
                elif event.unicode.isdigit():
                    newWeight += str(event.key - 48)

                elif event.key == pygame.K_RETURN and modifyWeight:
                    try:
                        weight = int(newWeight)
                        modLink.setWeight(weight)
                        newWeight = ""
                        modifyWeight = False
                        modLink = None
                    except:
                        print("not a number")

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

        elif event.type == pygame.MOUSEBUTTONUP:

            match event.button:

                case 1:
                    moving = False
                    movingNode = None

        elif event.type == pygame.MOUSEMOTION:

            if moving and movingNode is not None:
                movingNode.updatePosition(pygame.mouse.get_pos())

       
    screen.fill(BACKGROUND_COLOR)

    # check for keyboard input

    keyboardInput = pygame.key.get_pressed()
    if left and deleteMode:

        position = pygame.mouse.get_pos()

        node = nearestNode(position, graph.getNodes())
        
        if node is not None:

            nodePosition = node.getPosition()
           
            # remove node and his links
            graph.removeNode(node)

        
    elif left and insertMode and not alg:

        anchor = None
        mousePosition = pygame.mouse.get_pos()
        graph.addNode(Node(mousePosition[0], mousePosition[1], nodeCounter))
        nodeCounter += 1
      
    if left and moving:

        # moving node
        movingNode = nearestNode(pygame.mouse.get_pos(), graph.getNodes())

    
    if right and anchor is not None and insertMode and not alg:
        
        position = pygame.mouse.get_pos()
        
        linkEnd = nearestNode(position, graph.getNodes())

        if linkEnd is not None and linkEnd != anchor:
            
            link = Link(anchor, linkEnd, 1)
            
            if not graph.addLink(link):
                linkError = True
                errorTime = pygame.time.get_ticks()

            linkEnded = True
            anchor = None

    elif right and anchor is None and insertMode and not alg:

        position = pygame.mouse.get_pos()
        anchor = nearestNode(position, graph.getNodes())
    
    # screen elements display -----------------------------------------------------------------------------

    # display links        
    for link in graph.getLinks():
        # check for weight click
        if not insertMode and not deleteMode and left and link.checkClick(pygame.mouse.get_pos()):
            modifyWeight = True
            newWeight = ""
            modLink = link
    
    if modifyWeight:

        screen.blit(modLinkText[0], modLinkText[1])

    # in the process of creating a new link, show a link attached to the anchor and the mouse position
        
    if anchor is not None:
        pygame.draw.line(screen, LINK_COLOR, anchor.getPosition(), pygame.mouse.get_pos(), 2)

    # rendering graph 

    if alg:
        algGraph.renderGraph(screen)
    else:
        graph.renderGraph(screen)

    # display buttons
    if not alg:
        for button in buttons:
            button.render(screen)
    
    if deleteMode and not alg:
        anchor = None
        screen.blit(deleteText, deleteTextRect)
    
    elif insertMode and not alg:    
        screen.blit(insertText, insertTextRect)

    if alg:
        screen.blit(escAlgVis[0], escAlgVis[1])

    if linkError and pygame.time.get_ticks() - errorTime < ERROR_DURATION:
        screen.blit(duplicateLinkError[0], duplicateLinkError[1])
    
    # -----------------------------------------------------------------------------------------------------

    pygame.display.flip()

    clock.tick(60)

pygame.quit()