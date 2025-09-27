N = int(input())
ans = sum(((-1) ** i) * (i ** 3) for i in range(1, N + 1))
print(ans)
