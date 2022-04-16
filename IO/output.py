import pygame
from typing import List
from IO.chessBoard import ChessBoard
from IO.queen import Queen
from Solver.index import QueenSolver
from Position.index import Position

class Graphic:
    def __init__(self,chessBoard: ChessBoard):
        self.solver = None
        self.isRunning = True
        self.chessBoard = chessBoard
        self.queenClasses = []
        self.queenPosition = Queen.readQueenFromFile(chessBoard.size)
        self.changeQueen(self.queenPosition)

    def display(self):
        pygame.init()
        screen = pygame.display.set_mode((self.chessBoard.size*64,self.chessBoard.size*64 + 128))
        pygame.display.set_caption("8 queens")
        icon = pygame.image.load("IO/images/icon.png")
        pygame.display.set_icon(icon)

        if self.solver:
            self.solver.setGraphic(self)
            
        while self.isRunning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isRunning = False 
                    print("Quit game")

            screen.fill((255,255,255))

            self.chessBoard.display(screen)
            for queenClass in self.queenClasses:
                queenClass.display(screen)

            if self.solver:
                self.solver.solve()
                

            pygame.display.update()
        pygame.display.flip()

    def setSolver(self,solver: QueenSolver):
        self.solver = solver

    def changeQueen(self,queens: List[int]):
        self.queenPosition = queens
        self.queenClasses = []
        for pos in self.queenPosition:
            if pos != -1:
                queen = Queen(Position.getPosIn2DArray(pos, self.chessBoard.size))
                self.queenClasses.append(queen)



