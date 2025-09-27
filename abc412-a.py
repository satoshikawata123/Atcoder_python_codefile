N=int(input())
A=[]
B=[]
for i in range(N):
    a,b=map(int,input().split())
    A.append(a)
    B.append(b)

ans=0
for i in range(N):
    if B[i]>A[i]:
        ans+=1

print(ans)
