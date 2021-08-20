# 打印 9*9 乘法表
i = 1
tier = 9
while i <= tier:
    j = 1
    while j <= i:
        # print(j,'*',i,'=',i*j,'  ',end='')
        print(f"{j}*{i}={j*i}  ",end='')
        j += 1
    print()
    i += 1
