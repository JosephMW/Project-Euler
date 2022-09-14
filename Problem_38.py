from math import *

def checkPandigital(num):
    dict = {}
    for i in str(num):
        if (i in dict) or (i == "0") or (int(i) > len(str(num))):
            return False
        else:
            dict[i] = 1
    
    count = 0
    for i in dict:
        count += 1
    
    if count == len(str(num)):
        return True
    else:
        return False

def largest9pandigital():

    largestPandigital = 0
    for i in range(9999):
        strnum = ""
        multiplier = 1

        while(len(strnum) < 9):
            strnum += str(i * multiplier)
            multiplier += 1

        num = int(strnum)
        if(len(strnum) == 9 and num > largestPandigital):
            if checkPandigital(num):
                largestPandigital = num
    
    return largestPandigital

print(largest9pandigital())



