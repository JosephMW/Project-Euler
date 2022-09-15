from math import *
from re import search

def generateTris(limit):
    tris = []
    for i in range(limit):
        tris.append(i * (i+1)/2)
    
    return tris
    
def generatePents(limit):
    pents = []
    for i in range(limit):
        pents.append(i * (3*i - 1)/2)
    
    return pents

def generateHexs(limit):
    hexs = []
    for i in range(limit):
        hexs.append(i * (2*i - 1))
    
    return hexs

def searchListsForCommon(tris, pents, hexs):
    it = 0
    ip = 0
    ih = 0

    while(True):
        valt = tris[it]
        valp = pents[ip]
        valh = hexs[ih]

        # The case where we have commonality:
        if(valt == valp and valp == valh):
            if (valh > 40755):
                return valt
            else:
                it += 1


        if(valt < valp):
            if(valt < valh):
                it += 1
            else:
                ih += 1
        else:
            if(valp < valh):
                ip += 1
            else:
                ih += 1

    
triangles = generateTris(100000)
pentagons = generatePents(100000)
hexagons = generateHexs(100000)
print(searchListsForCommon(triangles, pentagons, hexagons))
















"""
Attempt Number 1 below. Far too slow.
"""

# from math import * 

# def checkTriangle(num):
#     n = floor(sqrt(2 * num))

#     if (n * (n+1)/2 == num):
#         return True
#     else:
#         return False


# def checkPentagon(n, num):
#     if(n * (3 * n - 1) == num * 2):
#         return True
#     else:
#         return False

# def checkHexagon(n, num):
#     if(n * (2 * n - 1) == num):
#         return True
#     else:
#         return False

# def checkAllThree(num):
#     if not checkTriangle(num):
#         return False
    
#     count = 0
#     for i in range(ceil(sqrt(num))):
#         if checkPentagon(i, num):
#             count += 1
        
#         if checkHexagon(i, num):
#             count += 1
        
#         if count == 2:
#             return True
    
#     return False




# # number = 586500000
# number = 40756
# while(not checkAllThree(number)):
#     if number % 1000000 == 0:
#         print(number)
#     number += 1

# print(number)

