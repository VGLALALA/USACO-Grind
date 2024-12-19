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
    
    in_files = sorted([f for f in files if f.endswith('.in')])
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
        result = thing(lines)
        
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
    directions = {"N": (0, 1), "S": (0, -1), "W": (-1, 0), "E": (1, 0)}
    curpos = (0, 0)
    curtime = 0
    visited = {curpos: curtime}
    min_time_diff = float('inf')

    for i in range(n):
        d, s = inp[i + 1].split()
        s = int(s)
        for _ in range(s):
            curpos = (curpos[0] + directions[d][0], curpos[1] + directions[d][1])
            curtime += 1
            if curpos in visited:
                time_diff = curtime - visited[curpos]
                if time_diff < min_time_diff:
                    min_time_diff = time_diff
            visited[curpos] = curtime

    return -1 if min_time_diff == float('inf') else min_time_diff



runTests()