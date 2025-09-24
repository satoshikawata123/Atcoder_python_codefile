s = input()

n = len(s)
s1 = s[:int((n-1)/2)]
s2 = s[int((n+1)/2):]
print('Yes' if (s==s[::-1] and s1==s1[::-1] and s2==s2[::-1]) else 'No')
