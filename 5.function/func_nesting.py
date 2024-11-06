# 1.函数的嵌套调用
def my_max(x, y):
    if x >= y:
        return x
    else:
        return y


def my_max4(a, b, c, d):
    res1 = my_max(a, b)
    res2 = my_max(c, d)
    res3 = my_max(res1, res2)
    return res3

# 2.函数的嵌套定义


def f1():
    def f2():
        pass
    print(f2)
