n,x=map(int,input().split())
a=map(int,input().split())
flag=0
for i in a:
  if i==x:
    flag+=1
if flag==0:
  print("No")
else:
  print("Yes")
