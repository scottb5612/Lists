from rich.console import Console
from rich.table import Table
from rich import print

# Local imports
import defs

if __name__ == '__main__':

    days = 19

    print("[orange3]Carry on limits")
    for c in defs.carry_on_geo:
        print(f"[orange3]{c}")
    print()

    table = Table(title=f"Tenerife, Jan 6-24, 2005 ({days})", box=None)
    # table.add_column("Released", justify="right", style="cyan", no_wrap=True)
    # table.add_column("Title", style="magenta")
    # table.add_column("Box Office", justify="right", style="green")

    table.add_row(defs.hdr["case_wide_thin"])
    table.add_row(defs.hdr["blue_med"])
    table.add_row(defs.hdr["extra_cp"])
    table.add_row(defs.hdr["orthotics"])
    table.add_row(defs.hdr["shave_kit"])
    table.add_row(defs.hdr["cable_sack"])
    table.add_row(defs.hdr["case_sm_thin"])
    table.add_row(defs.hdr["case_in_flight"])
    table.add_row(defs.hdr["case_wide_thin"])

    console = Console()
    console.print(table)
