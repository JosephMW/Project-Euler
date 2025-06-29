from math import *

sum = 0
i = 1
# first ring
sum += i

# second ring
ringnum = 2
ringsize = 8
i = 2

while(i < 1002001):
    print("------ NEW RING STARTING ------")
    howOftenAdd = 2 * (ringnum - 1)

    counter = 1
    for j in range(i,i+ ringsize):
        if (counter % howOftenAdd == 0):
            print("about to add: " + str(j))
            sum += j
            print("sum is now: " + str(sum))
        counter += 1
    
    i = i + ringsize
    print(i)
    ringsize += 8
    ringnum += 1



