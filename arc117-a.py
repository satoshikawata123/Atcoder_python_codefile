a,b=map(int,input().split())
e=[0]*(a+b)

for i in range(a):
    e[i]=i+1
for j in range(b):
    e[j+a]=-j-1
if sum(e)>0:
    e[-1]-=sum(e)
else:
    e[a-1]-=sum(e)
print(*e)
