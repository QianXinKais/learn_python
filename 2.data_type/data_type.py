"""
数值类型
    整型 int
    浮点型 float
    复数 complex
"""
a = 4
print(type(a))
b = 4.12
print(type(b))
c = 4+3j
print(type(c))

"""
文本类型
    字符串 str
"""
zfc = "hello wolrd!"
print(type(zfc))

"""
序列类型
    列表 list
    元组 tuple
    范围 range
"""
lb = [1, 2, 3]
print(type(lb))
yz = ("y", "组", "1")
print(type(yz))
numbers = range(1, 10)
print(type(numbers))

"""
映射类型
    字典 dict
"""
zd = {"name": "张三", "sex": "男", "age": 18}
print(type(zd))

"""
集合类型
    集合 set
    冻结集合 frozenset
"""
jh = {1, 2, 3, 4, 5, 6}
print(type(jh))
djjh = frozenset({1, 2, 4})
print(type(djjh))


"""
布尔类型
    布尔 bool
"""
br = True
print(type(br))

"""
二进制类型
    字节 bytes
    字节数组 bytearray
    内存视图 memoryview
"""
zj = b"hello"
print(type(zj))

zjsz = bytearray(b'sad')
print(type(zjsz))

ncst = memoryview(zj)
print(type(ncst))

"""
空类型
    NoneType:表示空值或无值
"""
value = None
print(type(value))
