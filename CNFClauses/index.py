from abc import ABC,abstractmethod

class CNF(ABC):
    def __init__(self,size):
        self.size = size

    @abstractmethod
    def getClauses(self,x,y):
        pass

