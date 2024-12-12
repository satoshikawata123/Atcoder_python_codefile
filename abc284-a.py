N = int(input())
S = list()
for i in range(N):
  S.append(input())

for j in range(N):
  print("".join(S[-j - 1]))
