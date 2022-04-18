from pygame import Surface
import pygame

class Button:
    def __init__(self,text,textColor,buttonColor,x,y,width,height):
        self.font = pygame.font.SysFont("Arial", 14)
        self.rect = pygame.Rect(x-width/2,y,width,height)
        self.text = self.font.render(text, 1, textColor)
        self.realText = text
        self.color = buttonColor

    def display(self,screen:Surface):
        pygame.draw.rect(screen,self.color,self.rect)
        width,height = pygame.font.Font.size(self.font, self.realText)
        screen.blit(self.text, (self.rect.centerx-width/2, self.rect.centery-height/2))