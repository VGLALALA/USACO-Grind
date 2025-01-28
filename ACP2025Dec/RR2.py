def direct_round(x, P):
    # Rounds x directly to the nearest 10^P
    power = 10**P
    # Truncate to multiples of 10^P
    truncated = (x // power) * power
    # Check the P-th digit from the right (for rounding)
    # This digit is at 10^(P-1) place
    check_digit = (x // (10**(P-1))) % 10
    if check_digit >= 5:
        return truncated + power
    else:
        return truncated

def chain_round(x, P):
    # Chain rounds x: first to 10, then to 100, ..., until 10^P
    for d in range(1, P+1):
        power = 10**d
        truncated = (x // power) * power
        check_digit = (x // (10**(d-1))) % 10
        if check_digit >= 5:
            x = truncated + power
        else:
            x = truncated
    return x

def solve():
    import sys
    input_data = sys.stdin.read().strip().split()
    T = int(input_data[0])
    numbers = list(map(int, input_data[1:] ))
    
    for N in numbers:
        # Find P such that 10^P >= N
        P = 0
        while 10**P < N:
            P += 1

        count_diff = 0
        # For smaller N, we can afford to loop
        for x in range(1, N+1):
            d = direct_round(x, P)
            c = chain_round(x, P)
            if d != c:
                count_diff += 1
        
        print(count_diff)

if __name__ == "__main__":
    solve()
