N = int(input())
D = list(map(int,input().split()))

for i in range(N-1):
    rui = 0
    d = []
    for j in range(i,N-1):
        rui += D[j]
        d.append(rui)
    print(*d)
