N=int(input())
T=list(input())
A=list(input())
count=0

for i in range(N):
  if T[i]==A[i]=="o":
    count+=1

if count>0:
  print("Yes")
else:
  print("No")
