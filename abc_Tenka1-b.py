N = int(input())
S = input()
K = S[int(input()) - 1]

for s in S:
    if s != K:
        print("*", end="")
    else:
        print(s, end="")
print()
