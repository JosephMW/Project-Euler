from math import *


sumOfSquares = 0
squareOfSum = 0

for i in range(1,101):
    sumOfSquares = sumOfSquares + i*i
    squareOfSum = squareOfSum + i

print('sum: ',squareOfSum)
print('squareOfSum: ',squareOfSum * squareOfSum)
print('sumOfSquares: ',sumOfSquares)

print('difference: ',squareOfSum * squareOfSum - sumOfSquares)
