from collections import Counter
s = input().strip()
for k, v in Counter(s).items():
    if v == 1:
        print(k)
        break
