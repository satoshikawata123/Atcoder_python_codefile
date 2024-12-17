import math
N,D = map(int,input().split())
X = []
a = 0
b = 0
c = 0

for i in range(N):
  x = list(map(int,input().split()))
  X.append(x)

for i in range(N-1):
  for j in range(i+1,N):
    for k in range(D):
      a += abs(X[i][k] - X[j][k])**2
    a = math.sqrt(a)
    if a-int(a) == 0.0:
      c += 1
    a = 0

print(c)
