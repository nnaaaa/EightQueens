from turtle import pos
from index import CNF
from ..Position.index import Position
class Level_1(CNF):
    def __getPosIn2DArray(self, position: int) -> Position:
        return position // self.size, position % self.size

    def __getPosIn1DArray(self, position: Position) -> int:
        return position.x * self.size + position.y

    def getClausesAt(self, position: Position):
        if not position.validate(self.size):
            return []
        
        for row in range(self.size):
            



level1 = Level_1(8)

level1.getClauses(4,5)