T = int(input())

def init(n):
    return [0]*(n+1)

def update(fw, n, i, v):
    while i <= n:
        fw[i] += v
        i += i & (-i)

def sum(fw, i):
    s = 0
    while i > 0:
        s += fw[i]
        i -= i & (-i)
    return s

def range_sum(fw, l, r):
    return sum(fw, r) - sum(fw, l-1)

def find(fw, n, k):
    pos = 0
    bit_mask = 1<<(n.bit_length()-1)
    while bit_mask > 0:
        nxt = pos + bit_mask
        if nxt <= n and fw[nxt] < k:
            k -= fw[nxt]
            pos = nxt
        bit_mask >>= 1
    return pos+1

for _ in range(T):
    N, K = map(int, input().split())
    trees = list(map(int, input().split()))
    intervals = []
    for __ in range(K):
        l, r, t = map(int, input().split())
        intervals.append((l, r, t))

    trees.sort()
    intervals.sort(key=lambda x: x[1])

    fw = init(N)
    for i in range(1, N+1):
        update(fw, N, i, 1)

    import bisect
    def idx_l_bound(val):
        return bisect.bisect_left(trees, val)
    def idx_r_bound(val):
        return bisect.bisect_right(trees, val)-1

    chosen_count = 0
    tree_ptr = 0

    for (l, r, t) in intervals:
        left_idx = idx_l_bound(l)
        right_idx = idx_r_bound(r)
        if left_idx > right_idx or left_idx < 0 or right_idx < 0 or left_idx >= N or right_idx >= N:
            continue

        total_in_interval = right_idx - left_idx + 1
        available_in_interval = range_sum(fw, left_idx+1, right_idx+1)
        chosen_in_interval = total_in_interval - available_in_interval

        need = t - chosen_in_interval
        while need > 0:
            sumR = sum(fw, right_idx+1)
            chosen_idx = find(fw, N, sumR) - 1
            update(fw, N, chosen_idx+1, -1)
            chosen_count += 1
            need -= 1

    result = N - chosen_count
    print(result)
