from math import *


primes = [2]
searchNumber = 300000
primeSum = 0

index = 1
while (primes[-1]<searchNumber):
    
    index += 2
    primeBool = True
    #print(index)
    for element in primes:
        if index%element == 0:
            primeBool = False
            break
        #print('still inside')
            
    if primeBool:
        primes = primes + [index]
        primeSum+=index

print(primes[-1])
print(primeSum-primes[-1])

