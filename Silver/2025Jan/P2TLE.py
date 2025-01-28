T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    a = list(map(int, input().split()))
    
    min_ops = float('inf')
    for x in range(M):
        curr_ops = 0
        for num in a:
            rem = num % M
            dist1 = (x - rem) % M
            dist2 = (rem - x) % M
            curr_ops += min(dist1, dist2)
        min_ops = min(min_ops, curr_ops)
    
    print(min_ops)
