# 质数是只能被 1 和自身整除的数
prime = int(input())
i = 2
while prime <= 2:
    print('输入数据不合法，请重新输入...')
    prime = int(input())
while i <= prime ** 0.5:
    flag = True
    if prime % i == 0:
        flag = False
        break
    else:
        i += 1
if flag:
    print(prime,"是质数")
else:
    print(prime,'不是质数')