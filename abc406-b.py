N,K = map(int,input().split())
A = list(map(int,input().split()))
S = 1

for i in range(N):
    S *= A[i]
    if S >= 10**K:
        S = 1
