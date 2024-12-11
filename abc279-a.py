S = input()
ans = 0

for i in range(len(S)):
    if S[i] == "v":
        ans = ans + 1
    else:
        ans = ans + 2

print(ans)
