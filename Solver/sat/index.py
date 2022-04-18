from pysat.solvers import Solver,Glucose3,Lingeling
from Solver.sat.Clauses.index import Level
from IO.chessBoard import ChessBoard
from Solver.index import QueenSolver

class SATSolver(QueenSolver):
    def __init__(self,level: Level):
        super().__init__()

        self.__clauses = level
        self.__solver = Lingeling(bootstrap_with=self.__clauses.getClauses(),with_proof=True)
        self.__queens = []

    def solve(self):
        # for clau in self.__clauses.getClauses():
        #     print(clau)
        # with Lingeling(bootstrap_with=self.__clauses.getClauses(), with_proof=False) as l:
        #     r = l.solve()
        #     if not r:
        #         #print(f"proof it's not satisfiable: \n{l.get_proof()}")
        #         return [0] 
        #     else:
        #         m = l.get_model() 

        #         n = []
        #         #print(m)
        #         for i in m:
        #             if (i > 0):
        #                 n+=[i]
        #         printChessBoard(n)
        self.__queens = []
        if self.__solver.solve() == False:
            print("This clauses can't be solved, proof:", self.__solver.get_proof())
        else:
            print("Solved")
            model = self.__solver.get_model()
            for v in model:
                if v > 0:
                    self.__queens.append(v)

            print("\nFull variables")
            print(model)
            print("\nValid queens")
            print(self.__queens)
            print("\nFor more observable")
            ChessBoard.printChessBoard(self.__queens)
            # i = 1
            # for m in self.__solver.enum_models():
            #     self.__queens = []
            #     print(f"Solution {i}")
            #     i+=1
            #     for v in m:
            #         if v > 0:
            #             self.__queens.append(v)
                
            




