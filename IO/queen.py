from Position.index import Position
import pygame

class Queen:
    def __init__(self,position: Position):
        self.image = pygame.transform.scale(pygame.image.load("IO/images/queen.png"),(64,64))
        self.position = position

    def display(self,screen):
        screen.blit(self.image, (self.position.x * 64, self.position.y * 64))

    @staticmethod
    def readQueenFromFile(sizeBoard:int):
        f = open("input.txt","r")
        numberOfQueens = int(f.readline())
        queens = [-1 for i in range(sizeBoard - numberOfQueens)]
        locationList = f.read().split()
        for i in range(len(locationList)):
            location = locationList[i].split(',')
            x = int(location[0].strip('('))
            y = int(location[1].strip(')'))
            pos = Position(x,y)
            queens.insert(0,Position.getPosIn1DArray(pos,sizeBoard))

        return queens