# 大根堆（二叉堆）实现 （存储罐优先队列问题）
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




# k 路归并 
# 利用前述实现的二叉堆进行归并
class KMerge:
    def __init__(self):
        self.ks = []
    
    def init(self, __ks):
        self.ks = __ks

    def sort(self):
        lst = []
        while 1:
            max = self.sortOne()
            if (max == None):
                break
            else:
                lst.append(max)

        return lst
        
    def sortOne(self):
        maxs = []
        for k in self.ks:
            if len(k) != 0:
                maxs.append(k[0])
    
        h = MaxHeap()
        h.fromList(maxs)
        theMax = h.getMax()
        
        for k in self.ks:
            if len(k) != 0:
                if k[0] == theMax:
                    k.pop(0)
                    break

        return theMax


# 下面是参数输入和结果输出

def line2nums(lineStr):
    lst = []
    for x in lineStr.split(' '):
        lst.append(int(x.strip()))

    return lst    

# 读文件
f = open("./input.txt", "r")

ks = []
for line in iter(f):
    nums = line2nums(line)
    ks.append(nums)
    print('增加一路:', nums)

K = len(ks)
print('K 为:', K)

merge = KMerge()
merge.init(ks)
result = merge.sort()

print(K, '路排序结果:', result)
