from typing import List
from Clauses.index import Level
from Position.index import Position

def printChessBoard(queens: List[int],level: Level):
    for i in range(queens.__len__()):
        for j in range(queens.__len__()):
            pos = Position(i,j)
            hasQueen = False
            for z in range(queens.__len__()):
                chess = level.getPosIn2DArray(queens[z])
                if chess == pos:
                    print('Q',end=' ')
                    hasQueen = True

            if hasQueen == False:
                print('_',end=' ')
        
        print('\n')
