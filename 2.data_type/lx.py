# # 写代码,有如下变量,请按照要求实现每个功能 （共6分，每小题各0.5分）
# name = " aleX"
# # 1)    移除 name 变量对应的值两边的空格,并输出处理结果
# print(name.strip(" "))
# # 2)    判断 name 变量对应的值是否以 "al" 开头,并输出结果
# print(name.startswith('al'))
# # 3)    判断 name 变量对应的值是否以 "X" 结尾,并输出结果
# print(name.endswith('X'))
# 4)    将 name 变量对应的值中的 “l” 替换为 “p”,并输出结果
# print(name.replace('l', 'p'))
# # 5)    将 name 变量对应的值根据 “l” 分割,并输出结果。
# print(name.split('l'))
# # 6)    将 name 变量对应的值变大写,并输出结果
# print(name.upper())
# # 7)    将 name 变量对应的值变小写,并输出结果
# print(name.lower())
# 8)    请输出 name 变量对应的值的第 2 个字符?
# print(name[1])
# # 9)    请输出 name 变量对应的值的前 3 个字符?
# print(name[:3])
# 10)    请输出 name 变量对应的值的后 2 个字符?
# print(name[-2:])
# # 11)    请输出 name 变量对应的值中 “e” 所在
# print(name.index('e'))
# # 12)    获取子序列,去掉最后一个字符。如: oldboy 则获取 oldbo。
# print(name[:-1])


# 1. 有列表data=['alex',49,[1900,3,18]]，分别取出列表中的名字，年龄，出生的年，月，日赋值给不同的变量
data = ['alex', 49, [1900, 3, 18]]
name = data[0]
age = data[1]
year = data[2][0]
month = data[2][1]
day = data[2][2]

print(name, age, year, month, day)

# 2. 用列表模拟队列
mndl = []
for i in range(5):
    mndl.append(i)
print(mndl)
for i in mndl:
    print(i)

# 3. 用列表模拟堆栈
mndz = []
for i in range(5):
    mndz.append(i)
print(mndz)
for i in range(len(mndz)):
    print(mndz[-i-1])

# 4. 有如下列表，请按照年龄排序（涉及到匿名函数）
l = [
    {'name': 'alex', 'age': 84},
    {'name': 'oldboy', 'age': 73},
    {'name': 'egon', 'age': 18},
]
l.sort(key=lambda item: item['age'])
print(l)
