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

    def action(self,currentQueen:int,value:int):
        successor = deepcopy(self)
        successor.board[currentQueen] = value
        successor.father = self
        successor.id = uuid4()
        successor.hvalue = successor.getHeuristicValue()
        successor.gvalue = successor.gvalue + 1
        return successor

    def generateSuccessors(self,initPos,currentPos):
        successors:List[State] = []
        boardSize = len(self.board)

        #move queen when entire queens placed
        if not -1 in self.board:
            for j in range(boardSize*boardSize):
                if j+1 in self.board:
                    continue
                successor = self.action(currentPos,j+1)
                successors.append(successor)

            currentPos += 1
            if currentPos == boardSize:
                currentPos = initPos

        else:
            #any queens haven't placed in the board yet
            for i in range(boardSize):
                if self.board[i] == -1:
                    for j in range(boardSize*boardSize):
                        if j+1 in self.board:
                            continue
                        successor = self.action(i,j+1)
                        successors.append(successor)

        return successors

    def __isSameDiagonal(self,firstQueen:Position,secondQueen:Position):
        boardSize = len(self.board)
        forwardPoint = deepcopy(firstQueen)
        while forwardPoint.validate(boardSize):
            if forwardPoint == secondQueen:
                return True
            forwardPoint.forwardDiagonalIncrease()
        forwardPoint = deepcopy(firstQueen)
        while forwardPoint.validate(boardSize):
            if forwardPoint == secondQueen:
                return True
            forwardPoint.forwardDiagonalDecrease()

        backwardPoint = deepcopy(firstQueen)
        while backwardPoint.validate(boardSize):
            if backwardPoint == secondQueen:
                return True
            backwardPoint.backDiagonalIncrease()
        backwardPoint = deepcopy(firstQueen)
        while backwardPoint.validate(boardSize):
            if backwardPoint == secondQueen:
                return True
            backwardPoint.backDiagonalDecrease()

        return False
        

    def getHeuristicValue(self):
        attackPairs = 0
        boardSize = len(self.board)
        for i in range(boardSize):
            for j in range(i+1,boardSize):
                if self.board[i] == -1 or self.board[j] == -1:
                    continue
                firstQueen = Position.getPosIn2DArray(self.board[i],boardSize)
                secondQueen = Position.getPosIn2DArray(self.board[j],boardSize)
                isSameRow = firstQueen.y == secondQueen.y
                isSameColumn = firstQueen.x == secondQueen.x
                isSameDiagonal = self.__isSameDiagonal(firstQueen,secondQueen)
                if isSameRow or isSameColumn or isSameDiagonal:
                    attackPairs += 1

        return attackPairs
