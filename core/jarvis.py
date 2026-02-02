from rich.console import Console
console = Console()

class Jarvis:
    def __init__(self, owner):
        self.owner = owner

    def boot(self):
        console.print("[bold cyan]Jarvis 5.0 Wealth OS booting...[/bold cyan]")
        console.print(f"[green]Owner:[/green] {self.owner}")
        console.print("[yellow]Mission:[/yellow] Build wealth, businesses & systems")

    def speak(self, message):
        console.print(f"[bold magenta]Jarvis:[/bold magenta] {message}")
