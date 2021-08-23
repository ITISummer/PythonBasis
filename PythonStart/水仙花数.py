# 求 1000 (n>=3)以内的水仙花数（每个位上的数字的 n 此幂之和等于该数本身）
num = 100
n = 3
while num < 1000:
    temp = num
    sum = 0
    while temp > 0:
        x = temp % 10
        sum += x ** n
        temp //= 10
    if sum == num:
        print(num)
    num += 1