n=int(input())
a=[[0,0] for i in range(n)]
ans=0

for i in range(n):
    a[i][0],a[i][1]=map(int,input().split())
for i in range(n-1):
    for j in range(i+1,n):
        if -1 <= (a[j][1]-a[i][1])/(a[j][0]-a[i][0]) <= 1:
            ans+=1
print(ans)
