N, R = map(int, input().split())
contests = [list(map(int, input().split())) for _ in range(N)]

for D, A in contests:
    if (D == 1 and 1600 <= R <= 2799) or (D == 2 and 1200 <= R <= 2399):
        R += A

print(R)
