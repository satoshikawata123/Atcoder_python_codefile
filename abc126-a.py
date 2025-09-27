N,K=map(int,input().split())
S = input()
result = S[:K-1] + S[K-1].lower() + S[K:]
print(result)
