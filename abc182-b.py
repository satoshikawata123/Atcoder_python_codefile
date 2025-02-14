N=int(input())
A=list(map(int,input().split()))

import math

ans=0

for k in range(2,1001):
    n=0
    for a in A:
        if a%k==0: n+=1
    if n>ans:
        ans=n
        km=k
print(km)
