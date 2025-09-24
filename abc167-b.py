a,b,c,k = map(int,input().split())

if a >= k:
  print(k)
elif a + b >= k:
  print(a)
else:
  x = k - (a + b)

  print(a - x)
