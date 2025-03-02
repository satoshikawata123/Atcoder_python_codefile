a = map(int,input().split())
a = [i for i in sorted(a)]

if a[0] * a[1] == a[2]:
    print("Yes")
else:
    print("No")
