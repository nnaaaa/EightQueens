from GUI.chessBoard import writeFile
from Solver.sat.Clauses.index import Level
from Position.index import Position


class FirstLevel(Level):
    def initClauses(self):
        self.rowConstraints()
        self.columnConstraints()
        self.forwardDiagonalConstraints()
        self.backDiagonalConstraints()

        self.cnf.to_file("clauses.txt")

    def rowConstraints(self):
        for rowIndex in range(self.size):
            self.cnf.append(
                [columnIndex for columnIndex in range(rowIndex*self.size + 1, rowIndex*self.size + self.size + 1)])
            for columnIndex in range(self.size):
                for nextColumnIndex in range(columnIndex+1,self.size):
                    column = Position(columnIndex,rowIndex)
                    nextColumn = Position(nextColumnIndex,rowIndex)
                    self.cnf.append([-Position.getPosIn1DArray(column, self.size), -
                                    Position.getPosIn1DArray(nextColumn, self.size)])

            
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
                    

    # def rowContraintAt(self, position: Position):
    #     startRow = Position(position.x, 0)
    #     while startRow.validate(self.size):
    #         if not startRow == position and startRow.y > position.y:
    #             self.cnf.append([-Position.getPosIn1DArray(position, self.size), -
    #                             Position.getPosIn1DArray(startRow, self.size)])
    #         startRow.rowIncrease()

    # def columnContraintAt(self, position: Position):
    #     startColumn = Position(0, position.y)
    #     while startColumn.validate(self.size):
    #         if not startColumn == position and startColumn.x > position.x:
    #             self.cnf.append([-Position.getPosIn1DArray(position, self.size), -
    #                             Position.getPosIn1DArray(startColumn, self.size)])
    #         startColumn.columnIncrease()

    def backDiagonalConstraints(self):
        for i in range(self.size):
            for j in range(self.size):
                startBackDiagonal = Position(j, i)
                nextStart = Position(startBackDiagonal.x + 1,startBackDiagonal.y + 1)
                while nextStart.validate(self.size):
                    literal = [-Position.getPosIn1DArray(nextStart, self.size), -Position.getPosIn1DArray(startBackDiagonal, self.size)]
                    if not self.isExistInClauses(literal):
                        self.cnf.append(literal)
                    nextStart.backDiagonalIncrease()



    def forwardDiagonalConstraints(self):
        for i in range(self.size):
            for j in range(self.size):
                startForwardDiagonal = Position(j, i)
                nextStart = Position(startForwardDiagonal.x - 1,startForwardDiagonal.y + 1)
                while nextStart.validate(self.size):
                    literal = [-Position.getPosIn1DArray(nextStart, self.size), -Position.getPosIn1DArray(startForwardDiagonal, self.size)]
                    if not self.isExistInClauses(literal):
                        self.cnf.append(literal)
                    nextStart.forwardDiagonalIncrease()

