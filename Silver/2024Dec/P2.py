# 导入系统模块以使用标准输入
import sys
input = sys.stdin.readline

# 读取测试用例数量T
T = int(input())

# 定义树状数组(Fenwick Tree)类
class Fenw:
    def __init__(self, n):
        # 初始化大小为n的树状数组
        self.n = n
        self.fw = [0]*(n+1)
        
    def update(self, i, v):
        # 更新树状数组中索引i的值,增加v
        # i & (-i)用于获取最低位1
        while i <= self.n:
            self.fw[i] += v
            i += i & (-i)
            
    def sum(self, i):
        # 计算从1到i的前缀和
        s = 0
        while i > 0:
            s += self.fw[i]
            i -= i & (-i)
        return s
        
    def range_sum(self, l, r):
        # 计算区间[l,r]的和
        return self.sum(r)-self.sum(l-1)
        
    def fenw_find(self, k):
        # 二分查找第k大的元素位置
        p = 0
        m = 1<<(self.n.bit_length()-1)
        while m > 0:
            n = p + m
            if n <= self.n and self.fw[n] < k:
                k -= self.fw[n]
                p = n
            m >>= 1
        return p+1

# 处理每个测试用例
for _ in range(T):
    # 读取n和k
    # n是数组长度,k是区间数量
    n, k = map(int, input().split())
    
    # 读取数组a
    a = list(map(int, input().split()))
    
    # 读取k个区间
    ivs = []
    for __ in range(k):
        # l,r是区间边界,t是目标值
        l, r, t = map(int, input().split())
        ivs.append((l, r, t))

    # 对数组a排序
    a.sort()
    # 按右边界对区间排序
    ivs.sort(key=lambda x: x[1])

    # 初始化树状数组,用于维护每个位置是否被使用
    f = Fenw(n)
    for i in range(1, n+1):
        f.update(i, 1)

    # 导入二分查找模块
    import bisect
    def lb(v):
        # 查找大于等于v的第一个位置
        return bisect.bisect_left(a, v)
    def rb(v):
        # 查找小于等于v的最后一个位置
        return bisect.bisect_right(a, v)-1

    # cnt记录需要移除的元素数量
    cnt = 0
    p = 0

    # 处理每个区间
    for (l, r, t) in ivs:
        # 找到区间[l,r]在排序后数组中的位置
        li = lb(l)
        ri = rb(r)
        
        # 如果区间无效则跳过
        if li > ri or li < 0 or ri < 0 or li >= n or ri >= n:
            continue

        # 计算区间内元素总数
        tot = ri - li + 1
        # 计算区间内还未被移除的元素数量
        av = f.range_sum(li+1, ri+1)
        # 计算已经被移除的元素数量
        ch = tot - av

        # 需要额外移除的元素数量
        need = t - ch
        while need > 0:
            # 找到右边界之前的元素和
            sr = f.sum(ri+1)
            # 找到对应的位置
            ci = f.fenw_find(sr) - 1
            # 标记该位置元素被移除
            f.update(ci+1, -1)
            cnt += 1
            need -= 1

    # 计算最终剩余的元素数量
    ans = n - cnt
    print(ans)
