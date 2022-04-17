from Solver.sat.Clauses.level_1 import FirstLevel
from Position.index import Position

class SecondLevel(FirstLevel):
    def initClauses(self):
        super().initClauses()
        self.columnConstraints()

        

    def columnConstraints(self):
        for columnIndex in range(self.size):
            self.cnf.append(
                [columnIndex+1+rowIndex*self.size for rowIndex in range(self.size)])
            for rowIndex in range(self.size):
                for nextRowIndex in range(rowIndex+1,self.size):
                    row = Position(columnIndex,rowIndex)
                    nextRow = Position(columnIndex,nextRowIndex)
                    self.cnf.append([-Position.getPosIn1DArray(row, self.size), -
                                    Position.getPosIn1DArray(nextRow, self.size)])