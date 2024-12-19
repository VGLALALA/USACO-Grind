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
                expected = [int(line.strip()) for line in f.readlines()]
                if result == expected:
                    console.print(Panel("[green]✓ Passed![/green]", title="Result", style="bold green", width=40))
                else:
                    console.print(Panel(f"[red]✗ Failed! Expected {expected}, got {result}[/red]", title="Result", style="bold red", width=40))
        else:
            console.print(Panel(f"[yellow]Answer: {result}[/yellow]", title="Result", style="bold yellow", width=40))

def thing(inp):
    from collections import Counter
    n = int(inp[0])
    print(n)
    outdic = {chr(i): 0 for i in range(ord('a'), ord('z') + 1)}
    for i in range(n):
        w1, w2 = inp[i + 1].split()
        c1, c2 = Counter(w1), Counter(w2)
        max_count = {char: max(c1.get(char, 0), c2.get(char, 0)) for char in set(w1 + w2)}
        for char, count in max_count.items():
            outdic[char] += count
    out = [outdic[chr(i)] for i in range(ord('a'), ord('z') + 1)]
    return out

runTests()