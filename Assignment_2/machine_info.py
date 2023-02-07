#import os
#os.system("settings")
#import subprocess
#subprocess.Popen([file],shell=True)
from fpdf import FPDF
import platform

print(platform.uname())
pdf = FPDF()

pdf.add_page()

pdf.set_font("Arial", size = 15)

f = platform.uname()

for x in f:
	pdf.cell(200, 10, txt=x, ln=1, align='C')
	
pdf.output("output.pdf")

import test
