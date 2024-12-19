MOD = 1000000007
import sys
def find_previous_position(position_set, x):
    from bisect import bisect_left
    sorted_positions = sorted(position_set)
    idx = bisect_left(sorted_positions, x)
    return sorted_positions[idx - 1] if idx > 0 else 0

def that(n, preference_string):
    red_count = [0] * (n + 1)
    blue_count = [0] * (n + 1)
    dp = [0] * (n + 1)
    prefix_sum_dp = [[0] * 2 for _ in range(n + 1)]
    
    red_positions = set()
    blue_positions = set()
    
    for i in range(1, n + 1):
        red_count[i] = red_count[i - 1]
        blue_count[i] = blue_count[i - 1]
        
        if preference_string[i - 1] == 'R':
            red_count[i] += 1
            red_positions.add(i)
        if preference_string[i - 1] == 'B':
            blue_count[i] += 1
            blue_positions.add(i)

    blue_positions.add(0)
    blue_positions.add(n + 1)
    red_positions.add(0)
    red_positions.add(n + 1)

    dp[0] = 1
    prefix_sum_dp[0][0] = 1
    
    for i in range(1, n + 1):
        if preference_string[i - 1] == 'X':
            dp[i] = dp[i - 1]
        
        distance = 1
        while True:
            prev_position = find_previous_position(blue_positions, i - distance + 1)
            while distance * 2 <= i and prev_position >= i - distance * 2 + 1:
                distance = i - find_previous_position(blue_positions, i - distance * 2 + 1) + 1

            if distance * 2 > i or red_count[i] - red_count[i - distance] > 0:
                break

            p = find_previous_position(blue_positions, i - distance)
            red_position = find_previous_position(red_positions, i - distance + 1)
            p = max(p, i - (i - red_position + 1) * 2 + 1)
            
            dp[i] = (dp[i] + prefix_sum_dp[i - distance * 2][i % 2] - (prefix_sum_dp[p - 1][i % 2] if p else 0)) % MOD
            distance = (i - p + 1) // 2
            if i - distance * 2 + 1 > p:
                distance += 1
        
        prefix_sum_dp[i][0] = prefix_sum_dp[i - 1][0]
        prefix_sum_dp[i][1] = prefix_sum_dp[i - 1][1]
        prefix_sum_dp[i][i % 2] = (prefix_sum_dp[i][i % 2] + dp[i]) % MOD

    return dp[n]

input = sys.stdin.readline
n = int(input().strip())
preference_string = input().strip()
result = that(n, preference_string)
sys.stdout.write(str(result) + '\n')
