# 创建一个函数 power 来为任意数字做幂运算 n ** i
def power(n, i):
    """
    计算一个数的 i 次幂
    :param n:  底数
    :param i: 幂
    :return:
    """
    if i == 1:
        return n
    else:
        return n * power(n, i - 1)


print(power(3, 2))


def hui_wen(s):
    """
    检查一个字符串是否是回文字符串
    :param s: 待检查的字符串
    :return: True - 是回文；False - 不是回文
    """
    if len(s) < 2:
        # 字符串长度小于 2，则一定是回文
        return True
    elif s[0] != s[-1]:
        # 字符串第一个和最后一个不相等，则不是回文
        return False
        # 开始递归检查剩余的内容是否相等 - 利用字符串切片
    return hui_wen(s[1:-1])

print(hui_wen('lvlv'))
print(hui_wen('abcddcba'))
