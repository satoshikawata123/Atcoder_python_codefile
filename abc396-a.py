n = int(input())
a = list(map(int, input().split()))

if n < 3:
    print("No")
else:
    for i in range(n - 2):
        if a[i] == a[i + 1] == a[i + 2]:
            print("Yes")
            break
    else:
        print("No")
