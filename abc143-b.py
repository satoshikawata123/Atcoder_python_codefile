N = int(input())
A = [int(x) for x in input().split()]
s = sum(A)
ans = 0

for x in A :
  s -= x
  ans += s * x

print(ans)
