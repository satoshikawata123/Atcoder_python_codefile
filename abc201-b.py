N = int(input())
mountains = []
for _ in range(N):
    S, T = input().split()
    T = int(T)
    mountains.append([T, S])

mountains.sort(reverse=True)

print(mountains[1][1])
