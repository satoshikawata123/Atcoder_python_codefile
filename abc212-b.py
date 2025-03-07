x=input()
ans='Strong'
k=0
l=0

for i in range(3):
  if (int(x[i])+1)%10==int(x[i+1]):
    l+=1
  elif int(x[i])==int(x[i+1]):
    k+=1
if k==3 or l==3:
  ans='Weak'
print(ans)
