
from pysat.solvers import Solver
from Clauses.index import Level
from GUI.chessBoard import printChessBoard
from Solver.index import QueenSolver

class SATSolver(QueenSolver):
    def __init__(self,level: Level):
        self.__clauses = level
        self.__solver = Solver('m22',bootstrap_with= self.__clauses.getClauses())
        self.__queens = []

    def __del__(self):
        self.__solver.delete()

    def solve(self):
        if self.__queens.__len__() > 0:
            return
        if self.__solver.solve() == False:
            print("Failed, proof:", self.get_proof())
        else:
            print("Success")
            i = 1
            for m in self.__solver.enum_models():
                self.__queens = []
                print(f"Solution {i}")
                i+=1
                for v in m:
                    if v > 0:
                        self.__queens.append(v)
                
                printChessBoard(self.__queens,self.__clauses)




