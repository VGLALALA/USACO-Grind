import sys
input = sys.stdin.readline

T = int(input())

def init(size):
    return [0] * (size + 1)

def update(fw, size, idx, val):
    while idx <= size:
        fw[idx] += val
        idx += idx & (-idx)

def sum(fw, idx):
    total = 0
    while idx > 0:
        total += fw[idx]
        idx -= idx & (-idx)
    return total

def range_sum(fw, left, right):
    return sum(fw, right) - sum(fw, left - 1)

def find(fw, size, k):
    pos = 0
    bit_mask = 1 << (size.bit_length() - 1)
    while bit_mask > 0:
        next_pos = pos + bit_mask
        if next_pos <= size and fw[next_pos] < k:
            k -= fw[next_pos]
            pos = next_pos
        bit_mask >>= 1
    return pos + 1

import sys
import bisect
input = sys.stdin.readline

def init(size):
    return [0] * (size + 1)

def update(fw, size, idx, val):
    while idx <= size:
        fw[idx] += val
        idx += idx & (-idx)

def sum(fw, idx):
    total = 0
    while idx > 0:
        total += fw[idx]
        idx -= idx & (-idx)
    return total

def range_sum(fw, left, right):
    return sum(fw, right) - sum(fw, left - 1)

def find(fw, size, k):
    pos = 0
    bit_mask = 1 << (size.bit_length() - 1)
    while bit_mask > 0:
        next_pos = pos + bit_mask
        if next_pos <= size and fw[next_pos] < k:
            k -= fw[next_pos]
            pos = next_pos
        bit_mask >>= 1
    return pos + 1

def process_case():
    N, K = map(int, input().split())
    trees = list(map(int, input().split()))
    intervals = [tuple(map(int, input().split())) for _ in range(K)]

    trees.sort()
    intervals.sort(key=lambda x: x[1])

    fw = init(N)
    for i in range(1, N + 1):
        update(fw, N, i, 1)

    def idx_l_bound(val):
        return bisect.bisect_left(trees, val)

    def idx_r_bound(val):
        return bisect.bisect_right(trees, val) - 1

    removed_count = 0

    for (l, r, t) in intervals:
        left_idx = idx_l_bound(l)
        right_idx = idx_r_bound(r)

        if left_idx > right_idx or left_idx < 0 or right_idx < 0 or left_idx >= N or right_idx >= N:
            continue

        total_in_interval = right_idx - left_idx + 1
        available_in_interval = range_sum(fw, left_idx + 1, right_idx + 1)
        chosen_in_interval = total_in_interval - available_in_interval

        need = t - chosen_in_interval
        while need > 0:
            sumR = sum(fw, right_idx + 1)
            chosen_idx = find(fw, N, sumR) - 1
            update(fw, N, chosen_idx + 1, -1)
            removed_count += 1
            need -= 1

    print(N - removed_count)

T = int(input())
for _ in range(T):
    process_case()
