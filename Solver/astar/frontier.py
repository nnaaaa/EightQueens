
from typing import List
from uuid import UUID
from Solver.astar.state import State


class Frontier:
    def __init__(self):
        self.__list:List[State] = []

    def isEmpty(self):
        return len(self.__list) == 0

    def remove(self,state:State):
        self.__list.remove(state)

    def push(self,state:State):
        self.__list.append(state)

    def putStateWithLowestFValue(self) -> State:
        stateWithLowestFValue = None
        for state in self.__list:
            if not stateWithLowestFValue:
                stateWithLowestFValue = state
            else:
                lowestFValue = stateWithLowestFValue.gvalue + stateWithLowestFValue.getHeuristicValue()
                fvalue = state.gvalue + state.getHeuristicValue()
                if fvalue < lowestFValue:
                    stateWithLowestFValue = state

        self.__list.remove(stateWithLowestFValue)
        return stateWithLowestFValue

    def isExist(self,state:State):
        node = self.findById(state.id)
        if node:
            return True
        else:
            return False

    def findById(self,id:UUID):
        for node in self.__list:
            if node.id == id:
                return node

        return None
            
