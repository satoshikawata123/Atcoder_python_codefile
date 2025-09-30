N=int(input())
L=list(map(int,input().split()))
L.sort()
print(L)
sum=0
for i in range(N):
  sum+=L[2*i]
print(sum)
