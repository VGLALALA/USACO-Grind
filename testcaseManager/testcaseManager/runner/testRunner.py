import os
import inspect
from rich.console import Console
from rich.table import Table
from rich.panel import Panel

class TestRunner:
    def __init__(self):
        self.console = Console()

    def fileDetect(self, processTestCase):
        # Get the directory of the processTestCase function
        test_case_dir = os.path.dirname(inspect.getfile(processTestCase))
        files = []
        for file in os.listdir(test_case_dir):
            if file.endswith('.in') or file.endswith('.out'):
                files.append(file)
        
        if len(files) == 0:
            self.console.print(Panel("[red]No input/output files found in current directory[/red]", title="Error", style="bold red"))
            return
            
        self.console.print(Panel("\n[cyan]Available test files:[/cyan]", title="Files", style="bold cyan"))
        
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
                
        self.console.print(table)
        return in_files, test_case_dir

    def runTests(self, processTestCase, output_mode="int"):
        if not callable(processTestCase):
            raise ValueError("The processTestCase argument must be a callable function.")
        
        in_files, test_case_dir = self.fileDetect(processTestCase)
        if not in_files:
            return

        # Get user input for test case selection
        selected_indices = input("Enter test case numbers separated by space (or press Enter to run all): ").strip()
        if selected_indices:
            selected_indices = set(map(int, selected_indices.split()))
            in_files = [f for i, f in enumerate(in_files, 1) if i in selected_indices]

        for in_file in in_files:
            self.console.print(Panel(f"[cyan]Testing {in_file}...[/cyan]", title="Test", style="bold cyan", width=40))
            
            with open(os.path.join(test_case_dir, in_file), 'r') as f:
                input_str = f.read()
            lines = input_str.strip().split('\n')
            result = processTestCase(lines)
            
            out_file = os.path.join(test_case_dir, in_file[:-3] + '.out')
            if os.path.exists(out_file):
                with open(out_file, 'r') as f:
                    content = f.read().strip()
                    if output_mode == "int":
                        expected = int(content)
                    elif output_mode == "int_list":
                        expected = list(map(int, content.split()))
                    elif output_mode == "str":
                        expected = content
                    elif output_mode == "str_list":
                        expected = content.split()
                    else:
                        raise ValueError("Invalid output mode. Must be 'int', 'int_list', 'str', or 'str_list'")

                    if result == expected:
                        self.console.print(Panel("[green]✓ Passed![/green]", title="Result", style="bold green", width=40))
                    else:
                        self.console.print(Panel(f"[red]✗ Failed! Expected {expected}, got {result}[/red]", title="Result", style="bold red", width=40))
            else:
                self.console.print(Panel(f"[yellow]Answer: {result}[/yellow]", title="Result", style="bold yellow", width=40))