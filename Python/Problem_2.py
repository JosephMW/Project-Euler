a=1
b=1
sum=0

while(b<4000000):
    if (b%2==0):
        sum = sum+b
    intermediate=a
    a=b
    b=intermediate+b

print(sum)
