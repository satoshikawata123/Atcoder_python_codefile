def add(value1, value2):
    # 戻り値としてvalue1 + value2を返す
    return value1 + value2

def lam(event, context):
    result = add(10, 20)
    print(result)

print("hello")
lam(1,1)
