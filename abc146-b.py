N = int(input())
S = input()

for i in S:
  print(chr(65 + (ord(i) - 65 + N) % 26), end="")
