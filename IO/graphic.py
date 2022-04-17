import pygame
from typing import List
from IO.chessBoard import ChessBoard
from IO.queen import Queen
from Solver.index import QueenSolver
from Position.index import Position
from pygame import Surface

class Graphic:
    def __init__(self,chessBoard: ChessBoard):
        self.solver = None
        self.isRunning = True
        self.chessBoard = chessBoard
        self.queenClasses = []
        self.queenPosition = Queen.readQueenFromFile(chessBoard.size)
        
        self.isStartSolve = False
        self.changeQueen(self.queenPosition)

    def display(self):
        pygame.init()
        screen = pygame.display.set_mode((self.chessBoard.size*64,self.chessBoard.size*64 + 64))
        pygame.display.set_caption("8 queens")
        icon = pygame.image.load("IO/images/icon.png")
        pygame.display.set_icon(icon)

        self.startSolveButton = Button("Start Solve",[255, 255, 255],[22,135,204])
        self.solvedButton = Button("Solved",[255, 255, 255],[216,147,43])

        if self.solver:
            self.solver.setGraphic(self)
            
        while self.isRunning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    self.isRunning = False
                    print("Quit")
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    self.onClick(pos)

            screen.fill((255,255,255))

            self.chessBoard.display(screen)
            for queenClass in self.queenClasses:
                queenClass.display(screen)

            

            if self.solver:
                if self.isStartSolve:
                    self.solver.solve()
                if not self.solver.isSolved:
                    self.startSolveButton.display(screen)
                if self.solver.isSolved:
                    self.solvedButton.display(screen)
                

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

    def onClick(self,pos):
        if pygame.Rect.collidepoint(self.startSolveButton.rect, pos):
            self.isStartSolve = not self.isStartSolve
    

class Button:
    def __init__(self,text,textColor,buttonColor):
        self.font = pygame.font.SysFont("Arial", 14)
        width = 100
        height = 30
        self.rect = pygame.Rect(8*32-width/2,8*64 + 20,width,height)
        self.text = self.font.render(text, 1, textColor)
        self.realText = text
        self.color = buttonColor

    def display(self,screen:Surface):
        pygame.draw.rect(screen,self.color,self.rect)
        width,height = pygame.font.Font.size(self.font, self.realText)
        screen.blit(self.text, (self.rect.centerx-width/2, self.rect.centery-height/2))





