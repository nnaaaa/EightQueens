from Solver.sat.Clauses.index import Level
from Solver.index import QueenSolver

class AStarSolver(QueenSolver):
    def __init__(self,level: Level):
        self.__frontier = []

    def __getHeuristicValue(state):
        return 1
