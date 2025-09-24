L = list(map(int, input().split()))

L.sort()

a = L.count(L[0])
b = 0
if a == 1 or a == 2 or a == 3:
  b = L.count(L[3])

print("Yes" if a+b == 4 and a != 4 else "No" )
