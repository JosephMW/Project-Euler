def nextElementInSequence(num):
    strnum = str(num)
    new = 0

    for i in strnum:
        new += int(i) ** 2
    
    return new

ones = []
eightynines = []

def iterateNumber(num):
    builtList = [num]
    while(num != 89 and num != 1):
        if num in ones:
            num = 1
        else:
            if num in eightynines:
                num = 89
            else:
                num = nextElementInSequence(num)
                builtList.append(num)
    
    if num == 1:
        ones.extend(builtList)
        return 1
    else:
        eightynines.extend(builtList)
        return 89

def iterateNumberSimple(num):
    while(num != 89 and num != 1):
        num = nextElementInSequence(num)
    
    if num == 1:
        return 1
    else:
        return 89

def howManyBelow(limit):
    count = 0
    for i in range(1, limit):
        result = iterateNumberSimple(i)
        if result == 89:
            count += 1
    
    return count

print(howManyBelow(10000000))

# print("ones:")
# print(ones)
# print("eightynines:")
# print(eightynines)
        



