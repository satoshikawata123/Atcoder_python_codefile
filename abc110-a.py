a,b,c=map(int,input().split())
if a>=b and a>=c:
  print(10*a+b+c)
elif b>=a and b>=c:
  print(10*b+a+c)
else:
  print(10*c+a+b)
