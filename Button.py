import pygame
class Button:

    def __init__(self, posx: int, posy: int, width: int, height: int, color: tuple, text: str):
        self.posx = posx
        self.posy = posy
        self.width = width
        self.height = height
        self.color = color
        self.text = text

    def render(self, display):
        pygame.draw.rect(display, self.color, [self.posx, self.posy, self.width, self.height])
        display.blit(self.text, self.posx * 1.5, self.posy)