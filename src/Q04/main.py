# 星星级别

# 在程序输入之后 A C 也会改变
A = []
C = []

# lowbit 计算
def LOWBIT(x):
    return x & (-x)

# 修改 C
def change(x):
    while x <= (len(C) - 1):
        C[x] += 1
        x += LOWBIT(x)

# 计算和
def getSum(i):
    t = 0
    while i > 0:
        t += C[i]
        i -= LOWBIT(i)

    return t

####### 下面是参数输入测试

# 把一行输入转为数字
def line2nums(lineStr):
    lst = []
    for x in lineStr.split(' '):
        lst.append(int(x.strip()))

    return lst

f = open("./input.txt", "r")

print('输入:')

starsCount = int(f.readline().strip())

print(starsCount)

A = [0] * starsCount
# 坐标不超过 1024
C = [0] * 1024

# 输入星星坐标
for i in range(starsCount):
    # 解构
    (x, y) = line2nums(f.readline())
    print(x, y)
    # 调整
    A[getSum(x)] = A[getSum(x)] + 1
    change(x)

# 输出结果
print('\n结果:')
for sum in A:
    print(sum)

