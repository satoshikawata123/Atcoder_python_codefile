n=int(input())
c=0

for i in range(1,n+1):
    i=str(i)
    if len(i)%2!=0:
        c+=1

print(c)
