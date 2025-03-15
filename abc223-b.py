S = input()
tmax, tmin = S, S

for i in range(len(S)):
    t = S[i:] + S[:i]
    tmax = max(t, tmax)
    tmin = min(t, tmin)
print(tmin, tmax, sep='\n')
