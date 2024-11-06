"""
关于字符串:str常用的一些方法
"""
str1 = 'hello world!'
# 1.按照索引取值
# 1.1 正向取值
print(str1[6])

# 1.2 反向取
print(str1[-4])

# 1.3 对于str来说，只能按照索引取值，不能改
# str1[0] = 'H'
# print(str1)  # TypeError: 'str' object does not support item assignment

# 2. 切片
# 2.1 前闭后开
print(str1[0:8])
print(str1[-1:-9:-1])

# 2.2 步长：上述例子（str1[-1:-9:-1]）的第三个参数（-1）,默认为1。
print(str1[0:8:2])

# 3. len 长度：通过len函数获取字符串的长度，注意，空格也算字符
print(len(str1))

# 4. 通过成员运算符判断某字符是否在字符串中
print('h' in str1)
print('hll' in str1)
print('hll' not in str1)

# 5. strip:移除字符串首尾指定的字符
str2 = '     hello world!     '
print(str2.strip())

str3 = '******hello world!******'
print(str3.strip('*'))

# 6. split: 用于将字符串分割成列表。括号内不指定字符,默认以空格作为分隔符号
str1 = 'hello world!'
print(str1.split())

str1 = 'h*e*l*l*o'
print(str1.split('*'))

# 7. 字符串进行循环
str1 = 'hello!'
for line in str1:
    print(line)

"""
常用方法记录
"""
str1 = '****hello****'
str2 = 'hello tom'
# 1.1 strip 移除左右两边的指定字符
print(str1.strip('*'))

# 1.2 lstrip    移除左边的指定字符
print(str1.lstrip('*'))

# 1.3 rstrip    移除右边的指定字符
print(str1.rstrip('*'))

# 2.1 lower     将英文字符串全部变为小写
str1 = "Hello World!"
print(str1.lower())

# 2.2 upper     将英文字符全部变为大写
print(str1.upper())

# 3.1 startswith    判断字符串是否以括号内指定的字符开头
print("************startswitch************")
print(str2.startswith('t'))
print(str2.startswith('h'))
print(str2.startswith('hel'))

# 3.2endswith       判断字符串是否以括号内指定的字符结尾
print("************endswith************")
print(str2.endswith('o'))
print(str2.endswith('m'))
print(str2.endswith('tom'))

# 4.1 split 将字符串按指定的分隔符拆分成列表。从左到右切分
str4 = "D:\A\Downloads\AliDownloads"
print(str4.split('\\'))
print(str4.split('\\', 2))  # 切割2次

# 4.2 rsplit 从右往左切分，可以指定切分次数
print(str4.rsplit('\\'))
print(str4.rsplit('\\', 1))

# 5. join 从可迭代对象中取出多个字符串，然后按照指定的分隔符进行拼接，拼接的结果为字符串
w_list = ["my", "name", "is", "Tom"]
print(" ".join(w_list))
print("|".join("Python"))


# 6. replace 将字符串中的指定子字符串替换为新的子字符串。
s1 = "My name is Tom,I am 18 years old!"
print(s1.replace('18', "25"))
s1 = s1.replace("I am", "My")
print(s1)
# 把My 改为You
print(s1.replace('My', 'You', 1))

# 7. isdigit 判断字符串是否纯数字组成，返回结果为True或者False
s2 = "843535"
print(s2.isdigit())
s3 = "962541s"
print(s3.isdigit())

# 8. find 用于查找子字符串在字符串中的位置。从指定范围内查找字符串的起始索引，找得到则返回起始索引值，找不到则返回-1
s4 = "My name is Tom,I am 18 years old!"
print(s4.find("Tom"))
print(s4.find('n', 2, 4))
print(s4.find('n', 5, 8))
print(s4.rfind("is"))  # 查找子字符串在字符串中最后一次出现的位置。

# 9. index用于查找子字符串在字符串中的第一次出现位置。与 find() 类似，但如果未找到子字符串，它会抛出 ValueError 异常。
print(s4.index("am"))
print(s4.rindex("18"))

# 10. count 用于计算子字符串在字符串中出现的次数。
print(s4.count('m'))

# 11. center 将字符串居中，两侧填充指定字符（默认为空格）。
name1 = 'Andy'
print(name1.center(10, '*'))

# 12.1 ljust 将字符串左对齐，右侧填充指定字符（默认为空格）。
print(name1.ljust(10, "*"))

# 12.2 将字符串右对齐，左侧填充指定字符（默认为空格）。
print(name1.rjust(10, "*"))

# 13. zfill 在字符串左侧填充零，常用于格式化数字字符串。
print(name1.zfill(25))

# 14. captalize: 首字母大写
print("hello".capitalize())

# 15. swapcase 大小写翻转
print("Python".swapcase())

# 16. 每个单词的首字母大写
print("hello,world!my name is bob!".title())

# 17. is……数字系列
n1 = b'5'  # byte
n2 = u'5'  # 5,unicode
n3 = '五'  # 中文数字5
n4 = 'Ⅴ'  # 罗马数字5
print(n1.isdigit())  # isdigit：认为byte和unicode为数字
print(n2.isdigit())
print(n3.isdigit())
print(n4.isdigit())

# print(n1.isdecimal()) byte无isdecimal方法
print(n2.isdecimal())
print(n3.isdecimal())
print(n4.isdecimal())

# print(n1.isnumeric)  # byte无isnumeric方法
print(n2.isnumeric)
print(n3.isnumeric)
print(n4.isnumeric)

strmes = "Tom18"
print(strmes.isalnum())  # 字符串中既可以包含数字也可以包含字母


"""
字符串格式化输出的方式有三种
"""
# 1. 使用%
# print("my name is %s,I am %d years old!" % ('tom', 16))

# # 2. 使用.format()方法
# print("my name is {},I am {} years old".format('tom', 17))
# print("my name is {name},I am {age} years old".format(name='tom', age=17))
# print("my name is {name},I am {age} years old".format(age=17, name='tom'))

# # 3. 使用f-字符串的方式
# name = 'Tom'
# age = 18
# print(f"my name is {name},I am {age} years old")
# print(f"my name is {"Bob"}, I am {18} years old")
