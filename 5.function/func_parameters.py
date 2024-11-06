# # 1.位置参数。按照从左到右的顺序依次定义的参数
# # 位置形参：调用时必须被传值，多一个少一个都不行。
# # 位置实参：

# def foo(x, y):
#     print(x, y)


# foo(1, 2)

# # 关键字参数： 在函数调用时，按照key = value的形式定义的实参。
# # 特点：指名道姓地给形参传值，不再依赖于位置。
# # 注意：1.关键字实参必须子啊位置实参的后面；2.不能为同一个参数赋值多次。


# def foo(x, y):
#     print(x, y)


# foo(x=1, y=2)

# # 默认参数：在函数定义阶段，就已经为形参赋值了。
# # 特点：定义阶段已经有值，意味着调用的时候可以不用传值。
# # 位置参数通常用于经常变化的参数，默认参数用于不经常变化的参数。


# def foo(x, y=1):
#     print(x, y)


# foo(2)

# res = 1


# def foo(x, y=res):
#     print(x, y)


# res = 10
# foo(1)

# 可变长参数：在调用函数时，实参值的个数不固定
# # 实参的形式有：位置参数和关键字实参。
# # 针对实参有以上两种传值方式，形参有两种解决方案：* ，**
# # 比如我想调用一个函数，参数需要写入foo(1,2,3,4,5,6，……),此时函数定义可写为以下这种方式：
# def foo(x, y, *z):  # *在形参中代表只接收按照位置定义的超出的参数
#     print(x)
#     print(y)
#     print(z)


# foo(1, 2, 3, 4, 5, 6)  # 此时x=1,y=2,*将剩下的值以元组的形式保存给变量z。即z=(3,4,5,6)
# foo(1, 2, *[3, 4, 5, 6])  # *在实参中代表的是位置参数。所以这种传值方式等同于foo(1, 2, 3, 4, 5, 6)

# **kwargs
# def foo(x, y, **kwargs):  # ** 在形参中代表,接收的是超出长度的关键字参数。
#     print(x, y)
#     print(kwargs)


# foo(y=2, x=1, z=3, k=4, t=5)  # x=1，y=2,kwargs ={"z":3,"k":4,"t":5}


# def foo(name, age):
#     print(name, age)


# foo(**{"name": "kais", "age": 18})  # ** 在实参中代表，传入的是关键字参数

# def wrapper(*args, **kwargs):  # 这种定义定义函数的参数，可以传任意长度任意类型的参数
#     print(args, kwargs)

# def foo(x, y, z):
#     print(x, y, z)


# def wrapper(*args, **kwargs):
#     foo(*args, **kwargs)


# # 这里需要注意，虽然wrapper函数可以传入任意长度任意类型的参数，但是因为wrapper调用了foo函数，所以调用wrapper的时候，必须遵循foo的参数传入原则，否则会报错
# wrapper(1, 2, 3)
# 练习题
# 1、写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成批了修改操作
def modify(filename, content):
    pass


modify()
# 2、写函数，计算传入字符串中【数字】、【字母】、【空格] 以及 【其他】的个数


def calc_num(str1):
    pass


calc_num

# 3、写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。


def len_greater_five(container):
    pass


len_greater_five
# 4、写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。


def twins_list(l1):
    pass


twins_list()
# 5、写函数，检查获取传入列表或元组对象的所有奇数位索引对应的元素，并将其作为新列表返回给调用者。


def odd_num(container):
    pass


odd_num()
# 6、写函数，检查字典的每一个value的长度, 如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
# dic = {"k1": "v1v1", "k2": [11, 22, 33, 44]}
# PS: 字典中的value只能是字符串或列表


def dic_len(dic):
    pass
