N,K = map(int,input().split())
C = [0 for _ in range(N)]

for _ in range(K):
    d = int(input())
    A = list(map(int,input().split()))
    for a in A:
        C[a-1] += 1

print(C.count(0))
