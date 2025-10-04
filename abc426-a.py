X, Y = input().split()
order = ["Ocelot", "Serval", "Lynx"]
rank = {v: i for i, v in enumerate(order)}
print("Yes" if rank[X] >= rank[Y] else "No")
