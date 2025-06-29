from math import *


numbers = []
limit=100000

for i in range(2,limit):
    numbers = numbers + [i]


for ind in range(ceil(sqrt(len(numbers)))):
    #print(numbers)
    #print(ind)
    #print(numbers[ind])
    toRemove = []
    try:
        upper = numbers[ind]
    except:
        break
    
    for x in range(2*numbers[ind],limit,upper):
        toRemove = toRemove + [x]
    #print('rem: ',toRemove)
    for y in toRemove:
        try:
            numbers.remove(y)
        except:
            pass
    #print('----------------------------')

primeSum = 0
for prime in numbers:
    primeSum += prime

print(primeSum)
