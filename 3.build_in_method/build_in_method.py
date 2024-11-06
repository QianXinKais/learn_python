"""
以下全部是一些常用的内置方法
"""
"""
类型转换
    int(x)：将 x 转换为整数。
    float(x)：将 x 转换为浮点数。
    str(x)：将 x 转换为字符串。
    bool(x)：将 x 转换为布尔值。
    list(iterable)：将 iterable 转换为列表。
    tuple(iterable)：将 iterable 转换为元组。
    set(iterable)：将 iterable 转换为集合。
    dict(mapping)：将 mapping 转换为字典。
"""
a = 3
b = 12.3
c = 0
d = 'hello world!'
x = int(b)
print(x, type(x))

x = float(a)
print(x, type(x))

x = str(a)
print(x, type(x))

x = bool(a)
y = bool(c)
print(x, type(x))
print(y, type(y))

x = list(d)
print(x, type(x))

x = tuple(d)
print(x, type(x))

x = set(d)
print(x, type(x))

x = dict([['name', 'tom'], ('age', 18)])
print(x, type(x))

"""
    数值相关的
        abs(x)：返回数值的绝对值。
        round(x, [ndigits])：返回四舍五入后的值。
        pow(x, y [, z])：计算 x 的 y 次幂，如果提供 z，则取模 z。
"""

"""
    数据结构相关
        len(s)：返回对象（字符串、列表、元组等）的长度。
        min(iterable, *[, key, default])：返回最小值。
        max(iterable, *[, key, default])：返回最大值。
        sum(iterable[, start])：返回求和结果。
        sorted(iterable, *, key=None, reverse=False)：返回排序后的列表。
        reversed(seq)：返回反向迭代器。
"""

"""
    输入输出
        print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)：打印对象到文本流。
        input([prompt])：从标准输入接收用户输入。
"""

"""
字符串方法
    str.lower()：返回字符串的小写版本。
    str.upper()：返回字符串的大写版本。
    str.strip([chars])：移除字符串开头和结尾的指定字符（默认为空格）。
    str.replace(old, new[, count])：返回字符串的副本，其中所有的 old 子字符串都被替换为 new。
    str.split([sep[, maxsplit]])：通过指定分隔符将字符串拆分为列表。
    str.join(iterable)：将可迭代对象的元素连接成一个字符串。
"""
"""
列表方法
    list.append(x)：在列表末尾添加一个元素。
    list.extend(iterable)：通过添加 iterable 中的所有元素来扩展列表。
    list.insert(i, x)：在指定位置插入一个元素。
    list.remove(x)：移除列表中第一个值为 x 的元素。
    list.pop([i])：移除并返回列表中的元素，默认为最后一个元素。
    list.clear()：移除列表中的所有元素。
    list.index(x[, start[, end]])：返回列表中第一个值为 x 的元素的索引。
    list.count(x)：返回 x 在列表中出现的次数。
    list.sort(*, key=None, reverse=False)：对列表进行原地排序。
    list.reverse()：反转列表中的元素。
"""

"""
字典方法
    dict.keys()：返回字典中的所有键。
    dict.values()：返回字典中的所有值。
    dict.items()：返回字典中的所有键值对。
    dict.get(key[, default])：返回键对应的值，如果键不在字典中则返回默认值。
    dict.update([other])：更新字典，添加其他键值对。
    dict.pop(key[, default])：移除指定键并返回其值。
    dict.popitem()：移除并返回最后插入的键值对。
    dict.clear()：移除字典中的所有项。
"""

"""
集合方法
    set.add(elem)：向集合中添加元素。
    set.update(*others)：用另一个集合更新集合。
    set.remove(elem)：移除指定元素，如果元素不存在会引发 KeyError。
    set.discard(elem)：移除指定元素，如果元素不存在不会引发错误。
    set.pop()：移除并返回任意一个元素。
    set.clear()：移除集合中的所有元素。
"""
