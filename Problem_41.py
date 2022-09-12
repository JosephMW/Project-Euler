from math import *

def checkPandigital(num):
    dict = {}
    for i in str(num):
        if (i in dict) or (i == "0") or (int(i) > len(str(num))):
            return False
        else:
            dict[i] = 1
    
    count = 0
    for i in dict:
        count += 1
    
    if count == len(str(num)):
        return True
    else:
        return False

def checkPrime(num):
    for i in range(2,ceil(sqrt(num))):
        if (num % i == 0):
            return False
    return num > 1
    
def largestPrimePandigital():
    largest = 0
    for i in range(1,987654322):
        if(checkPandigital(i)):
            if(checkPrime(i)):
                largest = i
    
    return largest

print(largestPrimePandigital())


