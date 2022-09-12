from math import *
from tabnanny import check

def checkPandigital(a,b,c):
    strnum = str(a) + str(b) + str(c)
    dict = {}
    for i in strnum:
        if i in dict or i == "0":
            return False
        else:
            dict[i] = 1
    
    count = 0
    for i in dict:
        count += 1
    
    if count == 9:
        return True
    else:
        return False

# print(checkPandigital(13, 32, 4567089))

def findPandigitalProducts(alimit, blimit):
    products = []

    for a in range(alimit):
        for b in range(blimit):
            product = a * b
            if (checkPandigital(a,b,product) and (product not in products)):
                products.append(product)

    total = 0
    for i in products:
        total += i
    
    return total

print(findPandigitalProducts(9999, 9999))


