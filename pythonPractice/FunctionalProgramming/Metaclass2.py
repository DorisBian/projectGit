# 自定义元类

def upper_attr(future_class_name,future_class_parents,future_class_attr):
    # 遍历属性字典，把所有不是__开头的属性名字变为大写
    newAttr={}
    for name,value in future_class_attr.items():
        if not name.startswith("__"):
            newAttr[name.upper()]=value

    # 调用type来创建一个类
    return type(future_class_name,future_class_parents,newAttr)

# 设置Foo类的元类为upper_attr
class Foo(object,metaclass=upper_attr):
    bar="bip"

print(hasattr(Foo,"bar"))
print(hasattr(Foo,"BAR"))

t=Foo()
# print(t.bar)     出错
# print(t.BAR)     出错
