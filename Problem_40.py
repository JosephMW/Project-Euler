def solve():
    index = 1
    num = str(index)
    while(len(num) < 10000003):
        num += str(index)
        index += 1
    
    calc = int(num[1]) * int(num[10]) * int(num[100]) * int(num[1000]) * int(num[10000]) * int(num[100000]) * int(num[1000000])

    return calc

print(solve())


