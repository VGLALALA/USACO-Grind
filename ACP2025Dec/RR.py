import sys

input = sys.stdin.readline
T = int(input())

rounding_ranges = []
for digit_length in range(2, 10):
    chain_start = int('4' * (digit_length - 1) + '5')
    chain_end = int('4' + '9' * (digit_length - 1))
    rounding_ranges.append((chain_start, chain_end))

for _ in range(T):
    N = int(input())

    if N < 2:
        print(0)
        continue

    count_differences = 0

    for chain_start, chain_end in rounding_ranges:
        if chain_start > N:
            break

        upper_limit = min(chain_end, N)

        if upper_limit >= chain_start:
            count_differences += upper_limit - chain_start + 1

    print(count_differences)
