S=input()
count_s=0
count_e=0
count_n=0
count_w=0

for i in S:
  if i == "S":
    count_s+=1
  elif i == "E":
    count_e+=1
  elif i == "N":
    count_n+=1
  else:
    count_w+=1
if (count_w>0 and count_e>0 and count_n^count_s==0) or (count_n>0 and count_s>0 and count_w^count_e==0):
  print("Yes")
else:
  print("No")
