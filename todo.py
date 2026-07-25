import sys

from rich.console import Console
from rich.table import Table
from rich.panel import Panel

# make sure ✓ and emojis print on Windows instead of crashing
sys.stdout.reconfigure(encoding="utf-8")

console = Console()

FILENAME = "tasks.txt"


def load_tasks(filename):
    """Read tasks back from the file. Returns a list of dicts."""
    tasks = []
    try:
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line == "":
                    continue
                done, title = line.split("|", 1)
                tasks.append({"title": title, "done": done})
    except FileNotFoundError:
        pass  # no file yet just means no tasks, that's fine
    return tasks


def save_tasks(tasks, filename):
    """Write every task to the file, one per line as  done|title."""
    with open(filename, "w", encoding="utf-8") as f:
        for task in tasks:
            f.write(f"{task['done']}|{task['title']}\n")


def show_tasks(tasks):
    """Print the tasks as a colored table."""
    if len(tasks) == 0:
        console.print("[dim]no tasks yet — add one![/dim]")
        return

    table = Table(title="My Tasks", title_style="bold cyan", border_style="blue")
    table.add_column("#", justify="right", style="dim")
    table.add_column("Status", justify="center")
    table.add_column("Task")

    for i, task in enumerate(tasks, start=1):
        if task["done"] == "1":
            status = "[green]✓[/green]"
            title = f"[green]{task['title']}[/green]"
        else:
            status = "[yellow]○[/yellow]"
            title = task["title"]
        table.add_row(str(i), status, title)

    console.print(table)


def main():
    tasks = load_tasks(FILENAME)  # load once when the app starts

    while True:
        menu = "[bold]1)[/bold] show   [bold]2)[/bold] add   [bold]3)[/bold] mark done   [bold]4)[/bold] quit"
        console.print(Panel(menu, border_style="magenta", expand=False))
        choice = console.input("[bold cyan]choose:[/bold cyan] ")

        if choice == "1":
            show_tasks(tasks)

        elif choice == "2":
            new_task = console.input("[green]new task:[/green] ")
            tasks.append({"title": new_task, "done": "0"})
            save_tasks(tasks, FILENAME)
            console.print("[green]✓ added[/green]")

        elif choice == "3":
            show_tasks(tasks)
            num = console.input("[yellow]number to mark done:[/yellow] ")
            if num.isdigit() and 1 <= int(num) <= len(tasks):
                tasks[int(num) - 1]["done"] = "1"
                save_tasks(tasks, FILENAME)
                console.print("[green]✓ done![/green]")
            else:
                console.print("[red]that number doesn't exist[/red]")

        elif choice == "4":
            console.print("[cyan]byyy[/cyan]")
            break

        else:
            console.print("[red]pick 1, 2, 3 or 4[/red]")


if __name__ == "__main__":
    main()
