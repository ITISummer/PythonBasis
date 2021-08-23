var1 = 'Hello World!'
var2 = "Runoob"

print ("var1[0]: ", var1[0])
print ("var2[1:5]: ", var2[1:5])

# --------------- 字符串运算符
a = "Hello"
b = "Python"
print("a + b 输出结果：", a + b)
print("a * 2 输出结果：", a * 2)
print("a[1] 输出结果：", a[1])
print("a[1:4] 输出结果：", a[1:4])
if( "H" in a) :
    print("H 在变量 a 中")
else :
    print("H 不在变量 a 中")
if( "M" not in a) :
    print("M 不在变量 a 中")
else :
    print("M 在变量 a 中")
print (r'\n')
print (R'\n')

# --------------- 字符串格式化
'''
Python 支持格式化字符串的输出 。尽管这样可能会用到非常复杂的表达式，
但最基本的用法是将一个值插入到一个有字符串格式符 %s 的字符串中。
在 Python 中，字符串格式化使用与 C 中 sprintf 函数一样的语法。
'''
print ("我叫 %s 今年 %d 岁!" % ('小明', 10))

# --------------- 字符串格式化



