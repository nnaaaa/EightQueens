from IO.chessBoard import printChessBoard
from IO.queen import Queen

from Solver.astar.state import State
from Solver.astar.frontier import Frontier
from Solver.sat.Clauses.index import Level
from Solver.index import QueenSolver

class AStarSolver(QueenSolver):
    def __init__(self,level: Level):
        super().__init__()
        self.graphic = None
        self.__frontier = Frontier()
        self.__expendedStates = Frontier()
        self.__root = State(Queen.readQueenFromFile(level.size))
        self.initQueenPos = 1
        self.currentQueenPos = self.initQueenPos 
        self.__frontier.push(self.__root)
        self.isSolved = False
    
    def solve(self):
        if not self.__frontier.isEmpty() and self.isSolved == False:
            currentNode = self.__frontier.putStateWithLowestFValue()
            self.__expendedStates.push(currentNode)

            if self.graphic:
                self.graphic.changeQueen(currentNode.board)

            if currentNode.getHeuristicValue() == 0 and not -1 in currentNode.board:
                self.isSolved = True
                printChessBoard(currentNode.board)
                return

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

        #print("Solution hasn't found")
        




