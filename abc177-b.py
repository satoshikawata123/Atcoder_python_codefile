S=input()
T=input()

n=len(S)
m=len(T)

ans=n
for s in range(n-m+1):
    d=0
    for i in range(m):
        if S[i+s]!=T[i]: d+=1
    ans=min(ans,d)
print(ans)
