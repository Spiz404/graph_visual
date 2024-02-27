import pygame
from Message import Message
from constants import *
class Button:

    def __init__(self, posx: int, posy: int, width: int, height: int, color: tuple, text: str, onClick=None):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.color = color
        self.text = text
        self.onClick = onClick
        self.rect = pygame.Rect(posx, posy, width, height)
        self.message = Message(FONT, text, TEXT_COLOR, (posx + self.width / 2, posy + self.height / 2)).buildText()

    def render(self, display):
        pygame.draw.rect(display, self.color, self.rect, border_radius=5)
        display.blit(self.message[0], self.message[1])

    