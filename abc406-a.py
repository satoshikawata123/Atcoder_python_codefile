a,b,c,d=map(int, input().split())
deadline=100*a+b
submit=100*c+d

if deadline>submit:
    print("Yes")
else:
    print("No")
