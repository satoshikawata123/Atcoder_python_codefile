n,m=map(int,input().split())
a=set(list(map(int,input().split())))
b=set(list(map(int,input().split())))

print(*a^b)
