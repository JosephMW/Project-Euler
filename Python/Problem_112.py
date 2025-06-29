from math import *
from operator import truediv
from tabnanny import check

def checkDecreasing(strnum):
    for i in range(len(strnum) - 1):
        if(strnum[i+1] > strnum[i]):
            return False
    return True

def checkIncreasing(strnum):
    for i in range(len(strnum) - 1):
        if(strnum[i+1] < strnum[i]):
            return False
    return True

def checkBouncy(num):
    strnum = str(num)
    if (not checkDecreasing(strnum) and not checkIncreasing(strnum)):
        return True
    return False


numBouncy = 0
max = 1
while(numBouncy / max < 0.99):
    max += 1
    if checkBouncy(max):
        numBouncy += 1

print("Number of Bouncy: " + str(numBouncy))
print("Max: " + str(max))