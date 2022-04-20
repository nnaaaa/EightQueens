from typing import List
from pysat.formula import CNF
import numpy as np
from Position.index import Position
class Level():
    def __init__(self,size):
        self.cnf = CNF()
        self.size = size 
        self.initClauses()

    def getClauses(self) -> List[List[int]]:
        return self.cnf.clauses

    def isExistInClauses(self,literal: List[int]):
        for clause in self.cnf.clauses:
            clause.sort()
            literal.sort()
            if len(clause) != len(literal):
                continue
            c1 = np.array(clause)
            c2 = np.array(literal)
            if (c1 == c2).all():
                return True

        return False

    def printClauses(self):
        f = open("clauses.txt","w")
        for clause in self.cnf.clauses:
            for i in range(len(clause)):
                if i == 0:
                    #print('(',clause[i],end=' V ')
                    f.write('('+str(clause[i])+' V ')
                elif i == len(clause) - 1:
                    #print(clause[i],end=')\n')
                    f.write(str(clause[i])+')\n')
                else:
                    #print(clause[i],end=' V ')
                    f.write(str(clause[i])+' V ')

    def printClausesSpecially(self):
        f = open("clauses.txt","w")
        for clause in self.cnf.clauses:
            
            for i in range(len(clause)):
                pos = Position.getPosIn2DArray(abs(clause[i]),self.size)
                special = 'b[' + str(pos.y) + ',' + str(pos.x) + ']'
                if clause[i] < 0:
                    special = '-' + special

                if i == 0:
                    f.write('('+special+' V ')
                elif i == len(clause) - 1:
                    f.write(special+') ^\n')
                else:
                    f.write(special+' V ')

    def restrictionAt(self,pos:Position):
        self.columnContraintAt(pos)
        self.rowContraintAt(pos)
        self.forwardDiagonalConstraintAt(pos)
        self.backDiagonalConstraintAt(pos)

    def rowContraintAt(self, position: Position):
        startRow = Position(position.x,0)
        while startRow.validate(self.size):
            if not startRow == position:
                self.cnf.append([-Position.getPosIn1DArray(position,self.size),-Position.getPosIn1DArray(startRow,self.size)])
            startRow.rowIncrease()

    def columnContraintAt(self, position: Position):
        startColumn = Position(0,position.y)
        while startColumn.validate(self.size):
            if not startColumn == position:
                self.cnf.append([-Position.getPosIn1DArray(position,self.size),-Position.getPosIn1DArray(startColumn,self.size)])
            startColumn.columnIncrease()

    def backDiagonalConstraintAt(self, position: Position):
        startBackDiagonal:Position
        if position.x >= position.y:
            startBackDiagonal = Position(position.x - position.y,0)
        else:
            startBackDiagonal = Position(0,position.y - position.x)
        
        while startBackDiagonal.validate(self.size):
            if not startBackDiagonal == position:
                self.cnf.append([-Position.getPosIn1DArray(position,self.size),-Position.getPosIn1DArray(startBackDiagonal,self.size)])
            startBackDiagonal.backDiagonalIncrease()

    def forwardDiagonalConstraintAt(self, position: Position):
        startForwardDiagonal:Position
        if position.x >= self.size - position.y:
            startForwardDiagonal = Position(self.size - 1,position.x - position.y)
        else:
            startForwardDiagonal = Position(self.size - 1 - (self.size - 1 - position.y - position.x),0)
        
        while startForwardDiagonal.validate(self.size):
            if not startForwardDiagonal == position:
                self.cnf.append([-Position.getPosIn1DArray(position,self.size),-Position.getPosIn1DArray(startForwardDiagonal,self.size)])
            startForwardDiagonal.forwardDiagonalIncrease()

    def initClauses(self):
        pass
    
