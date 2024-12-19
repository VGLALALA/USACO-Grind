import sys
input = sys.stdin.readline

def solve_cake_sharing(num_cases):
    for _ in range(num_cases):
        size = int(input())
        cakes = list(map(int, input().split()))
        
        required = size // 2 - 1
        best_share = sum(cakes[i] for i in range(required)) 
        current_share = best_share
        
        for i in range(required):
            current_share = current_share + cakes[size - 1 - i] - cakes[required - 1 - i]
            best_share = max(best_share, current_share)
            
        cake_total = sum(cakes)
        print(cake_total - best_share, best_share)

if __name__ == "__main__":
    test_cases = int(input())
    solve_cake_sharing(test_cases)
