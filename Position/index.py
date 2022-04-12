
from xmlrpc.client import boolean


class Position:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def validate(self, size: int) -> boolean:
        return self.x > 0 and self.x < size and self.y > 0 and self.y < size