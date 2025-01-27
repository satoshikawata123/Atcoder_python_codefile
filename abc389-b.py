X = int(input())
x =1

for i in range(1,X+1):
    x = x * i
    if x == X:
        print(i)
        exit()
