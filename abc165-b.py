n = int(input())
x = 100
cnt = 0

while x < n:
  x += x//100
  cnt += 1
print(cnt)
