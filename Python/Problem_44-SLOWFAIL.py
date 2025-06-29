from math import *
    
def generatePents(limit):
    pents = []
    for i in range(1, limit):
        pents.append(i * (3*i - 1)/2)
    
    return pents

pents = generatePents(10000)
solutions = []

for i in range(len(pents)):
    for j in range(i+1, len(pents)):
        pi = pents[i]
        pj = pents[j]
        if (pi+pj) in pents:
            if (pj-pi) in pents:
                print("pi: " + str(pi) + " pj: " + str(pj))
                solutions.append(pj-pi)

print(solutions)

