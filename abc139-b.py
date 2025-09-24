a,b = map(int,input().split())
c = 1
d = 0

while c < b:
  c += a - 1
  d += 1

print(d)
