# 入力を受け取る
H, W, X, Y = map(int, input().split())  # H: 行数, W: 列数, X: 初期位置の行, Y: 初期位置の列
X, Y = X - 1, Y - 1  # 0-based index に変更
grid = [input().strip() for _ in range(H)]  # マス目を読み込む
T = input().strip()  # サンタクロースの行動指示

# 訪れた家の位置を記録するための集合
visited_houses = set()

# 初期位置が家なら、訪れた家として記録
if grid[X][Y] == '@':
    visited_houses.add((X, Y))

# サンタクロースの移動処理
for move in T:
    if move == 'U':  # 上に移動
        if X > 0 and grid[X - 1][Y] != '#':  # 通行可能な場合
            X -= 1
    elif move == 'D':  # 下に移動
        if X < H - 1 and grid[X + 1][Y] != '#':  # 通行可能な場合
            X += 1
    elif move == 'L':  # 左に移動
        if Y > 0 and grid[X][Y - 1] != '#':  # 通行可能な場合
            Y -= 1
    elif move == 'R':  # 右に移動
        if Y < W - 1 and grid[X][Y + 1] != '#':  # 通行可能な場合
            Y += 1

    # 移動後のマスが家（@）なら、訪れた家として記録
    if grid[X][Y] == '@':
        visited_houses.add((X, Y))

# 最後にサンタクロースがいるマスと、訪れた家の数を出力
print(X + 1, Y + 1, len(visited_houses))  # 1-based indexに戻して出力
