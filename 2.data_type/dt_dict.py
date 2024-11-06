dt = {
    "name": "Tom",
    "age": 18,
    "sex": "male",
    "ah": ['game', 'football']
}
# # 1.1 取操作,通过键取值
# print(dt["name"])

# # 1.2 存操作,若该键不存在，则新增；若存在，则修改value值
# dt['score'] = 100
# print(dt)
# dt['sex'] = "female"
# print(dt)

# # 2. 长度len
# print(len(dt))

# # 3. 通过成员运算符 in , not in
# print('name' in dt)
# print(18 in dt)

# # 4. pop 删除,通过指定字典的key来删除字典的键值对
# dt.pop('sex')
# print(dt)

# # 5. 键keys,值 values, 键值对items
# print(dt.keys())
# print(dt.values())
# print(dt.items())

# # 6.1 默认循环遍历字典的key
# for key in dt:
#     print(key)

# # 6.2 只遍历key
# for key in dt.keys():
#     print(key)

# 6.3 只遍历value
# for value in dt.values():
#     print(value)

# # 6.4 同时遍历key和value
# for key in dt.items():
#     print(key)

"""
关于字典的常用方法
"""
# # 1. get 取值。通过key，取值
# print(dt.get('name'))

# # 2. pop 删除。通过指定key删除对应的键值对,并返回删除的值
# print(dt.pop('sex'))
# print(dt)

# # 3. popitem() 随机删除一组键值对，并将删除的键值对放到元组中返回，
# print(dt.popitem())
# print(dt)

# # 4. update 更新。用新字典更新旧字典，有则修改，无则添加。
# dt.update({"name": "Jack"})  # 有值的情况，进行修改
# print(dt)

# dt.update({"score": 100})    # 无值的情况，进行添加
# print(dt)

# # 5. fromkeys 这个方法用于创建一个新的字典，其中包含指定的键和统一的值（默认为None）。
# # 使用列表创建字典，默认为none
# dt1 = dict.fromkeys(['name', "age", "year"])
# print(dt1)

# # 使用元组创建新字典，初始值为0
# dt2 = dict.fromkeys(("k1", "k2", "K3"), 0)
# print(dt2)

# # 使用集合创建新字典，初始值为“default”
# dt3 = dict.fromkeys({"key1", "key2", "key3"}, "default")
# print(dt3)

# 6. setdefault setdefault() 方法是字典（dict）对象提供的一个方法，用于获取字典中指定键的值。如果键存在于字典中，则返回该键对应的值；如果键不存在，则插入指定的键值对，并返回默认值（如果提供了）。
# 这个方法的作用类似于通过键访问字典的 get() 方法，但有一个关键区别：如果键不存在，setdefault() 方法会将指定的键值对插入字典中。
# print(dt.setdefault('name'))
# print(dt.setdefault("k1", 111))
# print(dt)
