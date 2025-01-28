N = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

matches = [1 if a[i] == b[i] else 0 for i in range(N)]

total = 0
for l in range(N):
    curr_matches = sum(matches[l:])
    for r in range(l, N):
        segment_matches = sum(matches[:l]) + sum(matches[r+1:])
        
        for i in range(l, r+1):
            if a[l + (r-i)] == b[i]:
                segment_matches += 1
                
        total += segment_matches

print(total)
