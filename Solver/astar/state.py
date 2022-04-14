
from typing import List

class State:
    def __init__(self,board: List[int],father):
        self.board = board
        self.isVisited = False
        self.isExpended = False
        self.gvalue = father.gvalue
        self.hvalue = 0
        self.father = father