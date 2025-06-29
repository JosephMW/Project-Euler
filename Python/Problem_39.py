from math import *
from multiprocessing import current_process

def checkRightAngleTriangle(p,a,b):
    c = sqrt(a**2 + b**2)
    # print(c)
    if c.is_integer() and p == a + b + c:
        return (True,int(c))
    
    else:
        return (False, None)

def numberOfSolutionsForp(p):
    solutions = []
    for i in range(ceil(p/2)):
        for j in range(ceil(p/2)):
            (rightAngle, c) = checkRightAngleTriangle(p,i,j)
            if(rightAngle):
                solutions = addIfFirstCase(solutions, i, j, c)
    
    return len(solutions)


def addIfFirstCase(solutions, a, b, c):
    tuple = (0,0,0)
    if(a <= b and a<= c):
        if(b <= c):
            tuple = (a,b,c)
        else:
            tuple = (a,c,b)
    else:
        if(b <= c):
            if(a <= c):
                tuple = (b,a,c)
            else:
                tuple = (b,c,a)
        else:
            if(b <= a):
                tuple = (c, b, a)
            else:
                tuple = (c,a,b)
    
    # we know have ordered tuple (refactor above?)

    if tuple not in solutions:
        solutions.append(tuple)
    
    return solutions

def findBestp(limit):
    bestp = 0
    bestcount = 0
    currentcount = 0
    for i in range(1, limit +1):
        currentcount = numberOfSolutionsForp(i)
        if(currentcount >= bestcount):
            bestcount = currentcount
            bestp = i
    
    print(bestcount)
    return bestp

        


print(findBestp(1000))