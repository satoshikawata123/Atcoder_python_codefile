n = int(input())

p=[]
q=[]

for i in range(n):
  s,a = map(str,input().split())
  p.append(s)
  q.append(int(a))

st = q.index(min(q))
ans=p[st:] +p[:st]

print(*ans , sep='\n')
