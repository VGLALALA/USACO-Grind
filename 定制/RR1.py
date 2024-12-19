def nearest_power_of_ten(x, b):
    power = 10 ** b
    remainder = x % power
    if remainder >= power // 2:
        return x + (power - remainder)
    else:
        return x - remainder

def chain_rounding(x):
    current = x
    b = 1
    while True:
        rounded = nearest_power_of_ten(current, b)
        if rounded == current:
            return rounded
        current = rounded
        b += 1

def count_differences(N):
    count = 0
    for x in range(1, N + 1):
        b = 1
        while 10 ** b <= x:
            b += 1
        bessie_result = nearest_power_of_ten(x, b - 1)
        
        elise_result = chain_rounding(x)
        
        if bessie_result != elise_result:
            count += 1
    return count

def that():
    T = int(input())
    for _ in range(T):
        N = int(input())
        print(count_differences(N))

that()