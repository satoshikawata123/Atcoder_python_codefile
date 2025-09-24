s = input()
lst = list(s)

while len(lst) > 0 and lst[-1] == '0':
    lst.pop()

if lst == lst[:: -1]:
    print("Yes")

else:
    print("No")
