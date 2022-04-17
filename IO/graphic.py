import pygame
from typing import List
from IO.chessBoard import ChessBoard
from IO.queen import Queen
from Solver.index import QueenSolver
from Position.index import Position
from Solver.astar.index import AStarSolver
from pygame import Surface
import tkinter
import tkinter.filedialog


class Graphic:
    def __init__(self,chessBoard: ChessBoard):
        self.solver = None
        self.isRunning = True
        self.chessBoard = chessBoard
        self.queenClasses = []
        self.queenPosition = []
        
        self.isStartSolve = False
        self.changeQueen(self.queenPosition)

    def display(self):
        pygame.init()
        screen = pygame.display.set_mode((self.chessBoard.size*64,self.chessBoard.size*67 + 64))
        pygame.display.set_caption("8 queens")
        icon = pygame.image.load("IO/images/icon.png")
        pygame.display.set_icon(icon)

        self.startSolveButton = Button("Start Solve",[255, 255, 255],[22,135,204],8*32,8*64 + 10,100,30)
        self.solvedButton = Button("Solved",[255, 255, 255],[216,147,43],8*32,8*64 + 10,100,30)
        self.choseFileButton = Button("Chose your input",[255, 255, 255],[22,135,204],8*32,8*64 + 50,100,30)

        
            
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

            self.choseFileButton.display(screen)

            if self.solver:
                self.solver.setGraphic(self)
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

    def choseFile(self):
        top = tkinter.Tk()
        top.withdraw()  # hide window
        file_name = tkinter.filedialog.askopenfilename(parent=top)
        top.destroy()
        return file_name

    def onClick(self,pos):
        if pygame.Rect.collidepoint(self.startSolveButton.rect, pos):
            self.isStartSolve = not self.isStartSolve

        if pygame.Rect.collidepoint(self.choseFileButton.rect, pos):
            filename = self.choseFile()
            if filename:
                queens = Queen.readQueenFromFile(self.chessBoard.size,filename)
                self.changeQueen(queens)
                astarSolver = AStarSolver(queens)
                self.setSolver(astarSolver)
    

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





