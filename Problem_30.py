from math import *

def seperateDigits(num):
    # We know num is 5 digs long:
    numstr = str(num)
    digs = []
    for i in numstr:
        digs.append(int(i))

    return (digs)

def powerCalculation(digList):
    total = 0
    for i in digList:
        total += i ** 5
    return total

def checkEqualsBlah(num):
    if num == powerCalculation(seperateDigits(num)):
        return True
    else:    
        return False

def sumSpecialNumsInRangeInclusive(bottom, top):
    total = 0
    for i in range(bottom, top+1):
        if(checkEqualsBlah(i)):
            total += i
    
    return total

print(sumSpecialNumsInRangeInclusive(2,9999999))
    