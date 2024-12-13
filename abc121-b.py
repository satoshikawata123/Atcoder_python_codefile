n,m,c = map(int,input().split())
b = list(map(int,input().split()))
ans = 0

for i in range(n):
  arr = list(map(int,input().split()))
  temp = c
  for j in range(m):
    temp += arr[j] * b[j]
  if temp > 0:
    ans +=1

print(ans)
