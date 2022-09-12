from math import *

# print(bin(585)[2:])

def sumUnderMil():
    sum = 0
    for i in range(0,1000000):
        if(checkDoublePalindrome(i)):
            sum += i

    return sum

def checkDoublePalindrome(num):
    numstr = str(num)
    numbin = bin(num)[2:]

    if(checkPalindrome(numstr) and checkPalindrome(numbin)):
        return True
    else: 
        return False

def checkPalindrome(numstr):
    for i in range(ceil(len(numstr) / 2)):
        if(numstr[i] != numstr[-i-1]):
            return False
    
    return True

print(sumUnderMil())
