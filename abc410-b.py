N,Q = map(int,input().split())
X = list(map(int,input().split()))
box = [0 for _ in range(N)]
L = []

for i in range(Q):
    if X[i] == 0:
        M = min(box)
        for i in range(N):
            if box[i] == M:
                box[i] += 1
                L.append(i+1)
                break
    else:
        box[X[i]-1] += 1
        L.append(X[i])

print(*L)
