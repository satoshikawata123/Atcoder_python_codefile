a,v = map(int,input().split())
b,w = map(int,input().split())
t = int(input())
dis = (v - w) * t

if dis >= abs(a - b):
  print("YES")
else:
  print("NO")
