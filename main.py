from Solver.sat.index import SATSolver
from Solver.astar.index import AStarSolver
from Solver.sat.Clauses.level_1 import FirstLevel

level = FirstLevel(4)
solver = AStarSolver(level)

solver.solve()
