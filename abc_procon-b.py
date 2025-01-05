S = input()
cnt = 0

for i in range(len(S)):
  cnt += S[i] == "o"

print('YES' if (15 - len(S)) + cnt >= 8 else 'NO')
