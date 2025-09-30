N, L, R = map(int, input().split())
S = input()

if all(c == "o" for c in S[L-1:R]):
    print("Yes")
else:
    print("No")
