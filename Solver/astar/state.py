from typing import List
from Position.index import Position
from copy import deepcopy
from uuid import uuid4

class State:
    def __init__(self,board: List[int],father = None):
        self.board = board
        self.id = uuid4()
        
        self.father = father
        self.hvalue = 99999

        if father:
            self.gvalue = father.gvalue + 1
        else:
            self.gvalue = 0


    def action(self,currentQueen:int,value:int):
        board = deepcopy(self.board)
        board[currentQueen] = value
        successor = State(board,self)
        return successor

    def generateSuccessors(self,initPos,currentPos):
        successors:List[State] = []
        boardSize = self.board.__len__()

        #move queen when entire queens placed
        if not -1 in self.board:
            print("Do nothing")
            # for j in range(boardSize):
            #     if j+1 in self.board:
            #         continue
            #     successor = self.action(currentPos,j+1)
            #     successors.append(successor)

            # currentPos += 1
            # if currentPos == boardSize:
            #     currentPos = initPos

        #any queens haven't placed in the board yet
        else:
            for i in range(boardSize):
                if self.board[i] == -1:
                    for j in range(boardSize):
                        pos = Position(j,i)
                        successor = self.action(i,Position.getPosIn1DArray(pos,boardSize))
                        successors.append(successor)

        return successors

    def __isSameDiagonal(self,firstQueen:Position,secondQueen:Position):
        boardSize = self.board.__len__()
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
