A, B, C, D = map(int, input().split())

for i in range(1000):
  if i%2 == 0:
    C -= B
  else:
    A -= D

  if C<=0:
    print("Yes")
    exit()
  if A<=0:
    print("No")
    exit()
