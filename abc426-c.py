import sys
sys.setrecursionlimit(1 << 25)
input=sys.stdin.readline

N,Q=map(int,input().split())
p=list(range(N+1))
c=[0]*(N+1)
for i in range(1,N+1):
    c[i]=1

def find(x):
    if p[x]!=x:
        p[x]=find(p[x])
    return p[x]

out=[]
for _ in range(Q):
    X,Y=map(int,input().split())
    s=0
    i=find(X)
    while i>0:
        s+=c[i]
        c[i]=0
        p[i]=find(i-1)
        i=find(i)
    c[Y]+=s
    out.append(str(s))
print("\n".join(out))
