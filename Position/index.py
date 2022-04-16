
class Position:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def validate(self, size: int) -> bool:
        return self.x >= 0 and self.x < size and self.y >= 0 and self.y < size

    def __eq__(self,after):
        return self.x == after.x and self.y == after.y

    def backDiagonalIncrease(self):
        self.x += 1
        self.y += 1

    def forwardDiagonalIncrease(self):
        self.x -= 1
        self.y += 1

    def backDiagonalDecrease(self):
        self.x -= 1
        self.y -= 1

    def forwardDiagonalDecrease(self):
        self.x += 1
        self.y -= 1

    def rowIncrease(self):
        self.y += 1
    
    def columnIncrease(self):
        self.x += 1

    @staticmethod
    def getPosIn2DArray(position: int,size: int):
        pos = position - 1
        return Position(pos % size,pos // size)

    @staticmethod
    def getPosIn1DArray(position,size: int) -> int:
        return position.y * size + position.x + 1

