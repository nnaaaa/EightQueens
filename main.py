from Solver.sat.index import SATSolver
from Solver.astar.index import AStarSolver
from Solver.sat.Clauses.level_1 import FirstLevel
from Solver.sat.Clauses.level_2 import SecondLevel
from IO.graphic import Graphic
from IO.chessBoard import ChessBoard
from IO.queen import Queen
from Solver.sat.Clauses.index import Level
from Position.index import Position
import time


# This is fixed size. If you changed this size, the graphic would display unexpectedly
size = 8
# Entire classes which created by me
# level = FirstLevel(size)
# satSolver = SATSolver(level)
# astarSolver = AStarSolver()

# chessBoard = ChessBoard(size)

# graphic = Graphic(chessBoard)
# graphic.setSolver(astarSolver)
# graphic.display()


while True:
    print("We have many solver for 8 queens probem")
    print("'b' Write CNF at position b[3][3] to clauses.txt")
    print("'c' '1' Write CNF clauses without column restrictions to clauses.txt")
    print("'c' '2' Write CNF clauses with full restrictions (row,column,diagonal) to clauses.txt")
    print("'d' Print a set of satisfied values from CNF clauses writed by 'c'")
    print("'e' Solve 8 queen by A star and print out. Input file name 'input.txt'")
    print("'f' Visualize A star and SAT by GUI. You can chose input or use our default 'input.txt'")
    print("'q' Quit")
    print("Which question you want?",end=' ')
    chose = input()
    if chose == "b":
        level = Level(size)
        position = Position(3, 3)
        level.restrictionAt(position)
        level.printClausesSpecially()

    if chose == "c":
        print("Type '1' or '2' to chose level: ",end=' ')
        levelChose = input()
        level = None
        if levelChose == "1":
            level = FirstLevel(size)
        else:
            level = SecondLevel(size)
            
        level.initClauses()
        level.printClauses()

    if chose == "d":
        level = SecondLevel(size)
        satSolver = SATSolver(level)
        satSolver.solve()

    if chose == "e":
        initQueens = Queen.readQueenFromFile(size)
        astarSolver = AStarSolver(initQueens)
        print("Solving ...")
        start = time.time()
        while not astarSolver.isSolved:
            astarSolver.solve()
        end = time.time()
        print("Solving time:",end - start)
        

    if chose == "f":
        chessBoard = ChessBoard(size)
        graphic = Graphic(chessBoard)
        graphic.display()

    if chose == "q":
        break

    print('\n')


