# 1.简述编译型与解释型语言的区别，且分别列出你知道的哪些语言属于编译型，哪些属于解释型
# 2.执行 Python 脚本的两种方式是什么
# 3.Pyhton 单行注释和多行注释分别用什么?
# 4.布尔值分别有什么?
# 5.声明变量注意事项有那些?
# 6.如何查看变量在内存中的地址?
# x = 12
# print(id(x))
# 7.写代码
#   1.实现用户输入用户名和密码, 当用户名为 seven 且 密码为 123 时, 显示登陆成功, 否则登陆失败!
# name = input()
# password = input()
# if name == 'seven' and password == '123':
#     print('登陆成功！')
# else:
#     print('登陆失败！')

# #   2.实现用户输入用户名和密码, 当用户名为 seven 且 密码为 123 时, 显示登陆成功, 否则登陆失败, 失败时允许重复输入三次
# tag = 3
# while tag > 0:
#     name = input()
#     password = input()
#     if name == 'seven' and password == '123':
#         print('登陆成功！')
#         break
#     else:
#         print('登陆失败！')
#         tag -= 1

#   3.实现用户输入用户名和密码, 当用户名为 seven 或 alex 且 密码为 123 时, 显示登陆成功, 否则登陆失败, 失败时允许重复输入三次
# tag = 3
# while tag > 0:
#     name = input()
#     password = input()
#     if (name == 'seven' or name == 'alex') and password == '123':
#         print('登陆成功！')
#         break
#     else:
#         print('登陆失败！')
#         tag -= 1

# 8.写代码
#   a. 使用while循环实现输出2-3+4-5+6...+100 的和
# tag = 2
# total = 0
# while tag <= 100:
#     if tag % 2 == 0:
#         total += tag
#     else:
#         total -= tag
#     tag += 1
# print(total)

#   b. 使用 while 循环实现输出 1, 2, 3, 4, 5, 7, 8, 9, 11, 12 使用 while 循环实现输出 1-100 内的所有奇数
# number = 1
# while number <= 100:
#     if number % 2 != 0:
#         print(number)
#     number += 1

#   e. 使用 while 循环实现输出 1-100 内的所有偶数
# number = 1
# while number <= 100:
#     if number % 2 == 0:
#         print(number)
#     number += 1

# 9.现有如下两个变量, 请简述 n1 和 n2 是什么关系?

# 2 作业：编写登陆接口
# 基础需求：
# 让用户输入用户名密码
# 认证成功后显示欢迎信息
# 输错三次后退出程序
# def login():
#     for _ in range(3):
#         name = input()
#         password = input()
#         if name == 'seven' and password == '123':
#             return print("欢迎登录！")
#         else:
#             print('登录失败！')


# login()


# 升级需求：
# 可以支持多个用户登录(提示，通过列表存多个账户信息)
# 用户3次认证失败后，退出程序，再次启动程序尝试登录时，还是锁定状态（提示: 需把用户锁定的状态存到文件里）
dic = {
    'zhaosi': {'password': '123', 'count': 0},
    'wangwu': {'password': '123', 'count': 0},
    'liu':  {'password': '123', 'count': 0}
}

count = 0
while True:
    name = input("u>>>>:")
    if name not in dic:
        print("用户不存在")
        continue

    with open('db.txt', 'r') as f:
        lock_users = f.read().split('|')
        if name in lock_users:
            print(f"用户{name}已经被锁定")
            break

    if dic[name]['count'] > 2:
        print("尝试次数过多，锁定")
        with open('db.txt', 'a') as f:
            f.write(f'{name}|')
        break

    password = input('p>>>:')

    if password == dic[name]['password']:
        print('登录成功！')
        break
    else:
        print('用户名或者密码错误！！！')
        dic[name]['count'] += 1
