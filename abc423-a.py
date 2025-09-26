S = input().strip()
a = int(S[0])
b = int(S[2])
c = S[1]
if b== 8:
    a += 1
    b = 1
else:
    b+= 1
e = str(a)
g = str(b)
ans =[e,c,g]
A = "".join(ans)
print(A)
