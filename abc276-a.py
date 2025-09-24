n = input()
ans = -1

for i in range(len(n)):
    if n[i] == "a":
        ans = i + 1

print(ans)
