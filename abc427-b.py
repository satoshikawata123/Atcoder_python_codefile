def s(x):
    return sum(int(c) for c in str(x))

N = int(input().strip())
if N == 0:
    print(1)
else:
    a = 1
    for _ in range(N - 1):
        a += s(a)
    print(a)
