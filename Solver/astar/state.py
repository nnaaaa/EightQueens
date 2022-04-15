
from typing import List
from Position.index import Position
from copy import deepcopy
from uuid import uuid4

class State:
    def __init__(self,board: List[int],father = None):
        self.board = board
        self.id = uuid4()
        
        self.hvalue = self.getHeuristicValue()
        self.father = father

        if father:
            self.gvalue = father.gvalue
        else:
            self.gvalue = 0

    def generateSuccessors(self):
        successors:List[State] = []
        boardSize = len(self.board)
        for i in range(boardSize):
            if self.board[i] == -1:
                for j in range(boardSize*boardSize):
                    successor = deepcopy(self)
                    successor.board[i] = j + 1
                    successor.father = self
                    successor.hvalue = successor.getHeuristicValue()
                    successor.gvalue = successor.gvalue + 1
                    successors.append(successor)

        return successors

    def getHeuristicValue(self):
        attackPairs = 0
        boardSize = len(self.board)
        for i in range(boardSize):
            for j in range(i+1,boardSize):
                firstQueen = Position.getPosIn2DArray(self.board[i],boardSize)
                secondQueen = Position.getPosIn2DArray(self.board[j],boardSize)
                isSameRow = firstQueen.y == secondQueen.y
                isSameColumn = firstQueen.x == secondQueen.x
                isSameDiagonal = firstQueen.y - firstQueen.x == secondQueen.y - secondQueen.x
                if isSameRow or isSameColumn or isSameDiagonal:
                    attackPairs += 1

        return 0
