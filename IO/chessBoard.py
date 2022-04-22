from typing import List
from Position.index import Position
import pygame
from pygame import Surface,Rect



class ChessBoard:
    def __init__(self,size):
        self.size = size
        self.tileSize = 64
        self.rects:List[Rect] = []

        for i in range(size):
            for j in range(size):
                self.rects.append(Rect(j*self.tileSize,i*self.tileSize,self.tileSize,self.tileSize))

        self.rectColorBlack = [104, 104, 171]
        self.rectColorWhite = [204, 204, 255]
        

    def display(self,screen:Surface):
        flag = 1
        i = 0
        for rect in self.rects:
            if i == 0:
                pygame.draw.rect(screen,self.rectColorBlack,rect) 
                if flag % self.size != 0 or self.size % 2 != 0:
                    i = 1
            elif i == 1:
                pygame.draw.rect(screen,self.rectColorWhite,rect)
                if flag % self.size != 0 or self.size % 2 != 0:
                    i = 0
            flag += 1

    @staticmethod
    def printChessBoard(queens: List[int]):
        boardSize = len(queens)
        for i in range(boardSize):
            for j in range(boardSize):
                pos = Position(j,i)
                hasQueen = False
                for z in range(boardSize):
                    chess = Position.getPosIn2DArray(queens[z],boardSize)
                    if chess == pos:
                        print('Q',end=' ')
                        hasQueen = True

                if hasQueen == False:
                    print('.',end=' ')
            
            print('\n')

    



