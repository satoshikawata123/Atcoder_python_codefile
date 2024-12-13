N=int(input())
sum=0

for i in range(N):
  x,u=map(str,input().split())
  x=float(x)
  if u=='BTC':
    x*=380000
  sum+=x

print(sum)
