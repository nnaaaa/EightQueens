from Solver.sat.index import SATSolver
from Solver.astar.index import AStarSolver
from Solver.sat.Clauses.level_1 import FirstLevel
from IO.output import Graphic
from IO.chessBoard import ChessBoard


#this is fixed size. If you changed this size, the graphic would display unexpectedly
size = 8


level = FirstLevel(size)
satSolver = SATSolver(level)
astarSolver = AStarSolver(level)

chessBoard = ChessBoard(size)

graphic = Graphic(chessBoard)
graphic.setSolver(astarSolver)
graphic.display()




