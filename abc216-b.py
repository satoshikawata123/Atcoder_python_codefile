n = int(input())
s = set()

for i in range(n):
    a = tuple(input().split())
    s.add(a)
if len(s) < n:
    print("Yes")
else:
    print("No")
