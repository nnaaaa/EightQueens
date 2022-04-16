from GUI.chessBoard import printChessBoard
from Solver.astar.state import State
from Solver.astar.frontier import Frontier
from Solver.sat.Clauses.index import Level
from Solver.index import QueenSolver

class AStarSolver(QueenSolver):
    def __init__(self,level: Level):
        self.__frontier = Frontier()
        self.__expendedStates = Frontier()
        self.__root = State([9,2,-1,-1])
        self.initQueenPos = 1
        self.currentQueenPos = self.initQueenPos 
    
    def solve(self):
        self.__frontier = Frontier()
        self.__expendedStates = Frontier()
        self.__frontier.push(self.__root)

        while not self.__frontier.isEmpty():
            currentNode = self.__frontier.putStateWithLowestFValue()
            self.__expendedStates.push(currentNode)
            # print(currentNode.getHeuristicValue(),end=' ')
            # print(currentNode.gvalue)
            # printChessBoard(currentNode.board)
            # print("\n")
            if currentNode.getHeuristicValue() == 0 and not -1 in currentNode.board:
                printChessBoard(currentNode.board)
                return currentNode

            for successor in currentNode.generateSuccessors(self.initQueenPos,self.currentQueenPos):
                if self.__expendedStates.isExist(successor):
                    continue

                if self.__frontier.isExist(successor):
                    nodeInFrontier = self.__frontier.findById(successor.id)
                    if successor.gvalue < nodeInFrontier.gvalue:
                        self.__frontier.remove(nodeInFrontier)
                        self.__frontier.push(successor)
                else:
                    self.__frontier.push(successor)



