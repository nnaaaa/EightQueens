from abc import ABC,abstractmethod

class QueenSolver(ABC):
    def __init__(self):
        self.graphic = None

    @abstractmethod
    def solve():
        pass

    def setGraphic(self,graphic):
        self.graphic = graphic