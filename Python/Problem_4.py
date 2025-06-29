from math import *


limit = 999
#low limit 10, 100?
maxim = 0

def checkPalin(number):
    l = list(str(number))
    return l==l[::-1]
    

for i in range(1,limit+1):
    for j in range(1,i+1):
        a = i*j
        if checkPalin(a):
            if a>maxim:
                maxim = a

print(maxim)
