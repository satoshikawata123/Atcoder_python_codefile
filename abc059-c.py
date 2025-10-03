n = int(input())
a = list(map(int, input().split()))
stn = 10**9

for i in range(-100, 101):
    cnt = 0
    for j in range(n):
        cnt += (i-a[j])**2
    stn = min(cnt, mv)

print(stn)
