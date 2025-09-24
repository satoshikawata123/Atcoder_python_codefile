N,M,T = map(int,input().split())
n = N
t = 0

for i in range(M):
    A,B = map(int,input().split())
    n -= A-t
    t += A-t
    if n <= 0:
        print('No')
        break
    n += B-A
    t += B-A
    n = min(n,N)
else:
    n -= T-t
    print('Yes' if n > 0 else 'No')
