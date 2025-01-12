A = []
for _ in range(3):
    A.append(list(map(int, input().split())))

X = [[0 for _ in range(3)] for _ in range(3)]
Y = [[0 for _ in range(3)] for _ in range(3)]


N = int(input())
for i in range(N):
    b = int(input())
    for i in range(3):
        for j in range(3):
            if A[i][j] == b:
                X[i][j] = 1
                Y[j][i] = 1

ans = "No"
if sum(X[0]) == 3 or sum(X[1]) == 3 or sum(X[2]) == 3:
    ans = "Yes"
elif sum(Y[0]) == 3 or sum(Y[1]) == 3 or sum(Y[2]) == 3:
    ans = "Yes"
elif X[0][0] + X[1][1] + X[2][2] == 3:
    ans = "Yes"
elif X[2][0] + X[1][1] + X[0][2] == 3:
    ans = "Yes"

print(ans)
