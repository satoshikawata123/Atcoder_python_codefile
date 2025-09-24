N, K = [int(x) for x in input().split()]
H = [int(x) for x in input().split()]

print(len([x for x in H if x >= K]))
