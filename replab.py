# https://stackoverflow.com/questions/9855445/how-to-change-text-font-color-in-reportlab-pdfgen
# https://docs.reportlab.com/reportlab/userguide/ch3_fonts/
# https://www.blog.pythonlibrary.org/2013/07/19/reportlab-all-about-fonts/

# import the canvas object
from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.platypus.tables import TableStyle, Table

# create a Canvas object with a filename
chello = canvas.Canvas("rl-hello_again.pdf", pagesize=(595.27, 841.89))  # A4 pagesize
# draw a string at x=100, y=800 points
# point ~ standard desktop publishing (72 DPI)
# coordinate system:
#   y
#   |
#   |   page
#   |
#   |
#   0-------x
chello.setFillColorRGB(1,0,0)
chello.drawString(50, 780, "Hello Again")
# finish page
chello.showPage()
# construct and save file to .pdf
chello.save()


ctable = canvas.Canvas("table.pdf", pagesize=A4) # 595 x 842 is the page dimensions for A4 at 72DPI
data=  [['00', '01', '02', '03', '04'],
        ['10', '11', '12', '13', '14'],
        ['20', '21', '22', '23', '24'],
        ['30', '31', '32', '33', '34']]
STYLE = TableStyle([('BACKGROUND',(1,1),(-2,-2),colors.green),
                        ('TEXTCOLOR',(0,0),(1,-1),colors.red)])
t=Table(data, style=STYLE)

#t.setStyle(TableStyle([('BACKGROUND',(1,1),(-2,-2),colors.green),
#                        ('TEXTCOLOR',(0,0),(1,-1),colors.red)]))
ctable.showPage()
ctable.save()
