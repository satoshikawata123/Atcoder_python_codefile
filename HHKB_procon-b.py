h,w=map(int,input().split())
s=[input() for _ in range(h)]
cnt=0

for i in range(h):
    for j in range(w):
        if s[i][j] == ".":
            if i+1<h and s[i+1][j]==".":
                cnt += 1
            if j+1<w and s[i][j+1]==".":
                cnt += 1
print(cnt)
