import os
from colorama import Fore, Style, init

def fileDetect():
    init()  # Initialize colorama
    files = []
    for file in os.listdir(os.path.dirname(__file__)):
        if file.endswith('.in') or file.endswith('.out'):
            files.append(file)
    
    if len(files) == 0:
        print(f"{Fore.RED}No input/output files found in current directory{Style.RESET_ALL}")
        return
        
    print(f"\n{Fore.CYAN}Available test files:{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}-" * 30 + f"{Style.RESET_ALL}")
    
    in_files = sorted([f for f in files if f.endswith('.in')])
    for i, f in enumerate(in_files, 1):
        out_file = f[:-3] + '.out'
        if out_file in files:
            print(f"{Fore.GREEN}{i}. {f} (with matching .out file){Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}{i}. {f} (no matching .out file){Style.RESET_ALL}")
            
    print(f"{Fore.YELLOW}-" * 30 + f"{Style.RESET_ALL}")
    return in_files

def runTests():
    in_files = fileDetect()
    if not in_files:
        return

    for in_file in in_files:
        print(f"\n{Fore.CYAN}Testing {in_file}...{Style.RESET_ALL}")
        
        with open(in_file, 'r') as f:
            input_str = f.read()
        
        result = thing(input_str)
        
        out_file = in_file[:-3] + '.out'
        if os.path.exists(out_file):
            with open(out_file, 'r') as f:
                expected = [int(line.strip()) for line in f.readlines()]
                if result == expected:
                    print(f"{Fore.GREEN}✓ Passed!{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}✗ Failed! Expected {expected}, got {result}{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}Answer: {result}{Style.RESET_ALL}")

def thing(input):
    lines = input.strip().split('\n')
    N = 3  # The number of buckets
    TURN_NUM = 100
    
    # Initialize capacity and milk arrays
    capacity = [0 for _ in range(N)]
    milk = [0 for _ in range(N)]
    
    # Parse input into arrays
    for i in range(N):
        capacity[i], milk[i] = map(int, lines[i].split())
    
    for i in range(TURN_NUM):
        bucket1 = i % N
        bucket2 = (i + 1) % N
        
        # Amount to pour is min of source milk and destination space
        amt = min(milk[bucket1], capacity[bucket2] - milk[bucket2])
        
        milk[bucket1] -= amt
        milk[bucket2] += amt
        
    return milk
runTests()