n=int(input())
a=list(map(int,input().split()))
b=list(map(int,input().split()))

if max(a)<=min(b):
  print(min(b)-max(a)+1)
else:
  print(0)
