s = input()
a = []

for i in s:
  if i == "0":
    a.append(0)
  elif i == "1":
    a.append(1)
  elif i == "B":
    if a != []:
      a.pop()

print(*a, sep="")
