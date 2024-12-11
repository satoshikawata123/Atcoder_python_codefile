N=int(input())
a=list(map(int,input().split()))
sum=0

for i in range(0,N):
  sum+=a[i]
print(sum)
