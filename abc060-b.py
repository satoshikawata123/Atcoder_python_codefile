A, B, C = map(int,input().split())

for k in range(500):
    for m in range(500):
        if A * k == m * B + C:
            print("YES")
            exit()

print("NO")
