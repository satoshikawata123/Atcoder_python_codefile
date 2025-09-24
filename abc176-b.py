N = input()
T = 0

for a in range(len(N)):
    T += int(N[a])
if T % 9 == 0:
    print("Yes")
else:
    print("No")
