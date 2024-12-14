from itertools import combinations

a, b, c, d, e = map(int, input().split())

scores = {'A': a, 'B': b, 'C': c, 'D': d, 'E': e}

participants = []

problems = "ABCDE"
for length in range(1, len(problems) + 1):
    for combination in combinations(problems, length):
        name = ''.join(combination)
        score = sum(scores[char] for char in combination)
        participants.append((score, name))

participants.sort(key=lambda x: (-x[0], x[1]))

for _, name in participants:
    print(name)
