t1 = (1, "hello", 13.14, 2, 90)
# 1. 按照索引取值
print(t1[2])
print(t1[-2])

# 2. 切片
print(t1[0:2])
print(t1[0:3:2])
print(t1[::2])

print(t1[-1:])
print(t1[-3:-1:2])
print(t1[:-1])

print(t1[1::-2])
print(t1[-1::-2])

# 3. 长度
print(len(t1))

# 4. 成员运算符
print(2 in t1)
print(2 not in t1)

# 5. 循环
for i in t1:
    print(i)
