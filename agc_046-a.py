N=int(input())
i=1
K=0

while K==0:
  if i*360%N==0:
    print(i*360//N)
    K=1
  else:
    i+=1
