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
    
    in_files = sorted([f for f in files if f.endswith('.in')], 
                     key=lambda x: (len(x), x))  # Sort by length first, then alphabetically
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
        lines = input_str.strip().split('\n')
        result = Solution(lines)
        
        out_file = in_file[:-3] + '.out'
        if os.path.exists(out_file):
            with open(out_file, 'r') as f:
                expected = int(f.read().strip())
                if result == expected:
                    print(f"{Fore.GREEN}✓ Passed!{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}✗ Failed! Expected {expected}, got {result}{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}Answer: {result}{Style.RESET_ALL}")

def thing(inp):
    x, y = map(int,inp[0].split())
    traveldis = 0
    index = 0
    currentpos = x
    while True:
        next_pos = (1 if index % 2 == 0 else -1) * (1 << (index // 2))
        if next_pos <= y <= currentpos or currentpos <= y <= next_pos:
            traveldis += abs(y - currentpos)
            break
        traveldis += abs(currentpos - next_pos)
        currentpos = next_pos
        index += 1

    return traveldis

def Solution(inp):
    x, y = map(int,inp[0].split())
    if y > x:
        p = 0
        while (2**p) + x < y:
            p += 2
    else:
        p = 1
        while x - (2**p) > y:
            p += 2

    # Then calculates total distance in one go
    total_distance = 1
    for i in range(1, p):
        total_distance += (2**i) + (2 ** (i - 1))
    total_distance += (2 ** (p - 1)) + abs(x - y)
    return total_distance
            

runTests()
# 3 -> 4 = 1
# 4 -> 2 = 2 
# 2 -> 6 = 4