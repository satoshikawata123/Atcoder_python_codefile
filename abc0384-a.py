N, c1, c2 = input().split()
N = int(N)
S = input()

result = ''.join([char if char == c1 else c2 for char in S])

print(result)
