# 多个装饰器

# 定义函数：完成包裹数据
def make_bold(fn):
    def wrapped():
        return "<b>"+fn()+"<b>"
    return wrapped

# 定义函数：完成包裹数据
def make_italic(fn):
    def wrapped():
        return "<i>"+fn()+"<i>"
    return wrapped

@make_bold
def test1():
    return "hello world-1"

@make_italic
def test2():
    return  "hello world-2"

@make_bold
@make_italic
def test3():
    return "hello world-3"

print(test1())
print(test2())
print(test3())