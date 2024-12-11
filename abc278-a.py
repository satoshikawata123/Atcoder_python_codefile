n, k = map(int, input().split())
a = list(map(int, input().split()))

for i in range(k, n):
    print(a[i], end=' ')

for i in range(min(k, n)):
    print(0, end=' ')
