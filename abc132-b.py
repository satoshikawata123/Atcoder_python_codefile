n = int(input())
p = [0] + list(map(int, input().split()))
res = 0

for i in range(2, n):
  res += (sorted([p[i - 1], p[i], p[i + 1]])[1] == p[i])

print(res)
