n = int(input())
g = [list(map(int,input().split())) for i in range(n)]
i = 0

for j in range(n):
    if i >= j + 1:i = g[i-1][j]
    else:i = g[j][i-1]
print(i)
