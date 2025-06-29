from math import *

# THIS IS WORKING BUT IS COUNTING DUPLICATE SOLUTIONS

dictionary = {}

def recursive(original, number, limit):
    if number == 1 or number == 0:
        return 1

    combinations = 0
    for i in range(number):
        mainGroup = number - i
        leftover = i

        if(mainGroup > limit):
            continue

        # print("maing: " + str(mainGroup) + " leftover: " + str(leftover))
        # how many ways to group leftover?
        if (leftover in dictionary):
            if(mainGroup in dictionary[leftover]):
                currentOptions = dictionary[leftover][mainGroup]
            else:
                currentOptions = recursive(original, leftover, mainGroup)
                dictionary[leftover][mainGroup] = currentOptions
        else:
            currentOptions = recursive(original, leftover, mainGroup)
            dictionary[leftover] = {}
            dictionary[leftover][mainGroup] = currentOptions
        
        if(original == number):
            print("MainGroup: " + str(mainGroup) + " with leftover: " + str(leftover) + " yields combinations: " + str(currentOptions))
        combinations += currentOptions
    
    # print("number: " + str(number) + " combinations: " + str(combinations))
    return combinations

def findPossibleGroupings(num):
    return recursive(num, num, num + 1) - 1 #subtracting case of all 100 + 0

print(findPossibleGroupings(100))
