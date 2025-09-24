H, W = map(int, input().split())
count = 0

for _ in range(H):
    row = input()
    count += row.count('#')

print(count)
