from Position.index import Position
import pygame
from pygame import Surface
from typing import List

class Queen:
    def __init__(self,position: Position):
        self.image = pygame.transform.scale(pygame.image.load("IO/images/queen.png"),(64,64))
        self.position = position

    def display(self,screen:Surface):
        screen.blit(self.image, (self.position.x * 64, self.position.y * 64))

    @staticmethod
    def readQueenFromFile(sizeBoard:int,filename = "input.txt"):
        f = open(filename,"r")
        numberOfQueens = int(f.readline())
        queens = [-1 for i in range(sizeBoard)]
        locationList = f.read().split()
        for i in range(len(locationList)):
            location = locationList[i].split(',')
            x = int(location[0].strip('('))
            y = int(location[1].strip(')'))
            pos = Position(x,y)
            queens[x] = Position.getPosIn1DArray(pos,sizeBoard)

        return queens