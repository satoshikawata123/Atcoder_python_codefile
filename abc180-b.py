N = int(input())
X = [*map(int,input().split())]
m = 0
u = 0
c = 0

for i in range(N):
    m += abs(X[i])
    u += X[i]**2
    c = max(c,abs(X[i]))
print(m)
print(u**0.5)
print(c)
