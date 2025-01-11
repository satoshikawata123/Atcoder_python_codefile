n, m = map(int, input().split())
a = list(map(int, input().split()))
x = sum(a)
y = 1 / (4 * m)

z = [i for i in a if i >= x * y]
if len(z) >= m:
    print('Yes')
else:
    print('No')
