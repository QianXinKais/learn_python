# 列表基本操作
l1 = [1, 2, 3, 4, 5, 6]
l2 = [4, 23, 66, 2, 8, 32, 11]
l3 = [4, 23, 66, 2, "h", 12.3]

# # 1.1 按照索引存取值,正向取
# print(l1[2])
# l1[2] = 99
# print(l1)

# # 1.2 反向取值
# print(l1[-1])
# l1[-1] = 99
# print(l1)

# # 2. 切片,前闭后开
# print(l1[0:4])
# print(l1[0:4:2])

# print(l1[-3:-1])
# print(l1[:-2])
# print(l1[-3:])
# print(l1[::-2]) 最后一个参数控制为正数，正着输出，为负数，倒着输出，数字为步长

# # 3. 长度len
# print(len(l1))

# # 4. 通过成员运算符判断元素是否在列表中
# print(1 in l1)
# print(99 in l1)

# # 5.1 append 向列表尾部追加元素,将整个对象作为单个元素添加到列表末尾。
# l1.append("l")
# print(l1)

# # 5.2 extend 一次性在列表尾部添加多个元素.将可迭代对象中的每个元素添加到列表末尾。
# l1.extend(('h', 'e', 'l', 'l', 'o'))
# print(l1)
# # append和extend的区别： append 添加的是一个元素。extend 添加的是多个元素。

# # 5.3 insert 在指定位置插入元素
# l1.insert(0, "kaitou")
# print(l1)

# # 6.1 del删除
# del l1[4]
# print(l1)


# # 6.2 pop() 默认删除列表的最后一个元素，并将删除的值返回。可以通过用索引值作为参数，指定删除元素
# l1.pop()
# print(l1)
# print(l1.pop(2))
# print(l1)

# # 6.3 remove()  指定删除某个元素，没有返回值
# print(l1.remove(4))
# print(l1)

# # 7. reverse() 颠倒列表内的元素顺序
# print(l1.reverse())
# print(l1)

# 8.1 sort() 排序。默认从小到大排序。可以用reverse来反转
# l2.sort()
# print(l2)
# print(l3.sort())  #排序时，列表元素必须是相同的数据类型，否则会报错。
print(l2.sort(reverse=True))
print(l2)
print(l2.sort(reverse=False))
print(l2)

# 8.2 列表可以直接进行比较大小。
print(l1 > l2)
# 字符之间的大小取决于ASCII表的先后顺序，如果1个字符串由多位字符组成，则挨个比较，比较出结果则马上输出结果
l4 = ['A', 'z', 'hello', 'he']
print(l4.sort())
print(l4)

# 9. 循环
for line in l2:
    print(line)
