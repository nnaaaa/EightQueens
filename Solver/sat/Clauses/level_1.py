from Clauses.index import Level
from Position.index import Position

class FirstLevel(Level):
    def initClauses(self):
        self.result = []
        for i in range(self.size):
            for j in range(self.size):
                pos = Position(i,j)
                self.columnContraintAt(pos)
                self.rowContraintAt(pos)
                self.forwardDiagonalConstraintAt(pos)
                self.backDiagonalConstraintAt(pos)

        #exactly one queen at one row
        for i in range(self.size):
            literal = []
            for j in range(self.size):
                pos = Position(i,j)
                literal.append(self.getPosIn1DArray(pos))

            self.cnf.append(literal)

        #exactly one queen at one column
        for i in range(self.size):
            literal = []
            for j in range(self.size):
                pos = Position(j,i)
                literal.append(self.getPosIn1DArray(pos))

            self.cnf.append(literal)

    def rowContraintAt(self, position: Position):
        startRow = Position(position.x,0)
        while startRow.validate(self.size):
            if not startRow == position:
                self.cnf.append([-self.getPosIn1DArray(position),-self.getPosIn1DArray(startRow)])
            startRow.rowIncrease()


    def columnContraintAt(self, position: Position):
        startColumn = Position(0,position.y)
        while startColumn.validate(self.size):
            if not startColumn == position:
                self.cnf.append([-self.getPosIn1DArray(position),-self.getPosIn1DArray(startColumn)])
            startColumn.columnIncrease()

    def backDiagonalConstraintAt(self, position: Position):
        startBackDiagonal:Position
        if position.x >= position.y:
            startBackDiagonal = Position(position.x - position.y,0)
        else:
            startBackDiagonal = Position(0,position.y - position.x)
        
        while startBackDiagonal.validate(self.size):
            if not startBackDiagonal == position:
                self.cnf.append([-self.getPosIn1DArray(position),-self.getPosIn1DArray(startBackDiagonal)])
            startBackDiagonal.backDiagonalIncrease()

    def forwardDiagonalConstraintAt(self, position: Position):
        startForwardDiagonal:Position
        if position.x >= self.size - position.y:
            startForwardDiagonal = Position(self.size - 1,position.x - position.y)
        else:
            startForwardDiagonal = Position(self.size - 1 - (self.size - 1 - position.y - position.x),0)
        
        while startForwardDiagonal.validate(self.size):
            if not startForwardDiagonal == position:
                self.cnf.append([-self.getPosIn1DArray(position),-self.getPosIn1DArray(startForwardDiagonal)])
            startForwardDiagonal.forwardDiagonalIncrease()

    



        

            
