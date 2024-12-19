# 导入双端队列数据结构
from collections import deque

def solve():
    # 读取输入:n是网格大小,m是操作数量
    n, m = map(int, input().split())
    
    # 初始化n*n的网格,0表示空格
    g = [[0]*n for _ in range(n)]
    # 初始化双端队列用于BFS
    q = deque()
    # 存储所有操作的数组
    arr = []
    
    # 读取m个操作
    for _ in range(m):
        # r是行,c是列,d是方向('U','D','L','R')
        r, c, d = input().split()
        # 坐标从0开始,所以减1
        r, c = int(r)-1, int(c)-1
        # 在网格中标记方向
        g[r][c] = d
        # 将操作添加到数组中
        arr.append((r, c, d))
    
    # 初始化答案数组
    ans = [0]*m
    # rem记录剩余未访问的格子数
    rem = n*n
    # 访问标记数组
    vis = [[0]*n for _ in range(n)]
    
    # 处理边界格子
    for i in range(n):
        for j in range(n):
            # 如果是边界格子
            if i == 0 or j == 0 or i == n-1 or j == n-1:
                # 如果是空格,可以直接逃脱
                if g[i][j] == 0:
                    q.append((i, j))
                    vis[i][j] = 1
                    rem -= 1
                # 如果在上边界且向上,可以逃脱
                if i == 0 and g[i][j] == 'U':
                    q.append((i, j))
                    vis[i][j] = 1
                    rem -= 1
                # 如果在左边界且向左,可以逃脱
                if j == 0 and g[i][j] == 'L':
                    q.append((i, j))
                    vis[i][j] = 1
                    rem -= 1
                # 如果在下边界且向下,可以逃脱
                if i == n-1 and g[i][j] == 'D':
                    q.append((i, j))
                    vis[i][j] = 1
                    rem -= 1
                # 如果在右边界且向右,可以逃脱
                if j == n-1 and g[i][j] == 'R':
                    q.append((i, j))
                    vis[i][j] = 1
                    rem -= 1
    
    # BFS遍历可以逃脱的格子
    while q:
        # 取出队首元素
        r, c = q.popleft()
        
        # 检查上方格子
        if r-1 >= 0 and (g[r-1][c] == 'D' or g[r-1][c] == 0) and not vis[r-1][c]:
            vis[r-1][c] = 1
            q.appendleft((r-1, c))
            rem -= 1
        # 检查下方格子
        if r+1 < n and (g[r+1][c] == 'U' or g[r+1][c] == 0) and not vis[r+1][c]:
            vis[r+1][c] = 1
            q.appendleft((r+1, c))
            rem -= 1
        # 检查左方格子
        if c-1 >= 0 and (g[r][c-1] == 'R' or g[r][c-1] == 0) and not vis[r][c-1]:
            vis[r][c-1] = 1
            q.appendleft((r, c-1))
            rem -= 1
        # 检查右方格子
        if c+1 < n and (g[r][c+1] == 'L' or g[r][c+1] == 0) and not vis[r][c+1]:
            vis[r][c+1] = 1
            q.appendleft((r, c+1))
            rem -= 1
    
    # 记录最后一步的答案
    ans[m-1] = rem
    
    # 从后向前模拟每一步
    for i in range(m-2, -1, -1):
        # 获取当前要移除的箭头位置和方向
        r, c, d = arr[i+1]
        
        # 检查移除箭头后是否可以从边界逃脱
        if r == 0 and g[r][c] != 'U' and not vis[r][c]:
            q.append((r, c))
            vis[r][c] = 1
            rem -= 1
        elif c == 0 and g[r][c] != 'L' and not vis[r][c]:
            q.append((r, c))
            vis[r][c] = 1
            rem -= 1
        elif r == n-1 and g[r][c] != 'D' and not vis[r][c]:
            q.append((r, c))
            vis[r][c] = 1
            rem -= 1
        elif c == n-1 and g[r][c] != 'R' and not vis[r][c]:
            q.append((r, c))
            vis[r][c] = 1
            rem -= 1
            
        # 检查移除箭头的格子是否可以通过相邻的已访问格子逃脱
        if not vis[r][c]:
            for dr, dc in [(0,1), (0,-1), (1,0), (-1,0)]:
                nr, nc = r+dr, c+dc
                if 0 <= nr < n and 0 <= nc < n and not vis[r][c] and vis[nr][nc]:
                    q.append((r, c))
                    vis[r][c] = 1
                    rem -= 1
                    
        # 移除箭头
        g[r][c] = 0
        
        # BFS遍历新的可以逃脱的格子
        while q:
            r, c = q.popleft()
            
            # 检查上方格子
            if r-1 >= 0 and (g[r-1][c] == 'D' or g[r-1][c] == 0) and not vis[r-1][c]:
                vis[r-1][c] = 1
                q.appendleft((r-1, c))
                rem -= 1
            # 检查下方格子
            if r+1 < n and (g[r+1][c] == 'U' or g[r+1][c] == 0) and not vis[r+1][c]:
                vis[r+1][c] = 1
                q.appendleft((r+1, c))
                rem -= 1
            # 检查左方格子
            if c-1 >= 0 and (g[r][c-1] == 'R' or g[r][c-1] == 0) and not vis[r][c-1]:
                vis[r][c-1] = 1
                q.appendleft((r, c-1))
                rem -= 1
            # 检查右方格子
            if c+1 < n and (g[r][c+1] == 'L' or g[r][c+1] == 0) and not vis[r][c+1]:
                vis[r][c+1] = 1
                q.appendleft((r, c+1))
                rem -= 1
                
        # 记录当前步骤的答案
        ans[i] = rem
        
    # 输出所有答案,每行一个数字
    print('\n'.join(map(str, ans)))

# 调用主函数
solve()