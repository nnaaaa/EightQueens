from GUI.chessBoard import writeFile
from Solver.sat.Clauses.index import Level
from Position.index import Position


class FirstLevel(Level):
    def initClauses(self):
        # exactly one queen at one row
        # for i in range(self.size):
        #     # literal = []
        #     # for j in range(self.size):
        #     #     pos = Position(i, j)
        #     #     literal.append(Position.getPosIn1DArray(pos, self.size))

        #     self.cnf.append(
        #         [i for i in range(i*self.size + 1, i*self.size + self.size + 1)])

        # # exactly one queen at one column
        # for i in range(self.size):
        #     literal = []
        #     for j in range(self.size):
        #         pos = Position(j, i)
        #         literal.append(Position.getPosIn1DArray(pos, self.size))

        #     self.cnf.append(literal)

        
        # self.rowConstraints()
        # self.columnConstraints()
        # #self.diagonalConstraints()
        # for i in range(self.size):
        #     for j in range(self.size):
        #         pos = Position(i, j)
        #         print(f"at ({pos.x},{pos.y})")
        #         print("forward")
        #         self.forwardDiagonalConstraintAt(pos)
        #         print("backward")
        #         self.backDiagonalConstraintAt(pos)

        
        restrictions = []
        for i in range(self.size):
            current=[i for i in range(i*self.size+1,i*self.size+self.size+1)]
            restrictions.append(current)
        for i in range(self.size*self.size):
            for j in range(self.size*self.size):
                if (i!=j)and((j % self.size == i %self.size) or (j // self.size == i // self.size) or (abs(i//self.size-j//self.size)==abs(i%self.size-j%self.size))):
                    restrictions.append([-1*(i+1),(j+1)*-1])

        self.cnf.extend(restrictions)
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

    def backDiagonalConstraintAt(self, position: Position):
        a = []
        startBackDiagonal: Position
        if position.x >= position.y:
            startBackDiagonal = Position(position.x - position.y, 0)
        else:
            startBackDiagonal = Position(0, position.y - position.x)

        while startBackDiagonal.validate(self.size):
            if not startBackDiagonal == position:
                literal = [-Position.getPosIn1DArray(position, self.size), -Position.getPosIn1DArray(startBackDiagonal, self.size)]
                if not self.isExistInClauses(literal):
                    a.append([Position.getPosIn1DArray(position, self.size), Position.getPosIn1DArray(startBackDiagonal, self.size)])
                    self.cnf.append(literal)
            startBackDiagonal.backDiagonalIncrease()

        for c in a:
            for i in c:
                pos = Position.getPosIn2DArray(i,self.size)
                print(f"({pos.x},{pos.y})",end=' ')
            print("\n")
        print("\n")

    def forwardDiagonalConstraintAt(self, position: Position):
        a = []
        startForwardDiagonal: Position
        if position.x >= self.size - position.y:
            startForwardDiagonal = Position(
                self.size - 1, position.x - position.y)
        else:
            startForwardDiagonal = Position(
                self.size - 1 - (self.size - 1 - position.y - position.x), 0)

        while startForwardDiagonal.validate(self.size):
            if not startForwardDiagonal == position:
                literal = [-Position.getPosIn1DArray(position, self.size), -Position.getPosIn1DArray(startForwardDiagonal, self.size)]
                if not self.isExistInClauses(literal):
                    a.append([Position.getPosIn1DArray(position, self.size), Position.getPosIn1DArray(startForwardDiagonal, self.size)])
                    self.cnf.append(literal)
            startForwardDiagonal.forwardDiagonalIncrease()

        for c in a:
            for i in c:
                pos = Position.getPosIn2DArray(i,self.size)
                print(f"({pos.x},{pos.y})",end=' ')
            print("\n")
        print("\n")
