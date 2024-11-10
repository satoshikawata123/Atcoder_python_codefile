a,b,c=(map(int,input().split()))
k=int(input())

d=max(a,b,c)
e=a+b+c-d

for i in range(k):
    d=d*2

print(e+d)
