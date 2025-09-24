N = int(input())
c1, c2 = input().split()
S = input()

# 文字列の置き換え処理
result = ""
for char in S:
    if char == c1:
        result += char  # c1 の場合、そのまま残す
    else:
        result += c2  # それ以外は c2 に置き換える

# 結果を出力
print(result)
