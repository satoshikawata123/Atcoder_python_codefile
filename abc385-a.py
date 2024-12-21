A,B,C = map(int, input().split())

if A + B == C or A + C == B or B + C == A or (A==B and B==C):
    print("Yes")
else:
    print("No")
