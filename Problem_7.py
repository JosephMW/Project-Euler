from math import *


primes = []
searchNumber = 10001

index = 1

while (len(primes)<searchNumber):
    
    index += 1
    primeBool = True
    
    for element in primes:
        if index%element == 0:
            primeBool = False
            
    if primeBool:
        primes = primes + [index]

print(primes[-1])

