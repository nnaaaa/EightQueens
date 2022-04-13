from CNFClauses.index import EightQueenCNF
from Position.index import Position
from pysat.formula import CNF

class Level_1(EightQueenCNF):
    def __init__(self, size):
        super().__init__(size)
    
    def __getPosIn2DArray(self, position: int) -> Position:
        return position // self.size, position % self.size

    def __getPosIn1DArray(self, position: Position) -> int:
        return position.x * self.size + position.y

    def getClausesAt(self, position: Position) -> CNF().clauses:
        if not position.validate(self.size):
            return []
        
        #cnf clauses for column
        startColumn = Position(0,position.y)
        while startColumn.validate(self.size):
            if not startColumn == position:
                self.resolutions.append([-self.__getPosIn1DArray(position),-self.__getPosIn1DArray(startColumn)])
            startColumn.columnIncrease()

        #cnf clauses for row
        startRow = Position(position.x,0)
        while startRow.validate(self.size):
            if not startRow == position:
                self.resolutions.append([-self.__getPosIn1DArray(position),-self.__getPosIn1DArray(startRow)])
            startRow.rowIncrease()

        #cnf clauses for back diagonal
        startBackDiagonal:Position
        if position.x >= position.y:
            startBackDiagonal = Position(position.x - position.y,0)
        else:
            startBackDiagonal = Position(0,position.y - position.x)
        
        while startBackDiagonal.validate(self.size):
            if not startBackDiagonal == position:
                self.resolutions.append([-self.__getPosIn1DArray(position),-self.__getPosIn1DArray(startBackDiagonal)])
            startBackDiagonal.backDiagonalIncrease()

        #cnf clauses for forward diagonal
        startForwardDiagonal:Position
        if position.x >= self.size - position.y:
            startForwardDiagonal = Position(self.size - 1,position.x - position.y)
        else:
            startForwardDiagonal = Position(self.size - 1 - (self.size - 1 - position.y - position.x),0)
        
        while startForwardDiagonal.validate(self.size):
            if not startForwardDiagonal == position:
                self.resolutions.append([-self.__getPosIn1DArray(position),-self.__getPosIn1DArray(startForwardDiagonal)])
            startForwardDiagonal.forwardDiagonalIncrease()

        return self.resolutions



        

            
