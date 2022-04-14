from Solver.sat import SATSolver
from Solver.sat.Clauses.level_1 import FirstLevel

level = FirstLevel(10)
solver = SATSolver(level)

solver.solve()
