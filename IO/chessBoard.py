from typing import List
from Position.index import Position
import pygame


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
                print('_',end=' ')
        
        print('\n')

def writeFile(clauses):
    f = open("clauses.txt","w")
    for clause in clauses:
        f.write(str(clause) + "\n")

    f.close()





class ChessBoard:
    def __init__(self,size):
        self.size = size
        self.image = pygame.transform.scale(pygame.image.load("IO/images/board.png"),(self.size*64,self.size*64))
        

    def display(self,screen):
        screen.blit(self.image, (0, 0))

    



