N,X=map(int,input().split())
X*=100
now=0

for i in range(N):
    v,p=map(int,input().split())
    now+=v*p
    if X<now:
        print(i+1)
        exit()
print(-1)
