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
        result = thing(lines)
        
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
    N, M = map(int, inp[0].split())
    fx, fy = map(int, inp[1].split())
    bx, by = map(int, inp[2].split())
    SF = inp[3].strip()
    SB = inp[4].strip()

    dx = {'E': 1, 'W': -1, 'N': 0, 'S': 0}
    dy = {'E': 0, 'W': 0, 'N': 1, 'S': -1}

    F = [(fx, fy)]
    for c in SF:
        fx += dx[c]
        fy += dy[c]
        F.append((fx, fy))

    B = [(bx, by)]
    for c in SB:
        bx += dx[c]
        by += dy[c]
        B.append((bx, by))


    dp = {}
    for fi in range(len(F)-1, -1, -1):
        for bi in range(len(B)-1, -1, -1):
            if fi == 0 and bi == 0:
                base = 0
            else:
                fx, fy = F[fi]
                bx, by = B[bi]
                base = (fx - bx)**2 + (fy - by)**2
                
            if fi + 1 == len(F) and bi + 1 == len(B):
                dp[(fi, bi)] = base
                continue
                
            best = float('inf')
            if fi + 1 < len(F):
                best = min(best, base + dp[(fi + 1, bi)])
            if bi + 1 < len(B):
                best = min(best, base + dp[(fi, bi + 1)])
            if fi + 1 < len(F) and bi + 1 < len(B):
                best = min(best, base + dp[(fi + 1, bi + 1)])
                
            dp[(fi, bi)] = best
            
    return dp[(0, 0)]

runTests()