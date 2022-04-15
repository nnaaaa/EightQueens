from abc import ABC,abstractmethod
from typing import List
from pysat.formula import CNF
import numpy as np

class Level(ABC):
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



    @abstractmethod
    def initClauses(self):
        pass
    
