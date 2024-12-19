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
                expected = int(f.readline().strip())
                if result == expected:
                    print(f"{Fore.GREEN}✓ Passed!{Style.RESET_ALL}")
                else:
                    print(f"{Fore.RED}✗ Failed! Expected {expected}, got {result}{Style.RESET_ALL}")
        else:
            print(f"{Fore.YELLOW}Answer: {result}{Style.RESET_ALL}")

def thing(input_str):
    lines = input_str.strip().split('\n')
    n = int(lines[0])
    shell_at_pos = [i for i in range(3)]
    counter = [0 for _ in range(3)]
    for i in range(n):
        a, b, g = [int(x) - 1 for x in lines[i+1].split()]
        shell_at_pos[a], shell_at_pos[b] = shell_at_pos[b], shell_at_pos[a]
        counter[shell_at_pos[g]] += 1

    return max(counter)

#runTests()
print(thing())
