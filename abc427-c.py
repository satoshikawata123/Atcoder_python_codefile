import sys

data = sys.stdin.read().strip().split()
it = iter(data)
N = int(next(it)); M = int(next(it))
edges = [(int(next(it))-1, int(next(it))-1) for _ in range(M)]

best = 0
for mask in range(1 << (N - 1)):
    def color(v):
        return 0 if v == 0 else (mask >> (v - 1)) & 1
    cut = 0
    for u, v in edges:
        if color(u) ^ color(v):
            cut += 1
    if cut > best:
        best = cut

print(M - best)
