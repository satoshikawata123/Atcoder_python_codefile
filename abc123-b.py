a=[]
b=10
e=0

for i in range(5):
  a.append(int(input()))
  if a[i]%10!=0:
    e+=10-a[i]%10
  if b > a[i]%10:
    b=a[i]%10

print(sum(a)+e+b-10)
