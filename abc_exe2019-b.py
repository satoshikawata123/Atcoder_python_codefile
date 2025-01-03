N = int(input())
s = input()
count = 0

for i in range(N):
	if s[i] == 'R':
		count += 1
if count > N-count:
	print('Yes')
else:
	print('No')
