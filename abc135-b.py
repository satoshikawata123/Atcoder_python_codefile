m=int(input())
n=list(map(int,input().split()))
c=0

for i in range(1,m):
    if i!=n[i-1]:
        c+=1

if c<=2:
    print('YES')
elif c>2:
    print('NO')
