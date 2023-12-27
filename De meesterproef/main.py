import typer 
import subprocess
from PyInquirer import prompt, print_json, Separator
from rich import print as rprint

app = typer.Typer()

@app.command("hi")
def sample_func():
    rprint("[red bold]Hi[/red bold] [yellow]World[yellow]")

@app.command("hello")
def sample_func():
    rprint("[red bold]Hello[/red bold] [yellow]World[yellow]")

if __name__ == "__main__":
    app()