from rich.console import Console
from rich.table import Table
# from rich import box
from rich import print


days = 19

print("[orange3]Carry-on limit LH, SAS: (55x40x23/8kg+40x30x15), BA: 56x24x35+40x30x15, AA:22x14x9")
print("[orange3]SW: 24x16x10 + 40x30x15cm, Norw: 55x23x40cm+(under)30x20x38cm")

hdr = {"pass": "BLUE PASSPORT CASE",
        "get_bring": "Get and Bring",
        "blue_med": "MEDS - BLUE CASE ({days+2})",
        "extra_cp": "Extra CP supplies x1 PILL dispenser loaded",
        "orthotics": "[total of 2 pr orthotics]",
        "shave_kit": "Shaving kit",
        "cable_sack": "Cable Sack",
        "case_sm_thin": "Small thin case",
        "case_in_flight": "In flight case",
        "case_wide_thin": "Wide this case",
        "wear": "WEAR",
       }
case_wide_thin = "Earphones + Audio jack->{firewire (iPhone), thunderbolt (iPad)} adapters"
passp = "Passport"
sv_res = "Sv Residence Permit"
goes = "GOES Card"
bofa = "BofA ATM card (Tr, 6168)"
cap1 = "Cap1"
keys = "Keys"
medicare = "Medicare + Pilgrim + Wellcare cards"

table = Table(title=f"Tenerife, Jan 6-24, 2005 ({days})", box=None)
# table.add_column("Released", justify="right", style="cyan", no_wrap=True)
# table.add_column("Title", style="magenta")
# table.add_column("Box Office", justify="right", style="green")

table.add_row(hdr["case_wide_thin"])
table.add_row(hdr["blue_med"])
table.add_row(hdr["extra_cp"])
table.add_row(hdr["orthotics"])
table.add_row(hdr["shave_kit"])
table.add_row(hdr["cable_sack"])
table.add_row(hdr["case_sm_thin"])
table.add_row(hdr["case_in_flight"])
table.add_row(hdr["case_wide_thin"])
# table.add_row("Dec 15, 2017", "Star Wars Ep. V111: The Last Jedi", "$1,332,539,889")

console = Console()
console.print(table)
