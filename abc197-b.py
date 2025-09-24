H, W, X, Y = map(int, input().split())
S = [input() for i in range(H)]

X -= 1
Y -= 1
ans = 0
for i in range(H):
    f = True
    for j in range(min(i, X), max(i, X)+1):
        if S[j][Y] == '#':
            f = False
    if f:
        ans += 1
for i in range(W):
    f = True
    for j in range(min(i, Y), max(i, Y)+1):
        if S[X][j] == '#':
            f = False
    if f:
        ans += 1
print(ans-1)
