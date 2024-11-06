def outer():
    x = 1
    y = 2

    def inner():
        print(x, y)
    return inner


f = outer()
print(f.__closure__)
