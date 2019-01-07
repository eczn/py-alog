# 数列逆序对个数

BORDER = 400

class Node:
    def __init__(self, l, r, c):
        self.left = l
        self.right = r
        self.counter = c

class SegTree:
    def __init__(self):
        self.initTree()
    
    def initTree(self):
        self.tree = []
        for i in range(BORDER):
            n = Node(0, 0, 0)
            self.tree.append(n)

    def construct(self, index, lef, rig):
        segTree = self.tree
        segTree[index].left = lef
        segTree[index].right = rig
        segTree[index].counter = 0

        if (lef == rig):
            return

        mid = int( (lef + rig) / 2 )

        self.construct(index + index + 1, lef, mid)
        self.construct(index + index + 2, mid + 1, rig)

    def insert(self, index, x):
        segTree = self.tree

        segTree[index].counter += 1

        if segTree[index].left == segTree[index].right:
            return
        
        mid = int( (segTree[index].left + segTree[index].right) / 2 )

        if x <= mid:
            self.insert(index*2+1, x)
        else:
            self.insert(index*2+2, x)

    def query(self, index, left, right):
        segTree = self.tree

        if (segTree[index].left==left) and (segTree[index].right==right):
            return segTree[index].counter
        
        mid = int( (segTree[index].left+segTree[index].right) / 2 )

        if right <= mid:
            return self.query(index + index + 1,left,right)
        elif left > mid:
            return self.query(index + index + 2,left,right)
        else: 
            return self.query(index*2+1,left,mid) + self.query(index*2+2,mid+1,right)

    def count(self, list):
        self.initTree()
        self.construct(0, 0, 100)
        sum = 0
        for i, elem in enumerate(list):
            t = st.query(0, elem + 1, 100)
            sum += t
            st.insert(1, elem)
        return sum



# 下面是输入参数测试:

def line2nums(lineStr):
    lst = []
    for x in lineStr.split(' '):
        lst.append(int(x.strip()))

    return lst    

# 读文件
f = open("./input.txt", "r")
line = f.readline()
nums = line2nums(line)

# 将读入的列表传入 SegTree 求逆序数
st = SegTree()
sum = st.count(nums)

print('输入:', line)
print('结果:', sum)
