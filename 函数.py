def fn():
    print('第一个函数定义')
    return 1

res = fn()
print(res)
print(fn)

def fn2(a,b,c):
    return a + b + c

print(fn2(fn(),2,3))