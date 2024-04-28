from fpdf import FPDF
from datetime import datetime

now = datetime.now()
pdf = FPDF('L','mm','A4')

pdf.add_page()

txt1 = "Assessment Report"
txt2 = "By: Uplabdhi Singh"
dateTime = now.strftime("%d/%m/%Y %H:%M:%S")

pdf.set_font('Times', 'B', 28)
pdf.cell(270, 10, txt1, 0, 1, 'C')

pdf.set_font('Times', size = 14)
pdf.cell(270, 10, txt2, 0, 1, 'C')
pdf.cell(270, 10, dateTime, 0, 1, 'C')
pdf.line(x1 = 10, y1 = 40, x2 = 280, y2 = 40)

txtScanFile = open("reportOutput.txt", "r")

pdf.set_font("Times", size = 12)
for x in txtScanFile:
	pdf.cell(40, 10, x, 0, 1)
	
pdf.output("reportPDF.pdf")
