import pygame
from Message import Message
from constants import *
class Button:

    def __init__(self, posx: int, posy: int, width: int, height: int, color: tuple, text: str, onClick=None, radius = 5):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.onClick = onClick
        self.radius = radius
        self.rect = pygame.Rect(posx, posy, width, height)
        self.message = Message(FONT, text, TEXT_COLOR, (posx + self.width / 2, posy + self.height / 2)).buildText()

    # rendering button 
    def render(self, display):
        pygame.draw.rect(display, self.color, self.rect, border_radius=5)
        display.blit(self.message[0], self.message[1])

    # check for mouse click on the button, return True if clicked, False otherwise
    # args: position -> mouse position when click event happen
        
    def checkClick(self, position: tuple):
        if self.rect.collidepoint(position[0], position[1]):
            self.onClick()
            return True
        else:
            return False