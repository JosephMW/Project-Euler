from gettext import find
from math import *

def numOfRects(cols, rows):
    rwidth = cols
    rheight = rows

    total = 0
    numberOfSpecificDimRect = 0
    while(rwidth > 0):
        rheight = rows
        while(rheight > 0):
            numberOfSpecificDimRect = (1 + cols - rwidth) * (1 + rows - rheight)
            total += numberOfSpecificDimRect

            rheight -= 1
        
        rwidth -= 1

    return total

# print("HERE: " + str(numOfRects(1999,1)))


def findClosestGrid2mil():
    cols = 53
    rows = 1

    bestArea = 0
    closestNumberOfRects = 2000000
    bestCols = 0
    bestRows = 0

    while(cols <= 1999):
        rows = 1

        # print("cols: " + str(cols) + ", rows: " + str(rows) + "\n")
        while(rows <= 53):
            numRects = numOfRects(cols,rows)
            distanceTo2mil = abs(numRects - 2000000)

            if(distanceTo2mil < closestNumberOfRects):
                closestNumberOfRects = distanceTo2mil
                bestArea = cols * rows
                bestCols = cols
                bestRows = rows
            
            if(numRects > 2000000):
                # print("breaking - cols: " + str(cols) + ", rows: " + str(rows) + "\n")
                break
            
            rows += 1
        cols += 1
    
    print("closestNumberOfRects: " + str(closestNumberOfRects))
    print("bestArea: " + str(bestArea))
    print("bestCols: " + str(bestCols))
    print("bestRows: " + str(bestRows))

findClosestGrid2mil()

