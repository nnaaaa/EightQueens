from pygame import Surface
import pygame

class Button:
    def __init__(self,text,x,y):
        self.font = pygame.font.SysFont("Arial", 14)
        self.rect = pygame.Rect(x,y,100,30)
        self.text = self.font.render(text, 1, [255, 255, 255])
        self.realText = text
        self.color = [104, 104, 171]

    def display(self,screen:Surface):
        pygame.draw.rect(screen,self.color,self.rect)
        width,height = pygame.font.Font.size(self.font, self.realText)
        screen.blit(self.text, (self.rect.centerx-width/2, self.rect.centery-height/2))

class CenterButton(Button):
    def __init__(self, text, x, y):
        super().__init__(text, x, y)
        self.rect = pygame.Rect(x/2-100/2,y,100,30)

class RightButton(Button):
    def __init__(self, text, x, y):
        super().__init__(text, x, y)
        self.rect = pygame.Rect(x-100,y,100,30)
