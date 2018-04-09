def compute_gcd(a, b):
    if a < b:
        a, b = b, a
        while b:
            a, b = b, a % b

    return a


a = int(input("輸入第一個數字: "))
b = int(input("輸入第二個數字: "))
print(a, '和', b, '的最大公因數是', compute_gcd(a, b))