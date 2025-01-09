N,A,B = map(int,input().split())
s = N //(A+B)
t = N - s*(A+B)

if(t <= A):
    print(s*(A) + t)
else:
    print(s*(A) + A)
