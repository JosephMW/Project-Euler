from math import *

def checkCircularPrime(num):
    strnum = str(num)
    for i in range(len(strnum)):
        # print(int(strnum[i:] + strnum[:i]))
        if (not checkPrime(int(strnum[i:] + strnum[:i]))):
            return False
    return True

def checkPrime(num):
    if num == 2: 
        return True

    for i in range(2,ceil(sqrt(num)) + 1):
        if (num % i == 0):
            return False
    return num > 1
    
def howCPManyBelow(limit):
    count = 0
    for i in range(limit):
        if(checkCircularPrime(i)):
            # print(i)
            count += 1

    return count

# print(checkPrime(25))
print(howCPManyBelow(1000000))


