N = int(input())
H = list(map(int, input().split()))

maxh = 0
ans = 0
for h in H:
    if maxh <= h:
        ans += 1
        maxh = h

print(ans)
