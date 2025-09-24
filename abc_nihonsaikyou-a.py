#saikyogakusei-1stA
M,D=map(int,input().split())
ans=0
i=1

while i<=M:
    j=1
    while j<=D:
        P=j//10
        Q=j%10
        if P*Q==i and P>1 and Q>1:
            ans+=1
        j+=1
    i+=1

print(ans)
