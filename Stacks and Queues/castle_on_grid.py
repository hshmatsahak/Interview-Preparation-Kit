#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumMoves function below.
def minimumMoves(grid, startX, startY, goalX, goalY):
    queue = []
    queue.append((startX, startY, 0))
    move = queue.pop(0)
    instack = []
    for i in range(len(grid)):
        temp = []
        for j in range(len(grid)):
            temp.append(False)
        instack.append(temp)
    while(not (move[0]==goalX and move[1]==goalY)):
        gridright = gridleft = gridup = griddown = move
        while (griddown[0]+1<len(grid) and grid[griddown[0]+1][griddown[1]]=='.'):
            griddown = (griddown[0]+1, griddown[1], move[2]+1)
            if (not instack[griddown[0]][griddown[1]]):
                queue.append(griddown)
                instack[griddown[0]][griddown[1]] = True
        while (gridup[0]-1>=0 and grid[gridup[0]-1][gridup[1]]=='.'):
            gridup = (gridup[0]-1, gridup[1], move[2]+1)
            if (not instack[gridup[0]][gridup[1]]):
                queue.append(gridup)
                instack[gridup[0]][gridup[1]] = True
        while (gridright[1]+1<len(grid) and grid[gridright[0]][gridright[1]+1]=='.'):
            gridright = (gridright[0], gridright[1]+1, move[2]+1)
            if (not instack[gridright[0]][gridright[1]]):
                queue.append(gridright)
                instack[gridright[0]][gridright[1]] = True
        while (gridleft[1]-1>=0 and grid[gridleft[0]][gridleft[1]-1]=='.'):
            gridleft = (gridleft[0], gridleft[1]-1, move[2]+1)
            if (not instack[gridleft[0]][gridleft[1]]):
                queue.append(gridleft)
                instack[gridleft[0]][gridleft[1]] = True
        move = queue.pop(0)
    print(move[2])
    return move[2]
            
            
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    startXStartY = input().split()

    startX = int(startXStartY[0])

    startY = int(startXStartY[1])

    goalX = int(startXStartY[2])

    goalY = int(startXStartY[3])

    result = minimumMoves(grid, startX, startY, goalX, goalY)

    fptr.write(str(result) + '\n')

    fptr.close()