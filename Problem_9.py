from math import *

#a<b<c

#1<=a <=333
#2<=b<=499
#335<=c<=997

"""
squares = []


for x in range(1,997):
    squares = squares + [x*x]

print(squares)
"""

for a in range(1,334):
    for c in range(335,1001-a -(a+1)):

        b = 1000 - c -a
        if b*b == c*c - a*a:
            print('a: ',a,' b: ',b,' c: ',c)
        
