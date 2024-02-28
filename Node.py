import pygame
from constants import *
class Node:
    def __init__(self, x, y, label):
        self.posx = x
        self.posy = y
        self.label = label
        self.shape = pygame.Rect(x, y, NODE_RADIUS, NODE_RADIUS)

    def getPosition(self):
        return ((self.posx, self.posy))
    
    def getLabel(self):
        return self.label
    
    def updatePosition(self, newPosition):
        self.posx = newPosition[0]
        self.posy = newPosition[1]

    def render(self, screen):
        pygame.draw.circle(screen, NODE_COLOR, self.getPosition(), NODE_RADIUS)
        #pygame.draw.rect(screen, NODE_COLOR, self.shape, border_radius=round(NODE_RADIUS/2))