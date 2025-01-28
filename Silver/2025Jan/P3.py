def solve():
    import sys
    sys.setrecursionlimit(10**7)
    
    input_data = sys.stdin.read().strip().split()
    N = int(input_data[0])
    vals = list(map(int, input_data[1:]))
    
    if N == 1:
        print(vals[0])
        return

    T = []
    idx = 0
    for r in range(N):
        row = vals[idx : idx + N]
        idx += N
        T.append(row)

    from collections import defaultdict, deque
    
    value_to_cells = defaultdict(list)
    for r in range(N):
        for c in range(N):
            value_to_cells[T[r][c]].append((r,c))
    
    distinct_values = sorted(value_to_cells.keys())
    comp_id_for_value = {}
    for i,v in enumerate(distinct_values):
        comp_id_for_value[v] = i
    comp_count = len(distinct_values)
    
    comp = [[0]*N for _ in range(N)]
    for v in distinct_values:
        cid = comp_id_for_value[v]
        for (r,c) in value_to_cells[v]:
            comp[r][c] = cid

    adj = [[] for _ in range(comp_count)]
    for r in range(N):
        for c in range(N-1):
            ca = comp[r][c]
            cb = comp[r][c+1]
            if ca != cb:
                adj[ca].append((cb, 'col', c))
                adj[cb].append((ca, 'col', c))
    for c in range(N):
        for r in range(N-1):
            ca = comp[r][c]
            cb = comp[r+1][c]
            if ca != cb:
                adj[ca].append((cb, 'row', r))
                adj[cb].append((ca, 'row', r))

    row_diff = [None]*(N-1)
    col_diff = [None]*(N-1)
    x = [None]*comp_count
    x[0] = 0

    queue = deque([0])
    in_queue = [False]*comp_count
    in_queue[0] = True

    while queue:
        u = queue.popleft()
        in_queue[u] = False
        base_x = x[u]
        for (v, typ, idx_) in adj[u]:
            if x[v] is None:
                if typ == 'row':
                    if row_diff[idx_] is None:
                        row_diff[idx_] = 0
                    x[v] = base_x - row_diff[idx_]
                else:
                    if col_diff[idx_] is None:
                        col_diff[idx_] = 0
                    x[v] = base_x - col_diff[idx_]
                queue.append(v)
                in_queue[v] = True
            else:
                want_diff = base_x - x[v]
                if typ == 'row':
                    if row_diff[idx_] is None:
                        row_diff[idx_] = want_diff
                    else:
                        if row_diff[idx_] != want_diff:
                            row_diff[idx_] = want_diff
                            if not in_queue[u]:
                                queue.append(u)
                                in_queue[u] = True
                else:
                    if col_diff[idx_] is None:
                        col_diff[idx_] = want_diff
                    else:
                        if col_diff[idx_] != want_diff:
                            col_diff[idx_] = want_diff
                            if not in_queue[u]:
                                queue.append(u)
                                in_queue[u] = True

    for r in range(N-1):
        if row_diff[r] is None:
            row_diff[r] = 0
    for c in range(N-1):
        if col_diff[c] is None:
            col_diff[c] = 0

    x = [None]*comp_count
    x[0] = 0
    queue = deque([0])
    in_queue = [False]*comp_count
    in_queue[0] = True

    while queue:
        u = queue.popleft()
        in_queue[u] = False
        base_x = x[u]
        for (v, typ, idx_) in adj[u]:
            want_diff = None
            if typ == 'row':
                want_diff = row_diff[idx_]
            else:
                want_diff = col_diff[idx_]
            candidate = base_x - want_diff
            if x[v] is None or x[v] != candidate:
                if x[v] is not None and x[v] != candidate:
                    pass
                x[v] = candidate
                if not in_queue[v]:
                    queue.append(v)
                    in_queue[v] = True

    raw_values = []
    for r in range(N):
        for c in range(N):
            raw_values.append(x[ comp[r][c] ])

    from collections import Counter

    desired_count = {}
    for k in range(2, 2*N+1):
        count_k = min(k-1, 2*N+1 - k)
        desired_count[k] = count_k

    min_raw = min(raw_values)
    max_raw = max(raw_values)
    min_shift = 2 - min_raw
    max_shift = 2*N - max_raw

    target_sorted = []
    for k in range(2, 2*N+1):
        target_sorted.extend([k]*desired_count[k])
    target_sorted = tuple(target_sorted)

    from bisect import bisect_left, bisect_right

    raw_values.sort()
    possible_solution_shift = None

    raw_vals_sorted = raw_values
    target_len = len(target_sorted)

    ans_shift = None
    for S in range(min_shift, max_shift+1):
        ok = True
        for i in range(target_len):
            if raw_vals_sorted[i] + S != target_sorted[i]:
                ok = False
                break
        if ok:
            ans_shift = S
            break

    final_x = [xx + ans_shift for xx in x]

    out = []
    for r in range(N):
        row_result = [str(final_x[ comp[r][c] ]) for c in range(N)]
        out.append(" ".join(row_result))
    print("\n".join(out))
solve()