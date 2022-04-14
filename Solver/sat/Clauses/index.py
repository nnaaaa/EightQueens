from abc import ABC,abstractmethod
from typing import List
from pysat.formula import CNF
from Position.index import Position

class Level(ABC):
    def __init__(self,size = 8):
        self.cnf = CNF()
        self.size = size 
        self.initClauses()

    def getPosIn2DArray(self, position: int) -> Position:
        pos = position - 1
        return Position(pos // self.size, pos % self.size)

    def getPosIn1DArray(self, position: Position) -> int:
        return position.x * self.size + position.y + 1

    def getClauses(self) -> List[List[int]]:
        return self.cnf.clauses

    @abstractmethod
    def initClauses(self):
        pass
    
