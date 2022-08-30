from math import *



#messy but works well enough (4 is put in the list of primes)



listt = []

for i in range(2,ceil(sqrt(600851475143))):
    if 600851475143%i==0:
        #print(i)
        prime = True

        for j in range(2,ceil(sqrt(i))):
            #print('j',j)
            if i%j==0:
                prime=False

        if prime:
            listt = listt + [i]

print('primes: ',listt)
    
