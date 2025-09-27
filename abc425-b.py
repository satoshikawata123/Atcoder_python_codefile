import sys

data = list(map(int, sys.stdin.read().split()))
N = data[0]
A = data[1:1+N]

used = set()
for x in A:
    if x != -1:
        if x in used:
            print("No")
            sys.exit()
        used.add(x)
remaining = [x for x in range(1, N+1) if x not in used]
it = iter(remaining)
P = []
for x in A:
    if x == -1:
        P.append(next(it))
    else:
        P.append(x)

print("Yes")
print(*P)
