S = input()

if all(S[i]  in "RUD" for i in range(0, len(S), 2)):
    if all(S[i]  in "LUD" for i in range(1, len(S), 2)):
        print("Yes")
        exit()

print("No")
