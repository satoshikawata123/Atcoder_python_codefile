S=input()
list=""
for i in range(len(S)):
  if S[i].isupper():
    list+=S[i]
print(list)
