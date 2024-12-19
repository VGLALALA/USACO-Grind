import os
from rich import print
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

console = Console()

def fileDetect():
    files = []
    for file in os.listdir(os.path.dirname(__file__)):
        if file.endswith('.in') or file.endswith('.out'):
            files.append(file)
    
    if len(files) == 0:
        console.print(Panel("[red]No input/output files found in current directory[/red]", title="Error", style="bold red"))
        return
        
    console.print(Panel("\n[cyan]Available test files:[/cyan]", title="Files", style="bold cyan"))
    
    # Sort the in_files numerically based on the number before the '.in' extension
    in_files = sorted([f for f in files if f.endswith('.in')], key=lambda x: int(x.split('.')[0]))
    table = Table(title="Test Files", show_header=True, header_style="bold magenta")
    table.add_column("Index", justify="right")
    table.add_column("File Name", justify="left")
    table.add_column("Status", justify="left")
    
    for i, f in enumerate(in_files, 1):
        out_file = f[:-3] + '.out'
        if out_file in files:
            table.add_row(str(i), f, "[green]with matching .out file[/green]")
        else:
            table.add_row(str(i), f, "[yellow]no matching .out file[/yellow]")
            
    console.print(table)
    return in_files

def runTests():
    in_files = fileDetect()
    if not in_files:
        return

    for in_file in in_files:
        console.print(Panel(f"[cyan]Testing {in_file}...[/cyan]", title="Test", style="bold cyan", width=40))
        
        with open(in_file, 'r') as f:
            input_str = f.read()
        lines = input_str.strip().split('\n')
        result = solution(lines)
        
        out_file = in_file[:-3] + '.out'
        if os.path.exists(out_file):
            with open(out_file, 'r') as f:
                expected = int(f.readline().strip())
                if result == expected:
                    console.print(Panel("[green]✓ Passed![/green]", title="Result", style="bold green", width=40))
                else:
                    console.print(Panel(f"[red]✗ Failed! Expected {expected}, got {result}[/red]", title="Result", style="bold red", width=40))
        else:
            console.print(Panel(f"[yellow]Answer: {result}[/yellow]", title="Result", style="bold yellow", width=40))

def thing(inp):
    n = int(inp[0])
    leader = ["",-1]
    stats = []
    change = 0
    cows = {'Elsie':7,'Bessie':7,"Mildred":7}
    for i in range(n):
        day, name, diff = inp[i + 1].split()
        stats.append([int(day),name,int(diff)])
    stats.sort(key=lambda x:x[0])
    #print(stats)
    
    for day,name,diff in stats:
        cows[name] += diff
        if (cows[name] > leader[1] and name != leader[0]) or (diff < 0 and list(cows.values()).count(cows[name]) > 1):
            leader[0],leader[1] = name, cows[name]
            change += 1
        elif cows[name] > leader[1]:
            leader[1] = cows[name]
    print(cows)
    return change

def solution(inp):
    n = int(inp[0])

    cows = []
    for i in range(n):
        g, p, c = inp[i + 1].split()
        g = int(g)
        c = int(c)
        cows.append([g, p, c])
        
    cows.sort(key = lambda x:x[0])

    leaderboard = {"Bessie":7,"Elsie":7,"Mildred":7}
    previousLeader = []
    leaderboardMax = -1
    counter = 0 
    for cow in cows:
        leaderboard[cow[1]] += cow[2]
        leaderboardMax = max(leaderboard.values())
        leaders = []
        for key in leaderboard:
            if leaderboard[key] == leaderboardMax:
                leaders.append(key)
        leaders.sort()
        if leaders != previousLeader:
            counter += 1
        previousLeader = leaders
    return counter

    
runTests()