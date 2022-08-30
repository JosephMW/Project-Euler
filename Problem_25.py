from math import *

x = 1
y = 1
i = 2
while (len(str(y)) < 1000):
    i += 1
    temp = y
    y = x + y
    x = temp

print("First above 1000 digits: " + str(y))
print(i)