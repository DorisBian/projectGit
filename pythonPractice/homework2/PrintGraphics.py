i=0
while i < 5:
    j=0
    while j<=i:
        print("*",end="")
        j+=1
    print(end="\n")
    i+=1


for i in range(0,11,2):
    if i < 5:
        print("*"*i, end="\n")
    else:
        print("*"*(10-i), end="\n")

name = "dlbavhfvfvjkfd"
for s in name:
    print("--------")
    if s=="v":
        continue
    print(s)
    
