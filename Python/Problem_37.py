from math import *

def checkPrime(num):
    if num == 2: 
        return True

    for i in range(2,ceil(sqrt(num)) + 1):
        if (num % i == 0):
            return False
    return num > 1

def checkTruncatablePrime(num):
    if not checkPrime(num):
        return False

    strnum = str(num)
    numdigits = len(strnum)
    if(numdigits == 1):
        return False

    for i in range(1, numdigits):
        if(not checkPrime(int(strnum[i:])) or not checkPrime(int(strnum[:i]))):
            return False
    
    return True

def sumTruncatablePrimes():
    count = 0
    sum = 0
    i = 10
    while(count < 11):
        if checkTruncatablePrime(i):
            print(i)
            sum += i
            count += 1

        i += 1
    
    return sum

print(sumTruncatablePrimes())