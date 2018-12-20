# ==、is

a=[11,22,33]
b=[11,22,33]
print(a==b)
print(a is b)

# is是比较两个引用是否是指向了同一个对象(引用比较）
# ==是比较两个对象是否相等

c=a
print(c)

print(id(a))
print(id(b))
print(id(c))
print(a==c)


