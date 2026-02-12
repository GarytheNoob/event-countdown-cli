from rich.console import Console
from rich.table import Table

from .event import Event


def display_events(events: list[Event]) -> None:
    console = Console()
    table = Table.grid(pad_edge=True, padding=(0, 2))

    # table.add_column()
    table.add_column(no_wrap=True)
    table.add_column(justify="right", min_width=8)
    table.add_column(justify="left")

    for event in events:
        # date_str = event.date.strftime("%Y-%m-%d")
        title = event.title
        tdelta = event.tdelta.days
        noun = "day" if abs(tdelta) == 1 else "days"
        if tdelta > 0:
            table.add_row(
                # date_str,
                f"[italic sky_blue2]{title}",
                f"[bold sky_blue1]{tdelta}",
                f"[sky_blue2]{noun} later",
            )
        elif tdelta < 0:
            table.add_row(
                # date_str,
                f"[italic orange3]{title}",
                f"[bold orange1]{-tdelta}",
                f"[orange3]{noun} ago",
            )
        else:
            table.add_row(
                # date_str,
                f"[yellow i]{title}",
                "[bold yellow]0",
                "[yellow]days",
            )

    console.print(table)
