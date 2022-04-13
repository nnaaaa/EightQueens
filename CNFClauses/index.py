from abc import ABC,abstractmethod
from pysat.formula import CNF

class EightQueenCNF(ABC):
    def __init__(self,size):
        self.size = size
        self.resolutions = CNF()

    @abstractmethod
    def getClausesAt(self,x,y):
        pass

