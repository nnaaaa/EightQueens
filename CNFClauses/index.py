from abc import ABC,abstractmethod

class CNF(ABC):
    def __init__(self,size):
        self.size = size
        self.resolutions = []

    @abstractmethod
    def getClausesAt(self,x,y):
        pass

