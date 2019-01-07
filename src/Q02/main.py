# 储钱罐问题描述
# 自动储钱罐：
#    1. 有一个钱孔可以投硬币
#    2. 有一个按钮取硬币，每次取出罐子里面值最大的硬币 
# 
# 解决方法：使用大根堆（二叉堆）的数据结构，每次都可以取出最大的
# 
class MaxHeap: 
    def __init__(self):
        self.list = []
    
    # 从列表中建堆
    def fromList(self, A):
        self.list = A 

        n = len(A) - 1
        for node in range(int(n / 2), -1, -1):
            self.down(node)
        return
    
    # 下沉
    def down(self, node):
        A = self.list
        child = 2 * node + 1
        
        if child > len(A) - 1:
            return
        if (
            child + 1 <= len(A) - 1) and (A[child+1] > A[child]):
            child += 1
        # preserves heap structure
        if A[node] < A[child]:
            self.swap(node, child)
            self.down(child)
        else:
            return

    # 交换
    def swap(self, i, j):
        A = self.list
        A[i], A[j] = A[j], A[i]
        return

    # 上浮
    def up(self, node): 
        A = self.list
        parent = int((node - 1) / 2)
        
        if A[parent] < A[node]:
            self.swap(node, parent)
        
        if parent <= 0:
            return
        else:
            self.up(parent)

    # 取出最大的，而且要进行调整
    def getMax(self):
        # 若为空返回 None
        if self.isEmpty():
            return None
        
        A = self.list
        n = len(A) - 1
        self.swap(0, n)
        max = A.pop(n)
        self.down(0)

        return max
    
    # 插入到堆中并调整
    def insert(self, val):
        A = self.list; 
        A.append(val)
        self.up(len(A) - 1)
        return

    # 判断是否为空
    def isEmpty(self):
        return len(self.list) == 0 


# 读文件
f = open("./input.txt", "r")

h = MaxHeap()
h.fromList([])

print('初始堆为空:', [])

for line in iter(f):
    coin = int(line.strip())
    h.insert(coin)
    print('投入硬币', coin, '插入后堆为:', h.list)

print('取出最大面值：(getMax操作)', h.getMax())
print('最终堆为:', h.list)
