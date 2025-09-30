n,s = map(int,input().split())
t = [0]+list(map(int,input().split()))
for i in range(n):
  if t[i+1]-t[i] > s:
    print("No")
    break
else:
  print("Yes")
