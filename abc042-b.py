N,L=map(int,input().split())
sum=[]
for i in range(N):
  sum.append(str(input()))

sum.sort()
print("".join(sum))
