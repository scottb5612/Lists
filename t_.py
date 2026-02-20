# https://stackoverflow.com/questions/9855445/how-to-change-text-font-color-in-reportlab-pdfgen
# https://docs.reportlab.com/reportlab/userguide/ch3_fonts/
# https://www.blog.pythonlibrary.org/2013/07/19/reportlab-all-about-fonts/

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus.tables import TableStyle, Table

from rich.console import Console
from rich.table import Table
# from rich import box
from rich import print

# Local imports
import defs

if __name__ == '__main__':

    days = 19
    place = "Tenerife"
    place_abbrev = "Ten"
    dates = "06-24_Jan2025"
    title=f"{place}, Jan 6-24, 2005 ({days}d)
    # table = Table(title=f"Tenerife, Jan 6-24, 2005 ({days})", box=None)
    ct = canvas.Canvas("t_.pdf", pagesize=(595.27, 841.89))  # A4 pagesize
    ct.setFillColorRGB(0.7,0,0.5)
    chello.drawString(50, 780, "Hello Again")

    print("[orange3]Carry on limits")
    for c in defs.carry_on_geo:
        print(f"[orange3]{c}")
    print()


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
