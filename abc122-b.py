ACGT = ("A","C","G","T")
temp_ans = 0
ans = 0

S= list(input())
for s in S:
    if s in ACGT:
        temp_ans += 1
        ans = max(ans,temp_ans)
    else:
        temp_ans = 0

print(ans)
