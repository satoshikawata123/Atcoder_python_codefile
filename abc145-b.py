n = int(input())
s = input()

if n % 2 == 0:
    if s[0:len(s)//2] == s[len(s)//2:]:
        print("Yes")
        exit()

print("No")
