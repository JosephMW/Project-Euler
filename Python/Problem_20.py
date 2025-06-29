from math import *

fac100 = factorial(100)

# First approach here: Correct but too slow!
def countDigits(num):
    count = 0
    while(num > 0):
        print(num)
        while(num%10 != 0):
            count +=1
            num -=1
            print(num)
        num = num / 10
    
    return count

# Second approach here: Correct and Fast! Needed stringification
def countDigits2(num):
    stringed = str(num)
    total = 0
    for i in range(len(stringed)):
        total += int(stringed[i])
    
    return total

print(countDigits2(fac100))