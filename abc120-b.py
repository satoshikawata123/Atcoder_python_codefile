a,b,k=map(int,input().split())
count=0
list=[]

for i in range(1,101):
  if a%i==0 and b%i==0:
    list.append(i)

list.sort(reverse=True)
print(list[k-1])
