s = list(input())
t = list(input())

if s == t:
  print("Yes")
  exit()

x = len(s)
for i in range(x-1):
  s[i],s[i+1] = s[i+1],s[i]
  if s == t:
    print("Yes")
    break
  else:
    s[i+1],s[i] = s[i],s[i+1]
else:
  print("No")
