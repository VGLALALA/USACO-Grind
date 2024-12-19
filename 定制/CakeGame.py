import sys
input = sys.stdin.readline

def that(num_cases):
    for _ in range(num_cases):
        num_cakes = int(input())
        cake_sizes = list(map(int, input().split()))
        
        half_cake_index = num_cakes // 2 - 1
        bessie_share = sum(cake_sizes[i] for i in range(half_cake_index))
        max_elsie_share = bessie_share
        
        for i in range(half_cake_index):
            bessie_share = bessie_share - cake_sizes[half_cake_index - 1 - i] + cake_sizes[num_cakes - 1 - i]
            max_elsie_share = max(max_elsie_share, bessie_share)
        
        total_cakes = sum(cake_sizes)
        print(total_cakes - max_elsie_share, max_elsie_share)

test_cases = int(input())
that(test_cases)
