from math import *

"""
NEVER FINISHED.
LOST INTEREST
"""

limit = 10000
maxVal = 0
maxN = 0


"""
This method is too slow
"""
"""
def totient(num):
    output = 0
    
    for i in range(1,num):
        if gcd(i,num)==1:
            output+=1
            
    return output
    
for i in range(2,limit+1):
    #print('i: ',i)
    #print('totient: ',totient(i))
    totVal = i/ totient(i)
    #print(totVal)
    if totVal >maxVal:
        maxVal = totVal
        maxN = i

print(maxN)
"""


val=1

while(val<1000000):
    val = val*nextPrime
    

print(val)
