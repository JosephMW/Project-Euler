from math import *

def lastTenDigs(num):
    strnum = str(num)
    if (len(strnum) > 10):
        return int(strnum[len(strnum) - 10:])
    return num

count = 0
i = 1

while(i <= 1000):
    count += lastTenDigs(i ** i)
    i += 1

print(count)