import sys

it = iter(map(int, sys.stdin.read().split()))
N = next(it); Q = next(it)
A = [next(it) for _ in range(N)]
pref = [0]
for x in A:
    pref.append(pref[-1] + x)
total = pref[-1]

s = 0

out = []
for _ in range(Q):
    t = next(it)
    if t == 1:
        c = next(it)
        s = (s + c) % N
    else:
        l = next(it)
        r = next(it)
        length = r - l + 1
        start0 = (s + (l - 1)) % N
        end0   = (start0 + length - 1) % N

        if start0 <= end0:
            res = pref[end0 + 1] - pref[start0]
        else:
            res = (total - pref[start0]) + (pref[end0 + 1] - pref[0])
        out.append(str(res))

print("\n".join(out))
