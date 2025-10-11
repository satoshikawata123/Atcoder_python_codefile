import sys

it = iter(sys.stdin.read().strip().split())
T = int(next(it))
ans = []
for _ in range(T):
    N = int(next(it)); M = int(next(it)); K = int(next(it))
    S = list(next(it).strip())
    out = [[] for _ in range(N)]
    for _m in range(M):
        u = int(next(it)) - 1
        v = int(next(it)) - 1
        out[u].append(v)

    cur = [c == 'A' for c in S]
    for _ in range(K):
        all_good = [False]*N
        for v in range(N):
            ok = True
            for w in out[v]:
                if not cur[w]:
                    ok = False
                    break
            if ok:
                all_good[v] = True
        nxt = [False]*N
        for u in range(N):
            for v in out[u]:
                if all_good[v]:
                    nxt[u] = True
                    break
        cur = nxt

    ans.append("Alice" if cur[0] else "Bob")

print("\n".join(ans))
