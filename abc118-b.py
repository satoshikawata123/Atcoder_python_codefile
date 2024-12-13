N,M=map(int,input().split())
cnt=[0]*M
ans=0

for _ in range(N):
    K,*A=map(int,input().split())
    for a in A:
        cnt[a-1] += 1

for c in cnt:
  if c==N:
    ans+=1

print(ans)
