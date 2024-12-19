import sys
sys.setrecursionlimit(10**7)

dir_map = {
    'L': (0, -1),
    'R': (0, 1),
    'U': (-1, 0),
    'D': (1, 0)
}

def that():
    input_data = sys.stdin.read().strip().split()
    N, Q = map(int, input_data[0:2])
    updates = input_data[2:]
    
    grid = [['?' for _ in range(N)] for __ in range(N)]
    
    for i in range(Q):
        r_i = int(updates[3*i]) - 1
        c_i = int(updates[3*i+1]) - 1
        t_i = updates[3*i+2]
        grid[r_i][c_i] = t_i
    
    for i in range(N):
        for j in range(N):
            if grid[i][j] == '?':
                if i == 0:
                    grid[i][j] = 'U'
                elif i == N-1:
                    grid[i][j] = 'D'
                elif j == 0:
                    grid[i][j] = 'L'
                elif j == N-1:
                    grid[i][j] = 'R'
                else:
                    grid[i][j] = 'U'
    
    def cell_id(x, y):
        return x * N + y
    
    edges = [-1]*(N*N)
    for i in range(N):
        for j in range(N):
            dx, dy = dir_map[grid[i][j]]
            nx, ny = i+dx, j+dy
            u = cell_id(i, j)
            if 0 <= nx < N and 0 <= ny < N:
                v = cell_id(nx, ny)
                edges[u] = v
            else:
                edges[u] = -1

    visited = [0]*(N*N)
    scc_id = [-1]*(N*N)
    scc_count = 0
    
    def dfs(u):
        stack = []
        cur = u
        while True:
            if visited[cur] == 0:
                visited[cur] = 1
                stack.append(cur)
                nxt = edges[cur]
                if nxt == -1:
                    break
                cur = nxt
            elif visited[cur] == 1:
                cycle_start = cur
                cycle_nodes = []
                while stack:
                    x = stack.pop()
                    cycle_nodes.append(x)
                    if x == cycle_start:
                        break
                nonlocal scc_count
                for node in cycle_nodes:
                    scc_id[node] = scc_count
                scc_count += 1
                for rem in stack:
                    visited[rem] = 2
                return
            else:
                break
        for node in stack:
            visited[node] = 2

    for u in range(N*N):
        if edges[u] != -1 and visited[u] == 0:
            dfs(u)
    
    if scc_count > 0:
        sizes = [0]*scc_count
        for u in range(N*N):
            if scc_id[u] != -1:
                sizes[scc_id[u]] += 1
        total_unusable = sum(sizes)
    else:
        total_unusable = 0

    print(total_unusable)

that()
