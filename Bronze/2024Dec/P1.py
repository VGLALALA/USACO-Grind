
import sys
input = sys.stdin.readline
T = int(input())

for i in range(T):
    query = int(input())
    # Precompute valid ranges 
    ranges = []
    for length in range(2, 10):
        low = '4' * (length-1) + '5'  
        high = '4' + '9' * (length-1)
        ranges.append((int(low), int(high)))
    print(ranges)

    if query < 2:
        print(0)
        continue
        
    ans = 0
    for start, end in ranges:
        print("ans: " + str(ans))
        if start > query:
            break
        print("start,end: " + str((start,end)))
        valid_end = min(end, query)
        if valid_end >= start:
            ans += valid_end - start + 1
        print("valid_end: " + str(valid_end))
            
    print(ans)
