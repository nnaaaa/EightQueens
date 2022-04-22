import pygame
from typing import List
from IO.chessBoard import ChessBoard
from IO.queen import Queen
from IO.button import Button,CenterButton,RightButton
from Solver.index import QueenSolver
from Position.index import Position
from pygame import Surface
import tkinter
import tkinter.filedialog
from Solver.sat.index import SATSolver
from Solver.astar.index import AStarSolver
from Solver.sat.Clauses.level_2 import SecondLevel

class Graphic:
    def __init__(self,chessBoard: ChessBoard):
        self.solver = None
        self.isRunning = True
        self.chessBoard = chessBoard
        self.queenClasses = []
        self.queenPosition = []
        
        self.isChosedFile = False
        self.isStartSolve = False
        self.isChosedSolver = False

    def display(self):
        pygame.init()
        screen = pygame.display.set_mode((self.chessBoard.size*self.chessBoard.tileSize,self.chessBoard.size*self.chessBoard.tileSize + 130))
        pygame.display.set_caption("8 queens")
        icon = pygame.image.load("IO/images/icon.png")
        pygame.display.set_icon(icon)

        self.astarSolveButton = RightButton("Chose A*",self.chessBoard.size*self.chessBoard.tileSize - 10,self.chessBoard.size*self.chessBoard.tileSize + 10)
        self.satSolveButton = RightButton("Chose SAT",self.chessBoard.size*self.chessBoard.tileSize - 10,self.chessBoard.size*self.chessBoard.tileSize + 50)
        self.solvedButton = CenterButton("Solved",self.chessBoard.size*self.chessBoard.tileSize,self.chessBoard.size*self.chessBoard.tileSize + 10)
        self.cannotSolvedButton = CenterButton("Can't be solved",self.chessBoard.size*self.chessBoard.tileSize,self.chessBoard.size*self.chessBoard.tileSize + 50)
        self.startSolveButton = CenterButton("Start solve",self.chessBoard.size*self.chessBoard.tileSize,self.chessBoard.size*self.chessBoard.tileSize + 90)
        self.choseFileButton = Button("Chose your input",10,self.chessBoard.size*self.chessBoard.tileSize + 10)

        
        while self.isRunning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT: 
                    self.isRunning = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    self.onClick(pos)
            
            screen.fill((255,255,255))

            self.chessBoard.display(screen)
            for queenClass in self.queenClasses:
                queenClass.display(screen)


            if not self.isChosedFile:
                self.choseFileButton.display(screen)
            else:

                if self.solver:
                    if not self.solver.graphic:
                        self.solver.setGraphic(self)

                    if self.isStartSolve:
                        self.solver.solve()

                    if self.isChosedSolver:
                        self.startSolveButton.display(screen)

                    if self.solver.cannotSolved:
                        self.cannotSolvedButton.display(screen)
                    elif self.solver.isSolved:
                        self.solvedButton.display(screen)

                        
                                
                else:
                    if not self.isStartSolve:
                        self.astarSolveButton.display(screen)
                        self.satSolveButton.display(screen)
                    
                    

                

            pygame.display.update()
        #pygame.display.flip()
        pygame.quit()

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
        if pygame.Rect.collidepoint(self.astarSolveButton.rect, pos):
            self.solver = AStarSolver(self.queenPosition)
            self.isChosedSolver = True

        if pygame.Rect.collidepoint(self.satSolveButton.rect, pos):
            level = SecondLevel(self.chessBoard.size)
            level.printClauses()
            self.solver = SATSolver(level,self.queenPosition)
            self.isChosedSolver = True

        if pygame.Rect.collidepoint(self.startSolveButton.rect, pos):
            self.isStartSolve = not self.isStartSolve

        if pygame.Rect.collidepoint(self.solvedButton.rect, pos):
            self.setSolver(None)
            self.isChosedFile = False
            self.isStartSolve = False
            self.isChosedSolver = False

        if pygame.Rect.collidepoint(self.choseFileButton.rect, pos):
            self.isChosedFile = True
            filename = self.choseFile()
            if filename:
                queens = Queen.readQueenFromFile(self.chessBoard.size,filename)
                self.changeQueen(queens)
                # astarSolver = AStarSolver(queens)
                # self.setSolver(astarSolver)
    







