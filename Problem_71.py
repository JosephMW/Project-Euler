from math import *


limit = 1000000
maxim = 2/7



for i in range(2,limit+1):
    a= floor(3*i/7)/i
    if a>maxim and a!=3/7:
        maxim = a
        num = (floor(3*i/7),i)

print(maxim)
print(num)

