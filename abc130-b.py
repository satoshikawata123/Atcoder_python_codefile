n,x=map(int,input().split())
l=list(map(int,input().split()))
p=[]
q=1

for i in range(n):
  p.append(l[i])
  s=sum(p)
  if s<=x:
    q+=1
  else:
    break

print(q)
