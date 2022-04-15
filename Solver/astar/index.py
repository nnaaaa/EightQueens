from GUI.chessBoard import printChessBoard
from Solver.astar.state import State
from Solver.astar.frontier import Frontier
from Solver.sat.Clauses.index import Level
from Solver.index import QueenSolver

class AStarSolver(QueenSolver):
    def __init__(self,level: Level):
        self.__frontier = Frontier()
        self.__root = State([1,-1,-1,-1,-1,-1,-1,-1])
    
    def solve(self):
        self.__frontier = Frontier()
        self.__frontier.push(self.__root)

        while not self.__frontier.isEmpty():
            currentNode = self.__frontier.putStateWithLowestFValue()
            printChessBoard(currentNode.board)
            print("\n")
            if currentNode.hvalue == 0 and not -1 in currentNode.board:
                printChessBoard(currentNode.board)

            for successor in currentNode.generateSuccessors():
                nodeInFrontier = self.__frontier.findById(successor.id)
                if nodeInFrontier:
                    if successor.gvalue < nodeInFrontier.gvalue:
                        self.__frontier.remove(nodeInFrontier)
                        self.__frontier.push(successor)
                else:
                    self.__frontier.push(successor)



