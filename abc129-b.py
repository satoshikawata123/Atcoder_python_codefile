N = int(input())
W = list(map(int, input().split()))
m = sum(W)

for i in range(1, N):
    A = sum(W[:i])
    B = sum(W[i:])
    m = min(abs(A-B), m)

print(m)
