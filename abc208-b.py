P = int(input())
A = [1]

for i in range(9):
    A.append(A[i]*(i+2))
ans = 0
rest = P
for i in range(10):
    ans = ans + rest//A[9-i]
    rest = rest%A[9-i]
print(ans)
