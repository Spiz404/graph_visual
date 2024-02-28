import pygame
class Message:
    
    def __init__(self, font : pygame.Font, text : str, color : str, pos : tuple):
        self.font = font
        self.pos = pos
        self.text = text
        self.color = color
    
    def buildText(self) -> list:
        
        message = self.font.render(self.text, True, self.color)
        box = message.get_rect()
        box.center = self.pos
        return [message, box]
    
    