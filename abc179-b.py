N = int(input())
cnt = 0
for i in range(N):
    d,e = input().split()
    if d==e:
        cnt+=1
    else:
        cnt = 0
    if cnt > 2:
        print('Yes')
        break
else:
    print('No')
