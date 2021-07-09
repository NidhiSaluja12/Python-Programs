from itertools import product
KM = list(map(int, input().split()))
K,M = KM[0],KM[1]
name = []
for i in range (K):
    name.append(list(map(int,input().split()))[1:])
N = list(product(*name))
answer = []
for i in N:
    sum1=0
    for j in i:
        sum1 += j ** 2
    answer.append(sum1 % M)
print(max(answer))
    
    

