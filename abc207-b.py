a, b, c, d = map(int, input().split())
l = 0
ans = 0

if b >= c * d:
    print(-1)
    exit()
while a > l * d:
    a += b
    l += c
    ans += 1
print(ans)
