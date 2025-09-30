A, B = map(int, input().split())
d = A/B
e = int(A/B)
f = d - e

if f > 0.5:
    print(e+1)
else:
    print(e)
