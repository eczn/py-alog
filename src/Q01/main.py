# 吧一行输入转为数字
def line2nums(lineStr):
    lst = []
    for x in lineStr.split(' '):
        lst.append(int(x.strip()))

    return lst


# 列表合并, 将 Lb 合并到 La
def union(La, Lb): 
    for b in Lb:
        if b not in La: 
            La.append(b)
    return La



# 读文件
f = open("./input.txt", "r")
lineOne = f.readline()
lineTwo = f.readline()

La = line2nums(lineOne)
Lb = line2nums(lineTwo)

print('输入La:', La)
print('输入Lb:', Lb)
union(La, Lb)
print('合并结果:', La)
