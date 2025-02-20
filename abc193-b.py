n = int(input())
st = set()

for i in range(n):
  a, p, x = map(int, input().split())
  if a < x:
    st.add(p)

print(-1 if len(st) ==  0 else min(st))
