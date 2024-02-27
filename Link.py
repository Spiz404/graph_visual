import pygame
from constants import *
from Message import Message
import math
class Link:
    
    def __init__(self, node1, node2, weight = 1):
        self.head = node1
        self.tail = node2
        self.weight = weight

    def getHead(self):
        return self.head
    
    def getTail(self):
        return self.tail
    
    def getWeight(self):
        return self.weight
    
    def setWeight(self, weight):
        self.weight = weight
    
    def render(self, screen):
        # plotting line
        pygame.draw.line(screen, LINK_COLOR, self.getHead().getPosition(), self.getTail().getPosition(), 2)
        # plotting weigth
        position = (round(0.5  * self.getHead().getPosition()[0] + 0.5 * self.getTail().getPosition()[0]), round(0.5 * self.getHead().getPosition()[1] + 0.5 * self.getTail().getPosition()[1]))
        self.weightMessage = Message(SECONDARY_FONT, str(self.getWeight()), TEXT_COLOR, position)
        self.weightMessage = self.weightMessage.buildText()
        pygame.draw.rect(screen, BACKGROUND_COLOR, self.weightMessage[1])
        screen.blit(self.weightMessage[0], self.weightMessage[1])
        
    def checkClick(self, mousePosition):
        
        if self.weightMessage[1].collidepoint(mousePosition):
            return True
        
        return False


    def __str__(self):
        return f'head {self.head} tail {self.tail} weight {self.weight}'
    
    def __eq__(link1, link2):
        return (link1.getHead().getPosition() == link2.getHead().getPosition() and link1.getTail().getPosition() == link2.getTail().getPosition()
                or link1.getHead().getPosition() == link2.getTail().getPosition() and link1.getTail().getPosition() == link2.getHead().getPosition())
