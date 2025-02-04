n=int(input())
L=list(map(int,input().split()))
tot=sum(L)
T=0
ans=10**18

for i in range(n):
  T+=L[i]
  if tot//2<=T:
    ans=min(ans,abs(tot-2*T))
    T-=L[i]
    ans=min(ans,abs(tot-2*T))
    break
print(ans)
